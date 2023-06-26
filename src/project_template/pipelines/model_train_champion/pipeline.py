
"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import  model_train_champion


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [

            node(
                func= model_train_champion,
                inputs=["X_train_data","X_test_data","y_train_data","y_test_data","parameters","best_columns"],
                #outputs= ["test_model","output_plot"],
                outputs= ["champion_model","champion_output_plot", "champion_classification_report", "champion_feature_importance"],
                name="train",
            ),
        ]
    )

