def estimate_cost(service, parsed):

    base_cost = {
        "EC2": 120,
        "SageMaker": 220,
        "Lambda": 50,
        "ECS": 100,
        "Bedrock": 300
    }

    cost = base_cost.get(service, 100)

    if parsed["users"]:
        cost += parsed["users"] * 0.1

    return round(cost, 2)