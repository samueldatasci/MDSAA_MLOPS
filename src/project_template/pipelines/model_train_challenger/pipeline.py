
"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import  model_train_challenger


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [

            node(
                func= model_train_challenger,
                inputs=["X_train_data","X_test_data","y_train_data","y_test_data","parameters","best_columns"],
                outputs= ["challenger_model","challenger_output_plot", "challenger_classification_report"],
                name="train",
            ),
        ]
    )
