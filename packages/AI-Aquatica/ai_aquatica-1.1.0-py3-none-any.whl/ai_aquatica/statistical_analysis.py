import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.formula.api import ols
import statsmodels.api as sm

# Podstawowe Statystyki

def calculate_basic_statistics(data):
    """
    Calculate basic statistics for the provided data.

    Parameters:
    data (pd.DataFrame): DataFrame containing the data.

    Returns:
    pd.DataFrame: DataFrame with basic statistics.
    """
    try:
        statistics = data.describe().T
        statistics['range'] = statistics['max'] - statistics['min']
        return statistics[['mean', '50%', 'std', 'range']]
    except Exception as e:
        print(f"Error calculating basic statistics: {e}")
        return pd.DataFrame()

def plot_distribution(data, column):
    """
    Plot the distribution of a specific column.

    Parameters:
    data (pd.DataFrame): DataFrame containing the data.
    column (str): Column name to plot.

    Returns:
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error plotting distribution: {e}")

def plot_boxplot(data, column):
    """
    Plot the boxplot of a specific column.

    Parameters:
    data (pd.DataFrame): DataFrame containing the data.
    column (str): Column name to plot.

    Returns:
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=data[column])
        plt.title(f'Boxplot of {column}')
        plt.xlabel(column)
        plt.show()
    except Exception as e:
        print(f"Error plotting boxplot: {e}")

# Analizy Zaawansowane

def calculate_correlation_matrix(data):
    """
    Calculate the correlation matrix for the provided data.

    Parameters:
    data (pd.DataFrame): DataFrame containing the data.

    Returns:
    pd.DataFrame: Correlation matrix.
    """
    try:
        correlation_matrix = data.corr()
        return correlation_matrix
    except Exception as e:
        print(f"Error calculating correlation matrix: {e}")
        return pd.DataFrame()

def perform_anova(data, formula):
    """
    Perform ANOVA (Analysis of Variance) on the provided data.

    Parameters:
    data (pd.DataFrame): DataFrame containing the data.
    formula (str): Formula for the ANOVA test.

    Returns:
    pd.DataFrame: ANOVA table.
    """
    try:
        model = ols(formula, data=data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        return anova_table
    except Exception as e:
        print(f"Error performing ANOVA: {e}")
        return pd.DataFrame()

def decompose_time_series(data, column, model='additive', freq=None):
    """
    Decompose the time series data to analyze trends and seasonality.

    Parameters:
    data (pd.DataFrame): DataFrame containing the time series data.
    column (str): Column name of the time series.
    model (str): Type of decomposition ('additive' or 'multiplicative').
    freq (int): Frequency of the time series.

    Returns:
    seasonal_decompose: Decomposition object.
    """
    try:
        series = data[column].dropna()
        n_obs = len(series)

        if n_obs < 2:
            raise ValueError(
                f"Insufficient data points ({n_obs}) in column '{column}' for seasonal decomposition."
            )

        period = freq

        def _fallback_period(base_period):
            candidate = base_period if base_period is not None else series.shape[0] // 2
            candidate = min(candidate, series.shape[0] // 2)
            candidate = max(candidate, 2)
            if candidate * 2 > series.shape[0]:
                return None
            return candidate

        if period is None or period < 2 or n_obs < 2 * period:
            fallback = _fallback_period(period)
            if fallback is None:
                raise ValueError(
                    "Unable to determine a suitable seasonal period: "
                    f"received freq={freq}, but only {n_obs} non-NaN observations are available."
                )
            if period is not None and fallback != period:
                warnings.warn(
                    "Provided period is too large for the available data. "
                    f"Falling back to period={fallback}.",
                    UserWarning,
                )
            period = fallback

        decomposition = seasonal_decompose(series, model=model, period=period)
        decomposition.plot()
        plt.show()
        return decomposition
    except Exception as e:
        print(f"Error decomposing time series: {e}")
        raise
