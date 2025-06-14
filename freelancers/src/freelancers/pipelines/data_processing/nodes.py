import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.model_selection import train_test_split


def preprocess_earnings(freelancers: pd.DataFrame) -> pd.DataFrame:
    freelancers = freelancers.drop(columns=["Freelancer_ID"], errors="ignore")

    def rating_to_class(rating):
        if rating <= 60:
            return "Low"
        elif rating < 90:
            return "Medium"
        else:
            return "High"

    freelancers["Job_Success_Rate"] = freelancers["Job_Success_Rate"].apply(rating_to_class)
    return freelancers