import pandas as pd
import pytest
from clean_csv import clean_dataframe
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # 让 Python 能找到同级 clean_csv.py

from clean_csv import clean_dataframe

def test_missing_columns_raises():
    df = pd.DataFrame({"a":[1,2], "b":[3,4]})
    with pytest.raises(ValueError):
        clean_dataframe(df, columns=["a","c"])

def test_dropna_removes_rows():
    df = pd.DataFrame({"a":[1,None,3], "b":[1,2,3]})
    df_out, summary = clean_dataframe(df, dropna=True, dropna_cols=["a"])
    assert len(df_out) == 2
    assert summary["rows_removed_na"] == 1

def test_dedup_removes_duplicates():
    df = pd.DataFrame({"name":["x","x","y"], "age":[1,1,2]})
    df_out, summary = clean_dataframe(df, dedup=True)
    assert len(df_out) == 2
    assert summary["rows_removed_dups"] == 1
