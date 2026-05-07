SERVICES = {
    "EC2": {
        "gpu": True,
        "cost": 150,
        "latency": 100,
        "scalability": 20,
        "ease": 10
    },
    "SageMaker": {
        "gpu": True,
        "cost": 250,
        "latency": 80,
        "scalability": 25,
        "ease": 25
    },
    "Lambda": {
        "gpu": False,
        "cost": 50,
        "latency": 200,
        "scalability": 30,
        "ease": 30
    },
    "ECS": {
        "gpu": True,
        "cost": 120,
        "latency": 120,
        "scalability": 25,
        "ease": 20
    },
    "Bedrock": {
        "gpu": False,
        "cost": 300,
        "latency": 90,
        "scalability": 30,
        "ease": 30
    }
}