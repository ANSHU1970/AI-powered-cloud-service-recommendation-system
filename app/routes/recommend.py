from fastapi import APIRouter
from app.models.schema import UserInput
from app.services.parser import parse_input
from app.services.scorer import score_services
from app.services.cost import estimate_cost
from app.services.explainer import generate_explanation

router = APIRouter()

@router.post("/recommend")
def recommend(data: UserInput):

    parsed = parse_input(data.text)

    scores = score_services(parsed)

    results = []
    for service, score in scores.items():
        cost = estimate_cost(service, parsed)

        results.append({
            "service": service,
            "score": score,
            "estimated_cost": cost
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)[:3]

    # Add explanations
    # for r in results:
    #     r["explanation"] = generate_explanation(r["service"], parsed)

    return {
        "parsed_input": parsed,
        "recommendations": results
    }