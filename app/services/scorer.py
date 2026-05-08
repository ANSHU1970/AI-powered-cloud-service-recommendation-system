def calculate_score(service, parsed, vector_rank):

    score = 0

    # Vector search influence
    score += (10 - vector_rank) * 10

    # GPU preference
    if parsed.get("gpu") and service["gpu"]:
        score += 30

    # Budget scoring
    if parsed.get("budget"):

        budget_score = max(
            0,
            1 - (service["cost"] / parsed["budget"])
        )

        score += budget_score * 25

    # Latency scoring
    if parsed.get("latency"):

        latency_score = max(
            0,
            1 - (service["latency"] / parsed["latency"])
        )

        score += latency_score * 20

    # Managed services bonus
    if service["managed"]:
        score += 10

    return round(score, 2)