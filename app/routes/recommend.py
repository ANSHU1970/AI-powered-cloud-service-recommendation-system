from fastapi import APIRouter

from app.models.schema import UserInput
from app.services.parser import parse_input
from app.services.recommender import recommend_services

router = APIRouter()


@router.post("/recommend")
def recommend(data: UserInput):

    # Structured input mode
    if data.model_size or data.users or data.budget:

        print("Using structured input")

        parsed = {
            "model_size": data.model_size,
            "users": data.users,
            "latency": data.latency,
            "budget": data.budget,
            "gpu": data.gpu,
            "inference_type": data.inference_type
        }

    # Natural language mode
    else:

        print("Using LLaMA parser")

        parsed = parse_input(data.text)

    recommendations = recommend_services(
        data.text if data.text else str(parsed),
        parsed
    )

    return {
        "parsed_input": parsed,
        "recommendations": recommendations
    }