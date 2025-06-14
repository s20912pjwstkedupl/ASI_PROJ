from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data, train_model, save_model, test_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(func=split_data, inputs="train_data_engineered", outputs=["train_data", "test_data"],
                 name="split_data_node"),
            node(func=train_model, inputs=["train_data", "params:hyperparameters"], outputs="model",
                 name="train_model_node"),
            node(
                func=save_model,
                inputs=["model", "params:model_output_path"],
                outputs="saved_model_path",
                name="save_model_node"
            ),
            node(func=test_model, inputs=["saved_model_path", "test_data"], outputs=[],
                 name="test_model_node"),
        ]
    )
