import requests

AZURE_PRICING_URL = (
    "https://prices.azure.com/api/retail/prices"
)

def get_azure_vm_price(
    vm_name="Standard_NC4as_T4_v3"
):

    try:

        params = {
            "$filter":
            f"serviceName eq 'Virtual Machines' "
            f"and armSkuName eq '{vm_name}'"
        }

        response = requests.get(
            AZURE_PRICING_URL,
            params=params
        )

        data = response.json()

        items = data.get("Items", [])

        if not items:
            return None

        price = items[0].get("retailPrice")

        return price

    except Exception as e:

        print("Azure Pricing Error:", e)

        return None