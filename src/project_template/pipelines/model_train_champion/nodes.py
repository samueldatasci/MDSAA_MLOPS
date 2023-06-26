import logging
from typing import Any, Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder , LabelEncoder
import shap 
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, f1_score
#
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import sklearn
import mlflow

#from sklearn.datasets import make_classification



def model_train_champion(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.DataFrame, y_test: pd.DataFrame, parameters: Dict[str, Any], best_cols):

# executes the run
    with mlflow.start_run(run_name="Champion_train", description="Executing the Champion train pipeline", nested=True) as run:

        if  parameters["with_feature_selection"] == False:
            X_train_copy = X_train.copy()
            X_test_copy = X_test.copy()
            best_cols = list(X_train.columns)
        else:
            X_train_copy = X_train[best_cols].copy()
            X_test_copy = X_test[best_cols].copy()

        mlflow.set_tag("mlflow.runName", parameters["run_name_champion"])
        mlflow.autolog(log_model_signatures=True, log_input_examples=True)


        model_rf = hyper_tunning( X_train_copy, y_train)


        importances = model_rf.feature_importances_

        # Create a dataframe with feature importances
        feature_importances_df = pd.DataFrame({'Feature': X_train_copy.columns, 'Importance': importances})

        # Sort the dataframe by feature importance in descending order
        feature_importances_df = feature_importances_df.sort_values('Importance', ascending=False)


        #RANDOM FOREST
        #model_rf = RandomForestClassifier(n_estimators=parameters["n_estimators"], max_depth=parameters["max_depth"], max_features=parameters["max_features"])
        #model_rf.fit(X_train_copy, y_train)
        explainer = shap.TreeExplainer(model_rf)
        

        shap_values = explainer.shap_values(X_test_copy) #shap values for X_test - # was: X_test, changed to X_test_copy
        shap.summary_plot(shap_values[1], X_test_copy,show=False) # ditto
        

        predict = model_rf.predict(X_test_copy)

        predict_labels = np.rint(predict)
        
        accuracy = sklearn.metrics.accuracy_score(y_test, predict_labels)

        report = classification_report(y_test, predict, output_dict=True)
        reportdf = pd.DataFrame(report).transpose()

 
        
        log_rf = logging.getLogger(__name__)
        log_rf.info(f"#Best columns: {len(best_cols)}")
        log_rf.info("Model accuracy on test set: %0.2f%%", accuracy * 100)

        mlflow.log_metric("accuracy", accuracy)


        mlflow.end_run()

    return model_rf,plt, reportdf, feature_importances_df




def hyper_tunning(X_train, y_train):
    X = X_train.copy()
    y = y_train.copy()
    #X = df_engineered[best_cols].copy()
    #y = df_engineered[parameters["target"]]

#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


    # Define the parameter grid for grid search
    param_grid = {
        'n_estimators': [20, 50],  # Number of trees in the forest
        'max_depth': [5, 10],  # Maximum depth of the tree
        'min_samples_split': [2, 5],  # Minimum number of samples required to split an internal node
        'min_samples_leaf': [2, 4]  # Minimum number of samples required to be at a leaf node
    }


    rf = RandomForestClassifier()

    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=2, verbose=2)
    grid_search.fit(X, y)

    print("Best hyperparameters: ", grid_search.best_params_)

    best_model = grid_search.best_estimator_

    #y_pred = best_model.predict(X_test)

    #f1 = f1_score(y_test, y_pred)

    #print("F1 score on test set: ", f1)
    
    return(best_model)
