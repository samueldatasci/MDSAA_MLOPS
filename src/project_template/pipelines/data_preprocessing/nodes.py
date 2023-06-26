"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

import logging
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd
from .utils import *


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder , LabelEncoder
import shap 
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import sklearn
import mlflow

def clean_data(
    data: pd.DataFrame,
) -> Tuple[pd.DataFrame, Dict, Dict]:
    """Does dome data cleaning.
    Args:
        data: Data containing features and target.
    Returns:
        data: Cleaned data
    """
    #remove some outliers
    df_transformed = data.copy()

    describe_to_dict = df_transformed.describe().to_dict()


    # Apply the clean_column_name function to each column name using rename()
    df_transformed = df_transformed.rename(columns=grp_clean_column_name)
    
    df_transformed = grp_feature_engineering(df_transformed)


    describe_to_dict_verified = df_transformed.describe().to_dict()

    return df_transformed, describe_to_dict, describe_to_dict_verified 





def feature_engineer( data: pd.DataFrame) -> pd.DataFrame:
    

    # Everything is in the clean_data


    return data


