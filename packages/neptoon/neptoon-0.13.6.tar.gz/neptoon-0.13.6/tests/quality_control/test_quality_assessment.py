import pytest
import pandas as pd
from neptoon.quality_control.quality_assessment import (
    QAMethod,
    QATarget,
    ValidationError,
    QualityCheck,
    DateTimeIndexValidator,
    DataQualityAssessor,
)
from datetime import datetime
from neptoon.columns import ColumnInfo


@pytest.fixture
def df():
    df = pd.DataFrame(
        {
            "range": [
                400,
                500,
                400,
                300,
                500,
            ],
            "spike": [
                1010,
                2000,
                2300,
                2300,
                8000,
            ],
        }
    )
    return df


def test_quality_check_validation():

    with pytest.raises(ValidationError):
        QualityCheck(
            target=str(ColumnInfo.Name.INCOMING_NEUTRON_INTENSITY),
            method=QAMethod.RANGE_CHECK,
            parameters={"min": 500},
        )


def test_wrong_param_supplied():
    with pytest.raises(ValidationError):
        QualityCheck(
            target=str(ColumnInfo.Name.INCOMING_NEUTRON_INTENSITY),
            method=QAMethod.RANGE_CHECK,
            parameters={
                "min": 500,
                "max": 550,
                "crazy_param": 550,
            },
        )


def test_column_assignment_quality_check_1():
    check = QualityCheck(
        target=QATarget.AIR_PRESSURE,
        method=QAMethod.RANGE_CHECK,
        parameters={
            "min": 500,
            "max": 550,
        },
    )
    assert "column_name" in check.parameters.keys()


def test_column_assignment_quality_check_2():
    check1 = QualityCheck(
        target=QATarget.AIR_PRESSURE,
        method=QAMethod.RANGE_CHECK,
        parameters={
            "min": 500,
            "max": 550,
        },
    )
    assert check1.parameters["column_name"] == str(
        ColumnInfo.Name.AIR_PRESSURE
    )


def test_date_time_index_validator():
    """
    Tests the object which checks if a DataFrame has a datetime index.
    """
    data = {
        "Column1": [1, 2, 3, 4, 5],
        "Column2": ["A", "B", "C", "D", "E"],
        "Column3": [10.1, 20.2, 30.3, 40.4, 50.5],
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        DateTimeIndexValidator(df)


def test_date_time_index_validator_with_date():
    """
    Tests the object which checks if a DataFrame has a datetime index.
    """
    data = {
        "Column1": [1, 2, 3, 4, 5],
        "Column2": ["A", "B", "C", "D", "E"],
        "Column3": [10.1, 20.2, 30.3, 40.4, 50.5],
    }
    df = pd.DataFrame(data)
    date_range = pd.date_range(start="2023-01-01", periods=5, freq="D")
    df.index = date_range
    DateTimeIndexValidator(df)


@pytest.fixture
def test_df():

    start_date = datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    date_range = pd.date_range(start=start_date, periods=5, freq="h")

    test_df = pd.DataFrame(
        {
            str(ColumnInfo.Name.AIR_PRESSURE): [555, 546, 515, 496, 500],
            str(ColumnInfo.Name.CORRECTED_EPI_NEUTRON_COUNT_FINAL): [
                56,
                60,
                70,
                60,
                45,
            ],
        },
        index=date_range,
    )
    return test_df


def test_quality_assessment(test_df):

    check1 = QualityCheck(
        target=QATarget.AIR_PRESSURE,
        method=QAMethod.RANGE_CHECK,
        parameters={
            "min": 500,
            "max": 550,
        },
    )

    qa = DataQualityAssessor(data_frame=test_df)
    qa.add_quality_check(check1)

    qa.apply_quality_assessment()

    result_df = qa.return_flags_data_frame()
    expected_flags = [
        "BAD",
        "UNFLAGGED",
        "UNFLAGGED",
        "BAD",
        "UNFLAGGED",
    ]
    actual_flags = result_df[str(ColumnInfo.Name.AIR_PRESSURE)].tolist()

    assert (
        actual_flags == expected_flags
    ), f"Expected {expected_flags}, but got {actual_flags}"


def test_quality_assessment_multi(test_df):

    check1 = QualityCheck(
        target=QATarget.AIR_PRESSURE,
        method=QAMethod.RANGE_CHECK,
        parameters={
            "min": 500,
            "max": 550,
        },
    )

    check2 = QualityCheck(
        target=QATarget.CORRECTED_EPI_NEUTRONS,
        method=QAMethod.RANGE_CHECK,
        parameters={
            "min": 50,
            "max": 65,
        },
    )

    qa = DataQualityAssessor(data_frame=test_df)
    qa.add_quality_check(check1)
    qa.add_quality_check(check2)

    qa.apply_quality_assessment()

    result_df = qa.return_flags_data_frame()
    print(result_df)
    expected_flags1 = [
        "BAD",
        "UNFLAGGED",
        "UNFLAGGED",
        "BAD",
        "UNFLAGGED",
    ]
    expected_flags2 = [
        "UNFLAGGED",
        "UNFLAGGED",
        "BAD",
        "UNFLAGGED",
        "BAD",
    ]
    actual_flag1 = result_df[str(ColumnInfo.Name.AIR_PRESSURE)].tolist()
    actual_flag2 = result_df[
        str(ColumnInfo.Name.CORRECTED_EPI_NEUTRON_COUNT_FINAL)
    ].tolist()

    assert (
        actual_flag1 == expected_flags1
    ), f"Expected {expected_flags1}, but got {actual_flag1}"

    assert (
        actual_flag2 == expected_flags2
    ), f"Expected {expected_flags2}, but got {actual_flag2}"


def test_spike_offset_detects_plateau_above_20_percent_only_on_rising_edge():
    # 1) build a DataFrame with datetime index and a plateau spike
    idx = pd.date_range(start="2025-06-25", periods=8, freq="h")
    values = [100, 110, 100, 150, 150, 150, 119, 120]
    df = pd.DataFrame({str(ColumnInfo.Name.AIR_PRESSURE): values}, index=idx)

    # 2) set up the assessor and register a single SPIKE_OFFSET check
    assessor = DataQualityAssessor(df)
    spike_check = QualityCheck(
        target=QATarget.AIR_PRESSURE,
        method=QAMethod.SPIKE_OFFSET,
        parameters={
            # essential params for offset detection
            "window": "12h",  # compare one step before & after
            "threshold_relative": 0.2,
        },
    )
    assessor.add_quality_check(spike_check)

    # 3) run QC, extract the flags
    assessor.apply_quality_assessment()
    flags = assessor.return_flags_data_frame()
    print(flags)

    result_df = assessor.return_flags_data_frame()
    expected_flags = [
        "UNFLAGGED",
        "UNFLAGGED",
        "UNFLAGGED",
        "BAD",
        "BAD",
        "BAD",
        "UNFLAGGED",
        "UNFLAGGED",
    ]
    actual_flags = result_df[str(ColumnInfo.Name.AIR_PRESSURE)].tolist()
    assert actual_flags == expected_flags


def test_spike_offset_detects_plateau_above_20_percent_on_lower():
    # 1) build a DataFrame with datetime index and a plateau spike
    idx = pd.date_range(start="2025-06-25", periods=8, freq="h")
    values = [100, 110, 100, 50, 50, 50, 85, 85]
    df = pd.DataFrame({str(ColumnInfo.Name.AIR_PRESSURE): values}, index=idx)

    # 2) set up the assessor and register a single SPIKE_OFFSET check
    assessor = DataQualityAssessor(df)
    spike_check = QualityCheck(
        target=QATarget.AIR_PRESSURE,
        method=QAMethod.SPIKE_OFFSET,
        parameters={
            # essential params for offset detection
            "threshold_relative": (0.2, -0.2),
            "window": "12h",
        },
    )
    assessor.add_quality_check(spike_check)

    assessor.apply_quality_assessment()
    flags = assessor.return_flags_data_frame()
    print(flags)

    result_df = assessor.return_flags_data_frame()
    expected_flags = [
        "UNFLAGGED",
        "UNFLAGGED",
        "UNFLAGGED",
        "BAD",
        "BAD",
        "BAD",
        "UNFLAGGED",
        "UNFLAGGED",
    ]
    actual_flags = result_df[str(ColumnInfo.Name.AIR_PRESSURE)].tolist()
    assert actual_flags == expected_flags
