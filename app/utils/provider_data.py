SERVICES = [

    # AWS
    {
        "name": "AWS SageMaker",
        "provider": "AWS",
        "description": "Managed machine learning platform for scalable GPU inference and training",
        "gpu": True,
        "serverless": False,
        "managed": True,
        "latency": 80,
        "cost": 250
    },

    {
        "name": "AWS EC2",
        "provider": "AWS",
        "description": "Virtual machines with GPU support for custom ML deployment",
        "gpu": True,
        "serverless": False,
        "managed": False,
        "latency": 100,
        "cost": 150
    },

    {
        "name": "AWS Bedrock",
        "provider": "AWS",
        "description": "Managed foundation model API platform for generative AI",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 60,
        "cost": 300
    },

    {
        "name": "AWS Lambda",
        "provider": "AWS",
        "description": "Serverless compute platform for lightweight inference",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 150,
        "cost": 40
    },

    # GCP
    {
        "name": "Google Vertex AI",
        "provider": "GCP",
        "description": "Managed AI platform with scalable training and inference",
        "gpu": True,
        "serverless": False,
        "managed": True,
        "latency": 75,
        "cost": 240
    },

    {
        "name": "Google Cloud Run",
        "provider": "GCP",
        "description": "Serverless container platform for scalable APIs and inference",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 120,
        "cost": 60
    },

    # Azure
    {
        "name": "Azure ML",
        "provider": "Azure",
        "description": "Managed machine learning platform with enterprise integration",
        "gpu": True,
        "serverless": False,
        "managed": True,
        "latency": 85,
        "cost": 245
    },

    # GPU Providers
    {
        "name": "RunPod",
        "provider": "RunPod",
        "description": "Low-cost GPU cloud optimized for LLM inference and AI hosting",
        "gpu": True,
        "serverless": False,
        "managed": False,
        "latency": 110,
        "cost": 90
    },

    {
        "name": "Lambda Labs",
        "provider": "Lambda",
        "description": "Affordable GPU servers for deep learning and LLM workloads",
        "gpu": True,
        "serverless": False,
        "managed": False,
        "latency": 115,
        "cost": 100
    },

    {
        "name": "CoreWeave",
        "provider": "CoreWeave",
        "description": "High performance GPU cloud for AI model deployment",
        "gpu": True,
        "serverless": False,
        "managed": False,
        "latency": 70,
        "cost": 180
    },

    # LLM APIs
    {
        "name": "Groq",
        "provider": "Groq",
        "description": "Ultra low latency inference platform for LLM applications",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 20,
        "cost": 50
    },

    {
        "name": "OpenAI API",
        "provider": "OpenAI",
        "description": "Hosted API access for GPT models and AI applications",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 40,
        "cost": 120
    },

    {
        "name": "Anthropic Claude API",
        "provider": "Anthropic",
        "description": "Hosted Claude API for enterprise AI workloads",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 45,
        "cost": 130
    },

    # Container Platforms
    {
        "name": "Kubernetes",
        "provider": "CNCF",
        "description": "Container orchestration platform for scalable ML infrastructure",
        "gpu": True,
        "serverless": False,
        "managed": False,
        "latency": 90,
        "cost": 170
    },

    {
        "name": "Railway",
        "provider": "Railway",
        "description": "Simple cloud deployment platform for APIs and ML services",
        "gpu": False,
        "serverless": True,
        "managed": True,
        "latency": 130,
        "cost": 30
    }

]