"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

import logging
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd
import great_expectations as gx

def unit_tests(
    data: pd.DataFrame,
): 

    pd_df_ge = gx.from_pandas(data)


    assert pd_df_ge.expect_table_column_count_to_equal(17).success == True, "Data validation error!\nThe input file must have 17 columns."

    expected_columns = ['Age', 'Job', 'Marital Status', 'Education', 'Credit', 'Balance (euros)', 'Housing Loan', 'Personal Loan', 'Contact', 'Last Contact Day', 'Last Contact Month', 'Last Contact Duration', 'Campaign', 'Pdays', 'Previous', 'Poutcome', 'Subscription']
    assert pd_df_ge.expect_table_columns_to_match_set(expected_columns).success == True, "Data validation error!\nColumn names differ from what was expected.\nExpected:{}".format(expected_columns)

    #assert pd_df_ge.expect_column_to_exist("Age").success == True, "Data validation error!\nColumn Age must exist in the dataset"
    #assert pd_df_ge.expect_column_values_to_be_of_type("Marital Status", "str").success == True, "Data validation error!\nMarital Status must be a string."

    dic_datatype = {}
    dic_datatype["Age"] = "int64"
    dic_datatype["Job"] = "object"
    dic_datatype["Marital Status"] = "object"
    dic_datatype["Education"] = "object"
    dic_datatype["Credit"] = "object"
    dic_datatype["Balance (euros)"] = "int64"
    dic_datatype["Housing Loan"] = "object"
    dic_datatype["Personal Loan"] = "object"
    dic_datatype["Contact"] = "object"
    dic_datatype["Last Contact Day"] = "int64"
    dic_datatype["Last Contact Month"] = "object"
    dic_datatype["Last Contact Duration"] = "int64"
    dic_datatype["Campaign"] = "int64"
    dic_datatype["Pdays"] = "int64"
    dic_datatype["Previous"] = "int64"
    dic_datatype["Poutcome"] = "object"
    dic_datatype["Subscription"] = "int64"

    for colname in data.columns:
        assert pd_df_ge.expect_column_values_to_be_of_type(colname, dic_datatype[colname]).success == True, "Data validation error!\n{} must be of type {} but is of type {}.".format(colname, dic_datatype[colname], data[colname].dtype)


    valuelist = ["married", "single", "divorced"]
    assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column="Marital Status", value_set=valuelist).success == True, "Data validation error!\nMarital Status has a value that is not expected {}.".format(valuelist)
    valuelist = ["unknown", "primary", "secondary", "tertiary"]
    assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column="Education", value_set=valuelist).success == True, "Data validation error!\nEducation has a value that is not expected {}.".format(valuelist)
    valuelist = ["yes", "no"]
    assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column="Credit", value_set=valuelist).success == True, "Data validation error!\Credit has a value that is not expected {}.".format(valuelist)
    assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column="Housing Loan", value_set=valuelist).success == True, "Data validation error!\Housing Loan has a value that is not expected {}.".format(valuelist)
    assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column="Personal Loan", value_set=valuelist).success == True, "Data validation error!\Personal Loan has a value that is not expected {}.".format(valuelist)
    valuelist = ["unknown", "cellular", "telephone"]
    assert pd_df_ge.expect_column_distinct_values_to_be_in_set(column="Contact", value_set=valuelist).success == True, "Data validation error!\Contact has a value that is not expected {}.".format(valuelist)

    
    assert pd_df_ge.expect_column_values_to_be_between(column="Last Contact Day", min_value=1, max_value=31)
    #valuelist = list(range(1, 32))
    #assert pd_df_ge.expect_column_values_to_be_in_set(column="Last Contact Day", value_set=valuelist)

    log = logging.getLogger(__name__)
    log.info("Data passed on the unit data tests")

    return 0


#data_path = f"C:/Users/Samuel Santos/Documents/MDSAA-DS/MLOPS/GitHub/MLOPS/data/01_raw/Bank Marketing.csv"
#bank_df = pd.read_csv(data_path)
#unit_tests(bank_df)
