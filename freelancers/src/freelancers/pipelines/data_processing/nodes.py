import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.model_selection import train_test_split
import numpy as np


def preprocess_earnings(freelancers: pd.DataFrame, model_options: dict) -> pd.DataFrame:
    # freelancers["Earnings_USD"] = freelancers["Earnings_USD"].apply(rating_to_class)
    return freelancers

def engineer_custom_features(data: pd.DataFrame):
    df = data.copy()
    df["Estimated_Earnings"] = df["Hourly_Rate"] * df["Job_Duration_Days"]
    df["Rehire_Impact"] = df["Rehire_Rate"] * df["Job_Completed"]
    df["Success_Weighted_Impact"] = df["Job_Success_Rate"] * df["Rehire_Rate"]

    def rating_to_class(rating):
        if rating <= 60:
            return "Low"
        elif rating < 90:
            return "Medium"
        else:
            return "High"

    df["Job_Success_Rate"] = df["Job_Success_Rate"].apply(rating_to_class)

    cat_cols = [
        "Job_Category", "Platform", "Experience_Level",
        "Client_Region", "Payment_Method", "Project_Type"
    ]
    df[cat_cols] = df[cat_cols].astype("category")

    df_model = df.drop(columns=["Freelancer_ID", "Earnings_USD"])
    return df_model
