#"""Project pipelines."""
#from typing import Dict

#from kedro.framework.project import find_pipelines
#from kedro.pipeline import Pipeline


#def register_pipelines() -> Dict[str, Pipeline]:
#    """Register the project's pipelines.

#    Returns:
#        A mapping from pipeline names to ``Pipeline`` objects.
#    """
#    pipelines = find_pipelines()
#    pipelines["__default__"] = sum(pipelines.values())
#    return pipelines


"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline, pipeline

from project_template.pipelines import (
    data_unit_tests as unit_tests,
    data_preprocessing as preprocessing,
    data_split as split_data,
    #model_train as train,
    model_train_challenger as train_challenger,
    model_train_champion as train_champion,
    feature_selection as best_features,
    model_predict as predict,
    model_predict_champion as predict_champion,
    model_predict_challenger as predict_challenger,
    # data_drift as drift_test,
)


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    unit_tests_stage = unit_tests.create_pipeline()
    preprocessing_stage = preprocessing.create_pipeline()
    split_data_stage = split_data.create_pipeline()
    #train_stage = train.create_pipeline()
    train_challenger_stage = train_challenger.create_pipeline()
    train_champion_stage = train_champion.create_pipeline()
    
    feature_selection_stage = best_features.create_pipeline()
    predict_stage = predict.create_pipeline()
    predict_champion_stage = predict_champion.create_pipeline()
    predict_challenger_stage = predict_challenger.create_pipeline()

    #drift_test_stage = drift_test.create_pipeline()


    return {
        "testing":unit_tests_stage,
        "preprocessing": preprocessing_stage,
        "split_data": split_data_stage,
        #"train": train_stage,
        "feature_selection": feature_selection_stage,
        "predict": predict_stage,
        #"drift_test" : drift_test_stage, 
        #"__default__": preprocessing_stage + split_data_stage + train_stage,



        "CHAMPION": unit_tests_stage + preprocessing_stage + split_data_stage + feature_selection_stage + train_champion_stage,
        "CHAMPION2": unit_tests_stage + split_data_stage + feature_selection_stage + train_champion_stage,

        "CHALLENGER": unit_tests_stage + preprocessing_stage + split_data_stage + feature_selection_stage + train_challenger_stage,
        "CHALLENGER2": preprocessing_stage + split_data_stage + feature_selection_stage + train_challenger_stage,
        "CHALLENGER3": preprocessing_stage + split_data_stage + train_challenger_stage,


        "PREDCHAMP": predict_champion_stage,
        "PREDCHALL": predict_challenger_stage,


        "__default__": preprocessing_stage
    }

