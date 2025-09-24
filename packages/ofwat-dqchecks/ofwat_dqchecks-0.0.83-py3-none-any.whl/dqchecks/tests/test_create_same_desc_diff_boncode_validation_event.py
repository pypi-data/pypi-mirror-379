"""
Test the create_same_desc_diff_boncode_validation_event function
"""
import pandas as pd
import pytest

from dqchecks.panacea import create_same_desc_diff_boncode_validation_event

def test_returns_empty_df_when_no_duplicates():
    """
    Test that the function returns an empty DataFrame when
    no Measure_Desc is associated with multiple Measure_Cd.
    """
    df = pd.DataFrame({
        'Measure_Cd': ['A1', 'B1', 'C1'],
        'Measure_Desc': ['desc1', 'desc2', 'desc3'],
        'Sheet_Cd': ['sheet1', 'sheet2', 'sheet3']
    })
    metadata = {
        'Batch_Id': 'batch1',
        'Submission_Period_Cd': '202301',
        'Process_Cd': 'proc1',
        'Template_Version': 'v1',
        'Organisation_Cd': 'org1'
    }

    result = create_same_desc_diff_boncode_validation_event(df, metadata)
    assert isinstance(result, pd.DataFrame)
    assert result.empty  # Should be empty DataFrame when no duplicates

def test_returns_validation_event_when_duplicates_found():
    """
    Test that the function returns a validation event DataFrame
    when a Measure_Desc has multiple different Measure_Cd.
    """
    df = pd.DataFrame({
        'Measure_Cd': ['A1', 'A2', 'B1'],
        'Measure_Desc': ['desc1', 'desc1', 'desc2'],
        'Sheet_Cd': ['sheet1', 'sheet2', 'sheet3'],
        "Cell_Cd": ["B1", "B2", "B4"],
    })
    metadata = {
        'Batch_Id': 'batch1',
        'Submission_Period_Cd': '202301',
        'Process_Cd': 'proc1',
        'Template_Version': 'v1',
        'Organisation_Cd': 'org1',
        'Validation_Processing_Stage': 'stage1'
    }

    result = create_same_desc_diff_boncode_validation_event(df, metadata)

    # Basic structure checks
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'Error_Desc' in result.columns
    assert 'Event_Id' in result.columns
    assert result['Event_Id'].is_unique

    # Expect two rows: one for A1, one for A2 (both under desc1)
    assert len(result) == 2

    # Check that each Error_Desc contains the correct format and data
    for _, row in result.iterrows():
        error_desc = row['Error_Desc']
        measure_cd = row['Error_Desc'].split("Current Measure_Cd: '")[1].split("'")[0]

        # It should reference 'desc1' (the conflicting Measure_Desc)
        assert "Measure_Desc 'desc1'" in error_desc

        # It should mention all sheet codes involved
        assert 'sheet1' in error_desc
        assert 'sheet2' in error_desc

        # It should reference the current Measure_Cd
        assert measure_cd in ['A1', 'A2']

def test_returns_empty_df_on_empty_input():
    """
    Test that an empty DataFrame input returns an empty validation event DataFrame.
    """
    df = pd.DataFrame(columns=['Measure_Cd', 'Measure_Desc', 'Sheet_Cd'])
    metadata = {
        'Batch_Id': 'batch1',
        'Submission_Period_Cd': '202301',
        'Process_Cd': 'proc1',
        'Template_Version': 'v1',
        'Organisation_Cd': 'org1'
    }

    result = create_same_desc_diff_boncode_validation_event(df, metadata)
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_raises_value_error_for_missing_columns():
    """
    Test that a ValueError is raised if required columns are missing.
    """
    df = pd.DataFrame({
        'Measure_Cd': ['A1'],
        'Measure_Desc': ['desc1']
        # Missing 'Sheet_Cd'
    })
    metadata = {
        'Batch_Id': 'batch1',
        'Submission_Period_Cd': '202301',
        'Process_Cd': 'proc1',
        'Template_Version': 'v1',
        'Organisation_Cd': 'org1'
    }

    with pytest.raises(ValueError, match="Missing required columns"):
        create_same_desc_diff_boncode_validation_event(df, metadata)

def test_raises_value_error_for_invalid_df_type():
    """
    Test that a ValueError is raised if df argument is not a DataFrame.
    """
    df = "not a dataframe"
    metadata = {
        'Batch_Id': 'batch1',
        'Submission_Period_Cd': '202301',
        'Process_Cd': 'proc1',
        'Template_Version': 'v1',
        'Organisation_Cd': 'org1'
    }

    with pytest.raises(ValueError, match="Input 'df' must be a pandas DataFrame"):
        create_same_desc_diff_boncode_validation_event(df, metadata)

def test_raises_if_metadata_not_dict():
    """test_raises_if_metadata_not_dict"""
    df = pd.DataFrame({
        "Measure_Cd": ["A5"],
        "Measure_Desc": ["Desc7"],
        "Sheet_Cd": ["Sheet9"]
    })
    not_metadata = ["not", "a", "dict"]

    with pytest.raises(ValueError, match="Input 'metadata' must be a dict."):
        create_same_desc_diff_boncode_validation_event(df, not_metadata)
