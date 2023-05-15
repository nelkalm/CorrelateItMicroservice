import numpy as np
import streamlit as st
from scipy.stats import t


################################################################################################
#
# CODE FOR FUNCTIONS TO CALCULATE STATISTICS
#
#
################################################################################################

@st.cache_data
def mean(data):
    """
    Calculates the mean of a set of data.
    """
    return sum(data) / len(data)


@st.cache_data
def median(data):
    """
    Calculates the median of a set of data.
    """
    data.sort()
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2-1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median


@st.cache_data
def mode(data):
    """
    Calculates the mode of a set of data.
    """
    from collections import Counter
    freq_dict = Counter(data)
    modes = [k for k, v in freq_dict.items(
    ) if v == max(list(freq_dict.values()))]
    if len(modes) == len(data):
        return None
    else:
        return modes


@st.cache_data
def variance(data):
    """
    Calculates the variance of a set of data.
    """
    n = len(data)
    if n == 0:
        return None
    mean_value = mean(data)
    variance = sum((x - mean_value) ** 2 for x in data) / n
    return variance


@st.cache_data
def standard_deviation(data):
    """
    Calculates the standard deviation of a set of data.
    """
    return variance(data) ** 0.5


@st.cache_data
def pearson_correlation(x, y):
    """
    Calculates the Pearson correlation coefficient between two variables.

    Parameters:
        x (numpy array): First variable.
        y (numpy array): Second variable.

    Returns:
        float: Pearson correlation coefficient.
    """
    # Compute the mean of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Compute the numerator and denominator of the correlation coefficient
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sqrt(np.sum((x - mean_x) ** 2)
                          * np.sum((y - mean_y) ** 2))

    # Compute the correlation coefficient
    corr_coef = numerator / denominator

    return corr_coef


@st.cache_data
def pearson_pval(r, n):
    """
    Calculate the two-tailed p-value for a Pearson correlation coefficient.

    Args:
        r (float): Pearson correlation coefficient
        n (int): Sample size

    Returns:
        float: Two-tailed p-value
    """
    df = n - 2  # degrees of freedom
    t_stat = r * ((n - 2) / ((1 - r**2)**0.5))  # t-statistic
    pval = 2 * t.sf(abs(t_stat), df)  # two-tailed p-value
    return pval


@st.cache_data
def stat_conclusion(p, r):
    """
    Returns a tuple containing the statistical significance and the direction of the relationship based on the given
    p-value and correlation coefficient.

    Args:
        p (float): The p-value for the correlation test.
        r (float): The correlation coefficient.

    Returns:
        tuple: A tuple containing the statistical significance (either 'significant' or 'non-significant') and the 
               direction of the relationship (either 'positive', 'negative', or an empty string if the correlation is
               zero).

    Example:
        >>> p_val, corr_coef = 0.023, 0.78
        >>> significance, direction = stat_conclusion(p_val, corr_coef)
        >>> print(f"The correlation is {significance} and {direction}.")
        The correlation is significant and positive.
    """

    significance = ""
    relationship = ""
    if p > 0.05:
        significance = "non-significant (p > 0.05)"
    elif p <= 0.05:
        significance = "significant (p <= 0.05)"

    if r > 0:
        relationship = "positive (r > 0)"
    elif r < 0:
        relationship = "negative (r < 0)"

    return significance, relationship


@st.cache_data
def is_numeric_array(arr):
    """
    Check if an array only contains numbers

    Parameters:
        arr (array-like): The input array to be checked

    Returns:
        bool: True if the array only contains numbers, False otherwise
    """
    for elem in arr:
        if not isinstance(elem, (int, float)):
            return False
    return True


@st.cache_data
def conclude_stat(significance: str, relationship: str, data_label_1: str, data_label_2: str) -> str:
    """
    Returns a string summarizing the statistical conclusion.

    Parameters:
    -----------
    - significance (str): The significance level of the statistical test (either "significant" or "non-significant").
    - relationship (str): The direction of the relationship between the two variables (either "positive" or "negative").
    - data_label_1 (str): The label for the first variable.
    - data_label_2 (str): The label for the second variable.

    Returns:
    --------
    - str: A string summarizing the statistical conclusion.
    """
    return f"There is a {significance} {relationship} relationship between {data_label_1} and {data_label_2}."
