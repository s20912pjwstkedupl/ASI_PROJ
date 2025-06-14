import logging
import os
from pathlib import Path

import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame):
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
    return train_data, test_data


def train_model(train_data: pd.DataFrame, hyperparameters: dict) -> TabularPredictor:
    predictor = TabularPredictor(label="Job_Success_Rate")
    model = predictor.fit(train_data, hyperparameters=hyperparameters)
    return model

def save_model(predictor: TabularPredictor, model_output_path: str):
    # Zapisujemy model
    predictor.save()
    os.rename(predictor.path, model_output_path)
    return str(model_output_path)