from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_earnings, engineer_custom_features


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_earnings,
                inputs=["earnings", "params:model_options"],
                outputs="preprocessed_freelancers",
                name="preprocess_freelancers_node",
            ),
            node(func=engineer_custom_features, inputs="preprocessed_freelancers", outputs="train_data_engineered",
                 name="engineer_features"),
        ]
    )
