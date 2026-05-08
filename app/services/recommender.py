import numpy as np

from app.services.embedder import (
    create_embedding
)

from app.services.vector_store import (
    index
)

from app.utils.provider_data import (
    SERVICES
)

from app.services.scorer import (
    calculate_score
)

from app.services.filter import (
    filter_services
)

from app.services.cost_engine import (
    estimate_cost
)


def recommend_services(
    query,
    parsed,
    top_k=10
):

    query_embedding = np.array(
        [create_embedding(query)]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    # Vector search results
    vector_results = []

    for idx in indices[0]:

        service = SERVICES[idx]

        vector_results.append(service)

    # Apply filtering
    filtered_services = filter_services(
        vector_results,
        parsed
    )

    recommendations = []

    for rank, service in enumerate(
        filtered_services
    ):

        score = calculate_score(
            service,
            parsed,
            rank
        )

        dynamic_cost = estimate_cost(
            service["name"]
        )

        recommendations.append({

            "service": service["name"],

            "provider": service["provider"],

            "score": score,

            "estimated_cost": dynamic_cost,

            "latency": service["latency"],

            "gpu_support": service["gpu"],

            "managed": service["managed"]

        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations