from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_earnings


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_earnings,
                inputs="earnings",
                outputs="preprocessed_freelancers",
                name="preprocess_freelancers_node",
            ),

        ]
    )
