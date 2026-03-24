import pandas as pd
import os

def test_dataset_exists():
    assert os.path.exists("data/sdss_sample.csv")

def test_dataset_not_empty():
    df = pd.read_csv("data/sdss_sample.csv")
    assert len(df) > 0

def test_required_columns():
    df = pd.read_csv("data/sdss_sample.csv")
    required = ['u', 'g', 'r', 'i', 'z', 'redshift', 'class']
    for col in required:
        assert col in df.columns