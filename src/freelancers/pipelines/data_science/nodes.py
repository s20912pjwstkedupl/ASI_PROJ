import logging
import os
from pathlib import Path
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame):
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
    return train_data, test_data


def train_model(train_data: pd.DataFrame, hyperparameters: dict) -> TabularPredictor:
    print(train_data)
    print(train_data["Job_Success_Rate"])
    print(train_data.dtypes)
    print(train_data.isna().sum())
    predictor = TabularPredictor(label="Job_Success_Rate", eval_metric="f1_macro", verbosity=2)
    model = predictor.fit(
    train_data=train_data,
    presets='medium_quality',  # albo medium_quality jeśli chcesz szybciej
    hyperparameters=hyperparameters)
    print(model.feature_importance(train_data))
    return model

def save_model(predictor: TabularPredictor, model_output_path: str):
    # Zapisujemy model
    print(predictor.leaderboard(silent=True))
    predictor.save()
    os.rename(predictor.path, model_output_path)
    return str(model_output_path)

def test_model(saved_model_path: str, data: pd.DataFrame):
    model = TabularPredictor.load(saved_model_path)
    y_pred = model.predict(data)
    preds_usd = np.expm1(y_pred)
    true_usd = np.expm1(data["Job_Success_Rate"])
    print("RMSE:", mean_squared_error(true_usd, preds_usd, squared=False))
    print("MAE:", mean_absolute_error(true_usd, preds_usd))
    print("R²:", r2_score(true_usd, preds_usd))
