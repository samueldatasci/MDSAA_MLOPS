import logging
from typing import Any, Dict, Tuple
import numpy as np
import pandas as pd
import json
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder , LabelEncoder
import shap 
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
import sklearn



def feature_selection(data: pd.DataFrame, X_train: pd.DataFrame , y_train: pd.DataFrame,  parameters: Dict[str, Any]):
    if parameters["feature_selection"] == "rfe":
        model = RandomForestClassifier(n_estimators=parameters["n_estimators"], max_depth=parameters["max_depth"], max_features=parameters["max_features"])
        model.fit(X_train, y_train)
        rfe = RFE(model)
        rfe = rfe.fit(X_train, y_train)
        f = rfe.get_support(1) #the most important features
        keep = X_train.columns[f].tolist()

    log = logging.getLogger(__name__)
    log.info(f"Number of best columns is: {len(keep)}")

    return keep

