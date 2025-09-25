import logging
from typing import Callable

import numpy as np
import sympy as sp
from lmfit import Model as LMFitModel
from lmfit import Parameters
from lmfit.model import ModelResult
from loguru import logger
from scipy.optimize import root_scalar

from calipytion.model import CalibrationModel, FitStatistics, Parameter
from calipytion.tools.utility import calculate_rmsd

LOGGER = logging.getLogger(__name__)


class Fitter:
    signal_var = "SIGNAL_PLACEHOLDER"

    def __init__(self, equation: str, indep_var: str, params: list[Parameter]):
        self.equation = equation
        self.params = params
        self.indep_var = indep_var
        self.dep_vars = [param.symbol for param in params if param.symbol != indep_var]
        self.model_callable = self._get_model_callable()
        self.lmfit_model: LMFitModel = self._prepare_model()
        self.lmfit_params: Parameters = self._prepare_params()
        self.lmfit_result: ModelResult | None = None

    def fit(self, y: np.ndarray, x: np.ndarray, indep_var_symbol: str) -> FitStatistics:
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        if not isinstance(y, np.ndarray):
            y = np.array(y)

        kwargs = {indep_var_symbol: x}

        self.lmfit_result = self.lmfit_model.fit(
            data=y, params=self.lmfit_params, **kwargs
        )

        self.lmfit_params = self.lmfit_result.params

        self._update_result_params()

        return self.extract_fit_statistics(self.lmfit_result)

    def predict(self, x: np.ndarray) -> np.ndarray:
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        return self.lmfit_model.eval(params=self.lmfit_params, **{self.indep_var: x})

    def calculate_roots(
        self,
        y: np.ndarray,
        lower_bond: float,
        upper_bond: float,
        extrapolate: bool,
    ) -> tuple[np.ndarray, list[float]]:
        """
        Calculate the roots of the equation for the given signals.
        If the extrapolate flag is set to True, the function will try to find the roots

        Args:
            y (np.ndarray): The signals for which the roots should be calculated.
            lower_bond (float): The lower bound for the root search.
            upper_bond (float): The upper bound for the root search.
            extrapolate (bool): If True, the function will try to extrapolate the calibration range.

        Returns:
            tuple[np.ndarray, list[float]]: The roots and the bracket used for the root search.
        """

        root_eq = self._get_root_eq()

        for param in self.params:
            if param.value is None:
                raise ValueError(f"Parameter '{param.symbol}' has no value set.")

        params = [{param.symbol: param.value for param in self.params}] * len(y)
        params = [
            {**param, self.signal_var: signal} for param, signal in zip(params, y)
        ]
        if not extrapolate:
            bracket = [lower_bond, upper_bond]

            roots = []
            failed_signals = []
            for param in params:
                try:
                    root = root_scalar(
                        root_eq, bracket=bracket, args=tuple(param.values())
                    )
                    roots.append(root.root)
                except ValueError:
                    roots.append(np.nan)
                    failed_signals.append(param[self.signal_var])

            return np.array(roots), bracket

        else:
            # update the bracket for the root search
            critical_points = self.calculate_critical_points()
            critical_points = sorted(critical_points, key=lambda x: x[0])

            # monotonically increasing function, no need to define sensible bracket
            if len(critical_points) == 0:
                bracket = [1e12, -1e12]

            elif len(critical_points) == 1:
                # if all signals are above the critical point y, crit must be the lower bound
                if all(y > critical_points[0][1]):
                    bracket = [critical_points[0][0], 1e12]
                # ... must be the upper bound
                elif all(y < critical_points[0][1]):
                    bracket = [1e12, critical_points[0][0]]
                # if signals are above and below the critical point y, extrapolation not possible
                else:
                    bracket = [lower_bond, upper_bond]
                    logger.warning(
                        f"Setting extended calibration range for {self.equation} not possible. Extrapolation not possible."
                    )
            elif len(critical_points) == 2:
                # if crit x1 has lower y value than crit x2, crit x1 must be the lower bound, since only monotonically increasing interval in function
                if critical_points[0][1] < critical_points[1][1]:
                    bracket = [critical_points[0][0], critical_points[1][0]]
                else:
                    if (
                        lower_bond - critical_points[1][0]
                        < critical_points[0][0] - upper_bond
                    ):
                        bracket = [critical_points[0][0], 1e12]
                    else:
                        bracket = [1e12, critical_points[1][0]]

            else:
                bracket = [lower_bond, upper_bond]
                logger.warning(
                    f"More than two critical points found for {self.equation}. Extrapolation not possible."
                )

            roots = []
            failed_signals = []
            for param in params:
                try:
                    # eq = self.equation + " - " + self.signal_var
                    # eqq = sp.sympify(eq)
                    # params_lower = {param.symbol: param.value for param in self.params}
                    # params_upper = {param.symbol: param.value for param in self.params}
                    # params_lower["SIGNAL_PLACEHOLDER"] = 4
                    # params_upper["SIGNAL_PLACEHOLDER"] = 4
                    # print(f"f(lower_bound) = {eqq.subs(params_lower)}")
                    # print(f"f(upper_bound) = {eqq.subs(params_upper)}")
                    root = root_scalar(
                        root_eq,
                        bracket=bracket,
                        args=tuple(param.values()),
                    )
                    roots.append(root.root)
                except ValueError:
                    roots.append(np.nan)
                    failed_signals.append(param[self.signal_var])

            if failed_signals:
                logger.warning(
                    f"Could not find roots for signals: {failed_signals} "
                    f"in extended calibration range {bracket}."
                )

            return np.array(roots), bracket

    # function that allows to define the nearest critical points from the root equation to determine the maximal calibration range during concentration calculations with extrapolation
    def calculate_critical_points(self) -> list[tuple[float, float]]:
        """
        Calculate the critical points of the equation.
        """

        eq = sp.sympify(self.equation)

        for param in self.params:
            if param.value is None:
                raise ValueError(f"Parameter '{param.symbol}' has no value set.")

        params = {param.symbol: param.value for param in self.params}

        eq = eq.subs(params)

        f_prime = sp.diff(eq, self.indep_var)

        critical_points = sp.solve(f_prime, self.indep_var)

        # get respective y values for the critical points
        y_values = [eq.subs(self.indep_var, cp) for cp in critical_points]

        # make list of tuple pairs of critical points and their respective y values
        critical_points = [
            (cp, y) for cp, y in zip(critical_points, y_values) if y.is_real
        ]

        logger.debug(f"Critical points: {critical_points}")

        return critical_points

    @classmethod
    def from_calibration_model(cls, calibration_model: CalibrationModel):
        assert calibration_model.signal_law is not None, (
            "Calibration model has no signal law."
        )
        assert calibration_model.molecule_id is not None, (
            "Calibration model has no molecule symbol."
        )

        return cls(
            equation=calibration_model.signal_law,
            indep_var=calibration_model.molecule_id,
            params=calibration_model.parameters,
        )

    def _get_model_callable(self) -> Callable[..., float]:
        sp_expression = sp.sympify(self.equation)
        variables = [self.indep_var] + self.dep_vars

        return sp.lambdify(variables, sp_expression)

    def _prepare_model(self) -> LMFitModel:
        callable_ = self.model_callable

        model = LMFitModel(callable_, independent_vars=[self.indep_var])

        return model

    def _get_param_dict(self, indep_var_values: np.ndarray):
        values_dict = self.lmfit_params.valuesdict()
        values_dict[self.indep_var] = indep_var_values

        return values_dict

    def _prepare_params(self):
        lm_params = Parameters()
        for param in self.params:
            lm_params.add(
                param.symbol,
                value=param.init_value,
                min=param.lower_bound if param.lower_bound is not None else -np.inf,
                max=param.upper_bound if param.upper_bound is not None else np.inf,
            )

        return lm_params

    def _get_root_eq(self):
        eq = self.equation + " - " + self.signal_var
        variables = [self.indep_var] + self.dep_vars + [self.signal_var]
        return sp.lambdify(variables, eq)

    def _update_result_params(
        self,
    ) -> None:
        """
        Extract parameters from a lmfit result.
        and update the parameters list.
        """

        for name, lmf_param in self.lmfit_params.items():
            for param in self.params:
                if param.symbol == name:
                    param.value = lmf_param.value
                    param.stderr = lmf_param.stderr

    def extract_fit_statistics(self, lmfit_result: ModelResult) -> FitStatistics:
        """
        Extract fit statistics from a lmfit result.
        """

        assert self.lmfit_model is not None, "Model was not fitted."

        if lmfit_result.success:
            rmsd = calculate_rmsd(lmfit_result.residual)

            return FitStatistics(
                aic=lmfit_result.aic,  # type: ignore
                bic=lmfit_result.bic,  # type: ignore
                r2=lmfit_result.rsquared,
                rmsd=rmsd,
            )

        raise ValueError("Model did not converge.")
