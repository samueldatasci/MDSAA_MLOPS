
"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import  data_drift
from project_template.pipelines.data_preprocessing.nodes import clean_data, feature_engineer

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_data,
                inputs="bank_daily_data",
                outputs=["bank_daily_data_cleaned","raw_describe_daily","cleaned_describe_daily"],
                name="clean",
            ),

            node(
                func= feature_engineer,
                inputs="bank_daily_data_cleaned",
                outputs= "bank_daily_data_engineered",
                name="engineering",
            ),

            node(
                func= data_drift,
                inputs=["bank_daily_data_engineered","bank_daily_data_engineered",],
                outputs= "drift_result",
                name="drift_analysis",
            ),
        ]
    )
