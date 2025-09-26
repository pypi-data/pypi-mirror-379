"""
Ordinary Least Squares (OLS) regression implementation.
"""

import warnings

import numpy as np

from ._rust_imports import calculate_ols_regression
from .base import BaseRegressor, OlsRegressionParams


class OlsRegressor(BaseRegressor[OlsRegressionParams]):
    """Class for calculating Ordinary Least Squares (OLS) regression.

    This class implements the standard least squares method, which minimizes
    the errors in the y-direction.

    Parameters
    ----------
    x : np.ndarray
        Input data for the independent variable (x-axis).
    y : np.ndarray
        Input data for the dependent variable (y-axis).
    """

    def __init__(self, x: np.ndarray, y: np.ndarray):
        """Initialize the OlsRegressor and fit the model.

        Parameters
        ----------
        x : np.ndarray
            Input data for the independent variable (x-axis).
        y : np.ndarray
            Input data for the dependent variable (y-axis).
        """
        self._p_value: float
        self._stderr: float
        self._intercept_stderr: float
        super().__init__(x, y)

    def _fit(self) -> None:
        """Perform OLS regression."""
        # Call the Rust implementation
        (
            _,
            self._slope,
            self._intercept,
            self._r_value,
            self._p_value,
            self._stderr,
            self._intercept_stderr,
        ) = calculate_ols_regression(self.x, self.y)

    def slope(self) -> float:
        """Return the slope of the regression line

        Returns
        -------
        float
            The slope of the regression line
        """
        return self._slope

    def intercept(self) -> float:
        """Return the intercept of the regression line

        Returns
        -------
        float
            The intercept of the regression line
        """
        return self._intercept

    def r_value(self) -> float:
        """Return the correlation coefficient

        Returns
        -------
        float
            The correlation coefficient
        """
        return self._r_value

    def p_value(self) -> float:
        """Return the p-value

        Returns
        -------
        float
            The p-value
        """
        return self._p_value

    def stderr(self) -> float:
        """Return the standard error of the slope

        Returns
        -------
        float
            The standard error of the slope
        """
        return self._stderr

    def intercept_stderr(self) -> float:
        """Return the standard error of the intercept

        Returns
        -------
        float
            The standard error of the intercept
        """
        return self._intercept_stderr

    def get_params(self) -> OlsRegressionParams:
        """Retrieve regression parameters.

        .. deprecated:: 0.2.0
            Use property methods instead: slope(), intercept(), r_value(),
            p_value(), stderr(), intercept_stderr()
            This method will be removed in v1.0.0.

        Returns
        -------
        OlsRegressionParams
            A data class containing all regression parameters, including
            slope, intercept, r_value, p_value, stderr, and intercept_stderr.
        """
        warnings.warn(
            "get_params() is deprecated and will be removed in v1.0.0. "
            "Use property methods instead: slope(), intercept(), r_value(), "
            "p_value(), stderr(), intercept_stderr()",
            DeprecationWarning,
            stacklevel=2,
        )
        return OlsRegressionParams(
            slope=self._slope,
            intercept=self._intercept,
            r_value=self._r_value,
            p_value=self._p_value,
            stderr=self._stderr,
            intercept_stderr=self._intercept_stderr,
        )
