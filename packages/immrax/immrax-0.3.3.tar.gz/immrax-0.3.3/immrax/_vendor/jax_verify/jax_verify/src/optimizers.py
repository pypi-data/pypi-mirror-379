# coding=utf-8
# Copyright 2023 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generic Optimizers for optimization based bound computation."""
import abc
import functools
from typing import Callable, Optional, Sequence, Tuple

import jax
from jax import numpy as jnp
from jax_verify.src import utils
from jax_verify.src.types import Nest, Tensor  # pylint: disable=g-multiple-import
import optax

ParamSet = Nest[Tensor]
ProgressStats = Nest[Tensor]
TensorFun = Callable[[ParamSet], Tensor]
ProjectFun = Callable[[ParamSet], ParamSet]


class Optimizer(metaclass=abc.ABCMeta):
  """Base class defining the interface of the optimizers for JaxVerify."""

  def __init__(self, log_optimization: bool = False):
    self._log_optimization = log_optimization
    self._opt_vals = None

  @abc.abstractmethod
  def optimize_fn(self,
                  obj_fun: TensorFun,
                  project_params: ProjectFun
                  ) -> Callable[[ParamSet], ParamSet]:
    """Return a function that minimizes obj_fun.

    The parameters should be in the set onto which `project_params` project to.

    Args:
      obj_fun: Function to minimize.
      project_params: Function to project parameters onto the feasible set of
        parameters. Returns the feasible arguments as a tuple.
    Returns:
      opt_fun: Function taking initial parameters and returning optimized ones.
    """

  def get_last_opt_run(self) -> Tensor:
    if not self._log_optimization:
      raise ValueError('Optimizer not configured to collect objective values.')
    if self._opt_vals is None:
      raise ValueError('Optimizer not called.')
    return self._opt_vals


class OptaxOptimizer(Optimizer):
  """Optimizer relying on Optax GradientTransformation to minimize an objective.

  Performs num_steps steps of updates, while keeping track of the lowest result
  obtained so far.
  """

  def __init__(
      self,
      opt_gt: optax.GradientTransformation,
      *,
      num_steps: int,
      log_optimization: bool = False,
  ):
    super().__init__(log_optimization)
    self._opt_gt = opt_gt
    self._num_steps = num_steps

  def optimize_fn(
      self,
      obj_fun: TensorFun,
      project_params: ProjectFun,
  ) -> Callable[[ParamSet], ParamSet]:
    """Returns a function that minimizes obj_fun."""
    val_and_grad_fn = jax.value_and_grad(obj_fun)

    def update_state(
        state: Tuple[ParamSet, ParamSet, ParamSet, Tensor],
    ) -> Tuple[ParamSet, ParamSet, ParamSet, Tensor]:
      """Update the state of the optimization.

      The loop state consists of:
        - params: Current value of the parameters in the optimization.
        - opt_state: State of the optax optimizer.
        - best_params: Value of the parameters that gave the lowest results.
        - best_val: Objective value achieved for the best params.

      Args:
        state: The loop state.
      Returns:
        next_state: The updated status of the loop after one more step of
          optimization.
        val: The value of the optimzation at this point.
      """
      params, opt_state, best_params, best_val = state
      val, params_grad = val_and_grad_fn(params)

      # Compute the next step in the optimization process.
      updates, next_opt_state = self._opt_gt.update(params_grad, opt_state)
      next_params = optax.apply_updates(params, updates)
      next_params = project_params(next_params)

      # Update the best params seen.
      where_improved = functools.partial(jnp.where, val < best_val)
      next_best_params = jax.tree_util.tree_map(where_improved,
                                                params, best_params)
      next_best_val = where_improved(val, best_val)

      next_state = (next_params, next_opt_state,
                    next_best_params, next_best_val)
      return next_state, val

    def opt_fun(init_params):
      best_params = init_params
      if self._num_steps:
        # Perform the optimization if we do at least one step.
        init_opt_state = self._opt_gt.init(init_params)
        _, _, best_params, _ = self.opt_loop(
            update_state,
            (init_params, init_opt_state, best_params, jnp.inf))
      return best_params

    return opt_fun

  def opt_loop(self, body_fun, init_vals):
    """Calls `body_fun` num_steps times to perform the optimization."""
    if self._log_optimization:
      step_fun = lambda carry, _: body_fun(carry)
      final_carry, opt_vals = jax.lax.scan(step_fun, init_vals, None,
                                           length=self._num_steps)
      self._opt_vals = opt_vals
      return final_carry
    else:
      # We drop the first value passed to the step function, because it
      # correspond to the iteration number.
      # We drop the second returned value, which is the current
      # value of the optimization that we do not need to log.
      step_fun = lambda _, carry: body_fun(carry)[0]
      return utils.fori_loop_no_backprop(0, self._num_steps,
                                         step_fun, init_vals)


def _sum_fn(fn, *args, **kwargs):
  out = fn(*args, **kwargs)
  summand = out[0] if isinstance(out, tuple) else out
  return summand.sum(), out


def _quad_approx(x: ParamSet, y: ParamSet, grad_y: ParamSet, step_size: Tensor
                 ) -> Tensor:
  """Compute the quadratic term used in the backtracking linesearch."""
  def quad_approx_var(x_var: Tensor, y_var: Tensor, grady_var: Tensor):
    diff = x_var - y_var
    return ((diff * grady_var).sum()
            + 0.5 / step_size * (diff**2).sum())
  per_var_quad_approx = jax.tree_util.tree_map(quad_approx_var, x, y, grad_y)
  return sum(jax.tree_util.tree_leaves(per_var_quad_approx))


def _broadcast_back_like(to_brd: Tensor, target: Tensor) -> Tensor:
  """Broadcast matching dimensions from the front rather than the back.

  By default, numpy/jax match dimensions from the back. In this case, we
  want to have a different step-size for each batch-element (so the common
  dimension is at the front). This function adds dummy dimensions so that
  broadcasting can happen as we want it.

  Args:
    to_brd: Tensor that we want to broadcast.
    target: Tensor that we want to be able to be broadcasted against.
  Returns:
    brd: Broadcasted tensor.
  """
  nb_add_dims = target.ndim - to_brd.ndim
  return jnp.reshape(to_brd, to_brd.shape + (1,) * nb_add_dims)


class LinesearchFistaOptimizer(Optimizer):
  """FISTA with line search.

  As done in the "An efficient nonconvex reformulation of stagewise convex
  optimization problems" NeurIPS2020 submission. This is a reimplementation
  of the code at:
  l/d/r/r_v/verification/ibp/verification/nonconvex_optimizable_bounds.py
  """

  def __init__(self,
               num_steps: int,
               max_step_size: float = 100.0,
               min_step_size: float = 1e-5,
               beta_l: float = 0.5,
               beta_h: float = 1.5,
               check_convergence_every: int = 1,
               log_optimization: bool = False):
    super().__init__(log_optimization)
    self._num_steps = num_steps
    self._max_step_size = max_step_size
    self._min_step_size = min_step_size
    self._beta_l = beta_l
    self._beta_h = beta_h
    self._check_convergence_every = check_convergence_every

  def optimize_fn(
      self,
      obj_fun: TensorFun,
      project_params: ProjectFun,
      not_converged_fun: Optional[Callable[[ParamSet], bool]] = None):
    """Returns a function that minimizes obj_fun.

    Args:
      obj_fun: Functions to minimize (If this is an array, we assume that all
        outputs needs to be minimized.)
      project_params: Function to project parameters onto the feasible set of
        parameters.
      not_converged_fun: Function to indicate whether the optimization can be
        early stopped because it has converged.
    Returns:
      opt_fun: Function taking initial parameters and returning optimized ones.
    """
    # If no function is provided to identify convergence, we assume
    # that the optmization has not converged at all time.
    not_converged_fun = not_converged_fun or (lambda *_: True)
    to_grad_fun = functools.partial(_sum_fn, obj_fun)
    val_and_grad_fn = jax.value_and_grad(to_grad_fun, has_aux=True)

    ## Define the functions for the backtracking line search
    def pgd_step(current: ParamSet, grad: ParamSet, step_size: Tensor):
      def step_per_var(curr, g):
        brd_step_size = _broadcast_back_like(step_size, g)
        return curr - brd_step_size * g
      gd_step = jax.tree_util.tree_map(step_per_var, current, grad)
      return project_params(gd_step)

    def should_decrease(step_size: Tensor,
                        y_stats: Tuple[ParamSet, ParamSet, ParamSet]):
      y, obj_y, grad_y = y_stats
      new_x = pgd_step(y, grad_y, step_size)
      val_newx = obj_fun(new_x)
      val_qapprox = obj_y + _quad_approx(new_x, y, grad_y, step_size)
      per_sp_insufficient_progress = val_newx >= val_qapprox
      step_size_not_min = step_size > self._min_step_size
      # Perform the updates
      return jnp.logical_and(step_size_not_min, per_sp_insufficient_progress)

    # This will be performed in jax.lax.while_loop, with the following arguments
    # ls_loop_args:
    #   need_lower: Boolean array indicating for each step_size if we still
    #     needs to lower the step size.
    #   step_size: Array of step size being used.
    #   y_stats: Tuple with y, f(y) and grad(y), so that we don't have to keep
    #     recomputing it.
    def lower_stepsize_if_needed(ls_loop_args):
      """Reduce the step size for all the optimization target that need it.

      Update the check to see if it needs to be reduced further.

      Args:
        ls_loop_args: Line search loop arguments
      Returns:
        new_ls_loop_args: Updated line search loop arguments
      """
      need_lower, step_size, y_stats = ls_loop_args
      new_step_size = jnp.where(need_lower,
                                self._beta_l * step_size, step_size)
      new_need_lower = should_decrease(new_step_size, y_stats)
      return new_need_lower, new_step_size, y_stats

    need_lower_stepsize = lambda ls_loop_args: ls_loop_args[0].any()

    ## Define the function for the optimization loop
    # Perform the Fista with backtracking line search algorithm, as described
    # in "A Fast Iterative Shrinkage-Thresholding Algorithm", Beck and Teboulle
    # The only change is that we increase the step size by a factor of
    # self._beta_h for step size that didn't need to be reduced at all during
    # the linesearch.
    # This is performed in a jax.lax.while_loop, with the following arguments:
    # opt_loop_args:
    #   it: Iteration counter
    #   x, y: variable set
    #   gamma: float, coefficient used for the momentum (t_k in the paper)
    #   step_size: Array containing the current values of the step size.
    #   last_obj_value: Last value of obj(j)
    # We stop either based on a maximum number of iterations, or based on the
    # given convergence criterion, which is checked every
    # self._check_convergence_every iterations.
    def fista_with_linesearch_step(opt_loop_args):
      it, x, y, gamma, step_size, _ = opt_loop_args
      # Compute f_y and d(f_y)/d(y)
      # We ignore the first returned value which correspond to the sum of the
      # objectives rather than the individual objectives.
      (_, obj_y), grad_y = val_and_grad_fn(y)

      # Compute the step size to use with a line search
      y_stats = y, obj_y, grad_y
      ini_need_lower = should_decrease(step_size, y_stats)
      _, new_step_size, _ = jax.lax.while_loop(
          need_lower_stepsize,
          lower_stepsize_if_needed,
          (ini_need_lower, step_size, y_stats))

      # Perform the updates
      new_x = pgd_step(y, grad_y, new_step_size)
      new_gamma = 1 + jnp.sqrt(1 + gamma ** 2) / 2
      coeff = (gamma - 1) / new_gamma
      new_y = jax.tree_util.tree_map(
          lambda new, old: new + coeff * (new - old), new_x, x)

      # Increase the step size of the samples that didn't need reducing.
      new_step_size = jnp.where(ini_need_lower,
                                new_step_size, self._beta_h * new_step_size)

      return it + 1, new_x, new_y, new_gamma, new_step_size, obj_y

    def continue_criterion(opt_loop_args):
      it, x, *_ = opt_loop_args
      not_all_iterations = it < self._num_steps
      opt_not_converged = jax.lax.cond(
          (it % self._check_convergence_every) == 0.,
          not_converged_fun,
          lambda _: jnp.array(True),
          operand=x)
      return jnp.logical_and(opt_not_converged, not_all_iterations)

    def optimize(ini_x: ParamSet) -> ParamSet:
      ini_y = ini_x
      gamma = jnp.array(0.)
      nb_targets = jax.eval_shape(obj_fun, ini_x).shape
      step_size = self._max_step_size * jnp.ones(nb_targets)
      init_val = jnp.inf * jnp.ones(nb_targets)
      it = jnp.array(0)

      _, final_x, _, _, _, _ = self.opt_loop(
          continue_criterion,
          fista_with_linesearch_step,
          (it, ini_x, ini_y, gamma, step_size, init_val))
      return final_x

    return optimize

  def opt_loop(self, continue_fun, update_fun, init_vals):
    """Performs the optimzation.

    The step is defined by the `update_fun` function, and the optimization is
    run for a maximum of self._num_steps, unless `continue_fun` returns False
    at any point.

    Args:
      continue_fun: Function indicating whether the optimization has converged.
      update_fun: Function performing one step of optimization.
      init_vals: Initial value of the optimizition variables.
    Returns:
      The final state of the optimzation variables.
    """
    if self._log_optimization:
      # We want to log the data throughout so we need the number of steps to
      # remain the same whatever happens, but we also don't want the
      # optimization (including the early stopping) to change just because we're
      # logging it. We're wrapping the function to add a marker of whether or
      # not the optimization has finished. If it has, we just stop updating the
      # values.
      # We also extract the value of the objective, which is the last element of
      # the carry, so that we can extract it from the scan loop.
      def step_fun(wrapped_loop_args, _):
        stopped, *opt_loop_args = wrapped_loop_args
        should_continue = continue_fun(opt_loop_args)
        new_stopped = jnp.logical_or(stopped, jnp.logical_not(should_continue))
        new_opt_loop_args = jax.lax.cond(new_stopped, tuple, update_fun,
                                         operand=opt_loop_args)
        val = new_opt_loop_args[-1]
        return (new_stopped, *new_opt_loop_args), val
      ini_stopped = jnp.array(True)
      (_, *final_carry), opt_vals = jax.lax.scan(
          step_fun, (ini_stopped, *init_vals), None, length=self._num_steps)
      self._opt_vals = opt_vals
      return final_carry
    else:
      return jax.lax.while_loop(continue_fun, update_fun, init_vals)


class PortfolioOptimizer(Optimizer):
  """Optimizer that combines several existing optimizers.

  Runs all of them independently and give the best result.
  """

  def __init__(self, optimizers: Sequence[Optimizer],
               log_optimization: bool = False):
    super().__init__(log_optimization)
    self._optimizers = optimizers
    if log_optimization:
      self._best_optimizer = 0

  def optimize_fn(self,
                  obj_fun: TensorFun,
                  project_params: ProjectFun
                  ) -> Callable[[ParamSet], ParamSet]:
    """Returns a functions that minimizes obj_fun."""

    base_opt_funs = [choice_opt.optimize_fn(obj_fun, project_params)
                     for choice_opt in self._optimizers]

    def opt_fun(initial_params):
      best_params = initial_params
      best_score = jnp.inf

      for opt_idx, base_opt_fun in enumerate(base_opt_funs):
        opt_params = base_opt_fun(initial_params)
        score = obj_fun(opt_params).sum()
        where_improved = functools.partial(jnp.where, score < best_score)

        best_params = jax.tree_util.tree_map(where_improved, opt_params,
                                             best_params)
        if self._log_optimization:
          self._best_optimizer = where_improved(jnp.asarray(opt_idx),
                                                self._best_optimizer)
        best_score = where_improved(score, best_score)

      return best_params

    return opt_fun

  def get_last_opt_run(self) -> Tensor:
    if not self._log_optimization:
      raise ValueError('Optimizer not configured to collect objective values.')
    # TODO: Make this jit compliant if it becomes necessary by padding
    # things to size.
    return self._optimizers[int(self._best_optimizer)].get_last_opt_run()
