"""
This module contains an example test.

Tests should be placed in ``src/tests``, in modules that mirror your
project's structure, and in files named test_*.py. They are simply functions
named ``test_*`` which test a unit of logic.

To run the tests, run ``kedro test`` from the project root directory.
"""

from pathlib import Path

import pytest
import pandas as pd
import numpy as np

from kedro.framework.project import settings
from kedro.config import ConfigLoader
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager
import sys
import os

from project_template.pipelines.data_preprocessing.nodes import clean_data, feature_engineer

def test_clean_date_type():
    df = pd.read_csv("data/01_daily_data/df_sample.csv")
    df_transformed, describe_to_dict, describe_to_dict_verified = clean_data(df)
    isinstance(describe_to_dict, dict)

@pytest.mark.slow
def test_clean_date_null():
    df = pd.read_csv("data/01_daily_data/df_sample.csv")
    df_transformed, describe_to_dict, describe_to_dict_verified = clean_data(df)
    assert [col for col in df_transformed.columns if df_transformed[col].isnull().any()] == []

def test_feature_engineering_month():
    df = pd.read_csv("data/01_daily_data/df_sample.csv")
    df_final = feature_engineer(df)
    assert(len(df["month"].unique().tolist()) <= 12)


def test_sam():
    filename = "data/01_raw/Bank Marketing.csv"
    df = pd.read_csv(filename)
    print("****************************************------------*********************************")
    assert( "Credit" in df.columns )
    # , "************************************* Credit column does not exist in " + filename
