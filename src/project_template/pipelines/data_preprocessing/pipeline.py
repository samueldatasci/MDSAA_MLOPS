
"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import  clean_data, feature_engineer

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_data,
                inputs="bank_raw_data",
                outputs=["bank_cleaned_data","raw_describe","cleaned_describe"],
                name="clean",
            ),

            node(
                func= feature_engineer,
                inputs="bank_cleaned_data",
                outputs= "bank_data_engineered",
                name="engineering",
            ),

        ]
    )
