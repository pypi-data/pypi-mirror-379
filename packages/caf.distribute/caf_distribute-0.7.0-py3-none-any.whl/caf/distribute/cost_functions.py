# -*- coding: utf-8 -*-
"""Collection of cost functions to be used with distribution models."""
from __future__ import annotations

# Built-Ins
import enum
import inspect
import logging
import random
from typing import Any, Callable, Mapping, Optional

# Third Party
import numpy as np

# pylint: disable=import-error,wrong-import-position
from caf.toolkit import math_utils

# pylint: enable=import-error,wrong-import-position

# # # CONSTANTS # # #
LOG = logging.getLogger(__name__)


# # # CLASSES # # #
@enum.unique
class BuiltInCostFunction(enum.Enum):
    """Enum of the built-in cost functions for easy access."""

    TANNER = "tanner"
    LOG_NORMAL = "log_normal"

    def get_cost_function(self) -> CostFunction:
        """Get the Class defining this cost function."""
        if self == BuiltInCostFunction.TANNER:
            return CostFunction(
                name=self.name,
                params={"alpha": (-1, 1), "beta": (-1, 1)},
                default_params={"alpha": 0.1, "beta": -0.1},
                function=tanner,
            )

        if self == BuiltInCostFunction.LOG_NORMAL:
            return CostFunction(
                name=self.name,
                params={"sigma": (0, 5), "mu": (0, 10)},
                default_params={"sigma": 1, "mu": 2},
                function=log_normal,
            )

        raise ValueError(f"No definition exists for {self} built in cost function")


class CostFunction:
    """Abstract Class defining how cost function classes should look.

    If a new cost function is needed, then a new class needs to be made
    which inherits this abstract class.
    """

    _default_param_val = 1

    def __init__(
        self,
        name: str,
        params: Mapping[str, tuple[float, float]],
        function: Callable,
        default_params: Optional[Mapping[str, float | int]] = None,
    ):
        self.name = name
        self.function = function

        # Split params
        self.param_names = list(params.keys())
        self.param_min = {k: min(v) for k, v in params.items()}
        self.param_max = {k: max(v) for k, v in params.items()}

        # Populate the default parameters
        default_params = dict() if default_params is None else default_params
        def_val = self._default_param_val
        self.default_params = {k: default_params.get(k, def_val) for k in self.param_names}

        self.kw_order = list(inspect.signature(self.function).parameters.keys())[1:]
        for val in ["max_return_val", "min_return_val"]:
            if val in self.kw_order:
                self.kw_order.remove(val)

        # Validate the params and cost function
        try:
            self.function(np.array(1e-2), **self.param_max)
        except TypeError as exc:
            raise ValueError(
                f"Received a TypeError while testing the given params "
                f"definition and cost function will work together. Have the "
                f"params been defined correctly for the given function?\n"
                f"Tried passing in '{self.param_names}' to function "
                f"{self.function}."
            ) from exc

    @property
    def parameter_names(self):
        """Return the key-word names of the cost function params."""
        return self.kw_order

    def validate_params(self, param_dict: dict[str, Any]) -> None:
        """Check the given values are valid and within min/max ranges.

        Validates that the param dictionary given contains only and all
        expected parameter names as keys, and that the values for each key
        fall within the acceptable parameter ranges.

        Parameters
        ----------
        param_dict:
            A dictionary of values to validate. Should be in
            {param_name: param_value} format.

        Raises
        ------
        ValueError:
            If any of the given params do not have valid name, or their values
            fall outside the min/max range defined in this class.
        """
        # Init
        # math_utils.check_numeric(param_dict)

        # Validate
        for name, value in param_dict.items():
            # Check name is valid
            if name not in self.param_names:
                raise ValueError(
                    f"Parameter '{name}' is not a valid parameter for "
                    f"CostFunction {self.name}"
                )

            # Check values are valid
            min_val = self.param_min[name]
            max_val = self.param_max[name]

            if value < min_val or value > max_val:
                raise ValueError(
                    f"Parameter '{name}' falls outside the acceptable range "
                    f"of values. Value must be between {min_val} and "
                    f"{max_val}. Got {value}."
                )

            if value > self.param_max[name]:
                raise ValueError()

    def random_valid_params(self) -> dict[str, Any]:
        """Get random parameter values for this cost function."""
        return_val = dict.fromkeys(self.param_names)
        for name in return_val:
            return_val[name] = random.uniform(self.param_min[name], self.param_max[name])
        return return_val

    def calculate(self, base_cost: np.ndarray, **kwargs) -> np.ndarray:
        """Calculate the actual cost using self.function.

        Before calling the cost function the given cost function params will
        be checked that they are within the min and max values passed in when
        creating the object. The cost function will then be called and the
        value returned.

        Parameters
        ----------
        base_cost:
            Array of the base costs.

        kwargs:
        Parameters of the cost function to pass to self.function.

        Returns
        -------
        costs:
            Output from self.function, same shape as `base_cost`.

        Raises
        ------
        ValueError:
            If the given cost function params are outside the min/max range
            for this class.
        """
        self.validate_params(kwargs)
        return self.function(base_cost, **kwargs)


# # # FUNCTIONS # # #
def tanner(
    base_cost: np.ndarray,
    alpha: float,
    beta: float,
    min_return_val: float = 1e-150,
    max_return_val: float = 1e100,
) -> np.ndarray:
    r"""Apply the tanner cost function.

    Parameters
    ----------
    base_cost : np.ndarray
        Array of the base costs.

    alpha, beta : float
        Parameters of the tanner cost function, see Notes.

    min_return_val: float
        The minimum value allowed in the return. Avoid return arrays with values
        such as 1e-300 which lead to overflow errors when divisions are made.

    max_return_val: float
        The maximum value allowed in the return. Avoid return arrays with values
        such as np.inf which lead to errors.

    Returns
    -------
    tanner_costs:
        Output from the tanner equation, same shape as `base_cost`.

    Notes
    -----
    Formula used for this function is:

    .. math:: f(C_{ij}) = C_{ij}^\alpha \cdot \exp(\beta C_{ij})

    where:

    - :math:`C_{ij}`: cost from i to k.
    - :math:`\alpha, \beta`: calibration parameters.
    """
    math_utils.check_numeric({"alpha": alpha, "beta": beta})

    # Don't do 0 to the power in case alpha is negative
    # 0^x where x is anything (other than 0) is always 0
    power = np.float_power(
        base_cost,
        alpha,
        out=np.zeros_like(base_cost, dtype=float),
        where=base_cost != 0,
    )
    exp = np.exp(beta * base_cost)

    # Clip the min values to the min_val
    arr = math_utils.clip_small_non_zero(power * exp, min_return_val)
    return np.minimum(arr, max_return_val)


def log_normal(
    base_cost: np.ndarray,
    sigma: float,
    mu: float,
    min_return_val: float = 1e-150,
) -> np.ndarray:
    r"""Apply of the log normal cost function.

    Parameters
    ----------
    base_cost : np.ndarray
        Array of the base costs.

    sigma, mu : float
        Parameters of the log normal cost function, see Notes.


    min_return_val: float
        The minimum value allowed in the return. Avoid return arrays with values
        such as 1e-300 which lead to overflow errors when divisions are made.

    Returns
    -------
    log_normal_costs:
        Output from the log normal equation, same shape as `base_cost`.

    Notes
    -----
    Formula used for this function is:

    .. math::

        f(C_{ij}) = \frac{1}{C_{ij} \cdot \sigma \cdot \sqrt{2\pi}}
        \cdot \exp\left(-\frac{(\ln C_{ij}-\mu)^2}{2\sigma^2}\right)

    where:

    - :math:`C_{ij}`: cost from i to j.
    - :math:`\sigma, \mu`: calibration parameters.
    """
    # Init
    math_utils.check_numeric({"sigma": sigma, "mu": mu})
    sigma = float(sigma)
    mu = float(mu)

    # We need to be careful to avoid 0 in costs
    # First calculate the fraction
    frac_denominator = base_cost * sigma * np.sqrt(2 * np.pi)
    frac = np.divide(
        1,
        frac_denominator,
        where=frac_denominator != 0,
        out=np.zeros_like(frac_denominator),
    )

    # Now calculate the exponential
    log = np.log(
        base_cost,
        where=base_cost != 0,
        out=np.zeros_like(base_cost).astype(float),
    )
    exp_numerator = (log - mu) ** 2
    exp_denominator = 2 * sigma**2
    exp = np.exp(-exp_numerator / exp_denominator)

    return np.maximum(frac * exp, min_return_val)
