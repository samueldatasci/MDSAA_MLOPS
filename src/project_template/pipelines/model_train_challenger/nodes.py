import logging
from typing import Any, Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder , LabelEncoder
import shap 
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
#
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import sklearn
import mlflow



def model_train_challenger(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.DataFrame, y_test: pd.DataFrame, parameters: Dict[str, Any], best_cols):
    #best_cols = ['age', 'balance_euros', 'last_contact_day', 'last_contact_duration', 'campaign', 'pdays']
    #print("best_cols:", best_cols)

    with mlflow.start_run(run_name="Challenger_train", description="Executing the Challenger train pipeline", nested=True) as run:

        if  parameters["with_feature_selection"] == False:
            X_train_copy = X_train.copy()
            X_test_copy = X_test.copy()
            best_cols = list(X_train.columns)
        else:
            X_train_copy = X_train[best_cols].copy()
            X_test_copy = X_test[best_cols].copy()

        mlflow.set_tag("mlflow.runName", parameters["run_name_challenger"])
        mlflow.autolog(log_model_signatures=True, log_input_examples=True)

        #LOGISTIC REGRESSION
        model_lr = LogisticRegression(solver='liblinear')
        model_lr.fit(X_train_copy, y_train)
        #explainer = shap.KernelExplainer(model_lr.predict_proba, X_test_copy) #importance of different features in making predictions

        #shap_values = explainer.shap_values(X_test_copy) #shap values for X_test
        #shap.summary_plot(shap_values[1], X_test_copy,show=False)
        
        predict = model_lr.predict(X_test_copy)
        predict_labels = np.rint(predict)   
        accuracy = sklearn.metrics.accuracy_score(y_test, predict_labels)
        

        report = classification_report(y_test, predict, output_dict=True)
        reportdf = pd.DataFrame(report).transpose()


        

        log_lr = logging.getLogger(__name__)
        log_lr.info(f"#Best columns: {len(best_cols)}")
        log_lr.info("Model accuracy on test: %0.2f%%", accuracy * 100)
        
        
        mlflow.log_metric("accuracy", accuracy)

        mlflow.end_run()

        
    return model_lr, plt, reportdf

