from app.services.pricing import (
    get_azure_vm_price
)

def estimate_cost(service_name):

    # Azure ML dynamic pricing
    if service_name == "Azure ML":

        hourly_price = get_azure_vm_price()

        if hourly_price:

            monthly = (
                hourly_price * 24 * 30
            )

            return round(monthly, 2)

    # Static fallback pricing
    fallback_costs = {

        "AWS SageMaker": 250,
        "AWS EC2": 150,
        "AWS Bedrock": 300,
        "AWS Lambda": 40,

        "Google Vertex AI": 240,
        "Google Cloud Run": 60,

        "RunPod": 90,
        "Lambda Labs": 100,
        "CoreWeave": 180,

        "Groq": 50,
        "OpenAI API": 120,
        "Anthropic Claude API": 130,

        "Kubernetes": 170,
        "Railway": 30
    }

    return fallback_costs.get(
        service_name,
        100
    )