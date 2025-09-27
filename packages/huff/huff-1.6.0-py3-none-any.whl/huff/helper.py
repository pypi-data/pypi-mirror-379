#-----------------------------------------------------------------------
# Name:        helper (huff package)
# Purpose:     Huff Model helper functions and definitions
# Author:      Thomas Wieland 
#              ORCID: 0000-0001-5168-9846
#              mail: geowieland@googlemail.com              
# Version:     1.0.0
# Last update: 2025-09-26 12:48
# Copyright (c) 2025 Thomas Wieland
#-----------------------------------------------------------------------

import pandas as pd
import numpy as np

PERMITTED_LOCATION_TYPES = [
    "origins",
    "destinations"
]

# Default column names:
DEFAULT_COLNAME_ATTRAC = "A_j"
DEFAULT_COLNAME_TC = "t_ij"
DEFAULT_COLNAME_UTILITY = "U_ij"
DEFAULT_COLNAME_UTILITY_SUM = "U_i"
DEFAULT_COLNAME_MARKETSIZE = "C_i"
DEFAULT_COLNAME_PROBABILITY = "p_ij"
DEFAULT_COLNAME_FLOWS = "E_ij"
DEFAULT_COLNAME_CUSTOMER_ORIGINS = "i"
DEFAULT_COLNAME_SUPPLY_LOCATIONS = "j"
DEFAULT_COLNAME_INTERACTION = "ij"
DEFAULT_COLNAME_TOTAL_MARKETAREA = "T_j"

# Default column name suffixes:
DEFAULT_LCT_SUFFIX = "__LCT"
DEFAULT_WEIGHTED_SUFFIX = "_weighted"
DEFAULT_OBSERVED_SUFFIX = "_emp"

DEFAULT_COLNAME_ATTRAC_WEIGHTED = f"{DEFAULT_COLNAME_ATTRAC}{DEFAULT_WEIGHTED_SUFFIX}"
DEFAULT_COLNAME_TC_WEIGHTED = f"{DEFAULT_COLNAME_TC}{DEFAULT_WEIGHTED_SUFFIX}"

DEFAULT_COLNAME_PROBABILITY_OBSERVED = f"{DEFAULT_COLNAME_PROBABILITY}{DEFAULT_OBSERVED_SUFFIX}"
DEFAULT_COLNAME_FLOWS_OBSERVED = f"{DEFAULT_COLNAME_FLOWS}{DEFAULT_OBSERVED_SUFFIX}"
DEFAULT_COLNAME_TOTAL_MARKETAREA_OBSERVED = f"{DEFAULT_COLNAME_TOTAL_MARKETAREA}{DEFAULT_OBSERVED_SUFFIX}"

# Default descriptions:
DEFAULT_NAME_ATTRAC = "Attraction"
DEFAULT_NAME_TC = "Transport costs"


PERMITTED_WEIGHTING_FUNCTIONS = {
    "power": {
        "description": "Power function",
        "function": "a*(values**b)",
        "no_params": 1
        },
    "exponential": {
        "description": "Exponential function",
        "function": "a*np.exp(b*values)",
        "no_params": 1
        },
    "logistic": {
        "description": "Logistic function",
        "function": "1+np.exp(b+c*values)",
        "no_params": 2
        },
    "linear": {
        "description": "Linear function",
        "function": "a+(b*values)",
        "no_params": 1
        }
    }
PERMITTED_WEIGHTING_FUNCTIONS_LIST = list(PERMITTED_WEIGHTING_FUNCTIONS.keys())

MCI_TRANSFORMATIONS = {
    "LCT": "Log-centering transformation",
    "ILCT": "Inverse log-centering transformation"
}
MCI_TRANSFORMATIONS_LIST = list(MCI_TRANSFORMATIONS.keys())
DEFAULT_MCI_TRANSFORMATION = MCI_TRANSFORMATIONS_LIST[0]

def weighting(
    values: pd.Series,
    func: str,
    b: float,
    c: float = None,
    a: float = 1.0
    ):
    
    if func not in PERMITTED_WEIGHTING_FUNCTIONS_LIST:
        raise ValueError (f"Parameter 'func' must be one of {', '.join(PERMITTED_WEIGHTING_FUNCTIONS_LIST)}")
    
    if not check_numeric_series(values):
        raise TypeError("Vector given by parameter 'series' is not numeric")    
    
    result = None
    
    calc_formula = PERMITTED_WEIGHTING_FUNCTIONS[func]["function"]
    
    calc_dict = {"a": a, "b": b, "values": values, "np": np}
    
    if "c" in calc_formula:
        if c is None:
            raise ValueError("Parameter 'c' must be provided for this function")
        calc_dict["c"] = c
        
    result = eval(calc_formula, {}, calc_dict)
    
    return result


def log_centering_transformation(
    df: pd.DataFrame,
    ref_col: str,
    cols: list,
    suffix: str = DEFAULT_LCT_SUFFIX
    ):
   
    check_vars(
        df = df,
        cols = cols
        )
    
    if ref_col not in df.columns:
        raise KeyError(f"Error in log-centering transformation: Column '{ref_col}' not in dataframe.")

    def lct (x):

        x_geom = np.exp(np.log(x).mean())
        x_lct = np.log(x/x_geom)

        return x_lct
    
    for var in cols:
        
        unique_values = df[var].unique()
        if set(unique_values).issubset({0, 1}):
            df[var+suffix] = df[var]
            print (f"Column {var} is a dummy variable and requires/allows no log-centering transformation")
            continue

        if (df[var] <= 0).any():
            df[var+suffix] = float("nan")
            print (f"Column {var} contains values <= 0. No log-centering transformation possible.")
            continue

        var_t = df.groupby(ref_col)[var].apply(lct)
        var_t = var_t.reset_index()
        df[var+suffix] = var_t[var]

    return df


def check_vars(
    df: pd.DataFrame,
    cols: list,
    check_numeric: bool = True,
    check_zero: bool = True
    ):

    for col in cols:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not in dataframe.")
    
    if check_numeric:
        for col in cols:
            if not check_numeric_series(df[col]):
                raise TypeError(f"Column '{col}' is not numeric. All stated columns must be numeric.")
    
    if check_zero:
        for col in cols:
            if (df[col] <= 0).any():
                raise ValueError(f"Column '{col}' includes values <= 0. All values must be numeric and positive.")
            
def check_numeric_series(
    values: pd.Series
    ):
    
    if not pd.api.types.is_numeric_dtype(values):
        return False
    else:
        return True