from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    get_cart_model_input,
    get_popular_model_input,
    get_similar_model_input,
)

base_ml_models_pipeline = pipeline(
    [
        node(
            get_cart_model_input,
            inputs={
                "produtos": "03_primary.produtos",
                "storesStock": "03_primary.storesStockSnapshot",
                "transactions": "03_primary.transactions",
                "params": "params:cart",
            },
            outputs=[
                "05_model_input.cart.produtos",
                "05_model_input.cart.stores_products",
                "05_model_input.cart.rules",
            ],
            tags="cart",
        ),
        node(
            get_popular_model_input,
            inputs={
                "produtos": "03_primary.produtos",
                "storesStock": "03_primary.storesStockSnapshot",
                "transactions": "03_primary.transactions",
                "params": "params:popular",
            },
            outputs=[
                "05_model_input.popular.produtos",
                "05_model_input.popular.store_stock",
                "05_model_input.popular.master_product_rank",
            ],
            tags="popular",
        ),
        node(
            get_similar_model_input,
            inputs={
                "produtos": "03_primary.produtos",
                "storesStock": "03_primary.storesStockSnapshot",
                "params": "params:similar",
            },
            outputs=[
                "05_model_input.similar.produtos",
                "05_model_input.similar.stores_products",
                "05_model_input.similar.produtosMestre_matrixIndices_mapping",
                "05_model_input.similar.tfidf_matrix",
            ],
            tags="similar",
        ),
    ]
)


def create_pipeline(**kwargs) -> Pipeline:
    ds_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="ds",
    )

    averara_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="averara",
    )

    botti_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="botti",
    )

    casaprado_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="casaprado",
    )

    capodarte_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="capodarte",
    )

    prestige_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="prestige",
    )

    niini_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="niini",
    )

    fillity_pipe = pipeline(
        base_ml_models_pipeline,
        namespace="fillity",
    )

    return ds_pipe + averara_pipe + botti_pipe + casaprado_pipe + capodarte_pipe + prestige_pipe + niini_pipe + fillity_pipe
