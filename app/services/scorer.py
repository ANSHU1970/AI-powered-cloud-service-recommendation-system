from app.utils.aws_data import SERVICES

def score_services(parsed):

    scores = {}

    for service, config in SERVICES.items():
        score = 0

        # GPU
        if parsed["gpu"] and config["gpu"]:
            score += 30

        # Budget
        if parsed["budget"] >= config["cost"]:
            score += 25

        # Latency
        if parsed["latency"] >= config["latency"]:
            score += 20

        # Scalability
        score += config["scalability"]

        # Ease
        score += config["ease"]

        scores[service] = score

    return scores