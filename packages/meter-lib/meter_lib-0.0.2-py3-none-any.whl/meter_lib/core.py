import requests

def fetch_customer_id(tenant_id: str):
    """
    Fetch the customer account for a given tenant_id.
    Returns a dict with customer info, or None if not found/error.
    """
    url = f"http://metering.metering.svc.cluster.local:8000/api/v1/customer-accounts/tenant/{tenant_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Handle list response
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        elif isinstance(data, dict):
            return data
        else:
            print(f"No customer account found for tenant {tenant_id}")
            return None

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def post_meter_usage(tenant_id: str, device_id: str, meter_id: str, total_usage: int) :
    """
    Posts meter usage to the events API.
    Uses tenant_id + device_id in headers and includes customer_id in payload.
    """
    customer_account = fetch_customer_id(tenant_id)
    if not customer_account:
        print("No customer account available, skipping meter usage post")
        return None

    url = "http://metering.metering.svc.cluster.local:8000/api/v1/events"
    headers = {
        "x-tenant-id": tenant_id,
        "x-device-id": device_id,
        "Content-Type": "application/json"
    }
    payload = {
        "meter_id": meter_id,
        "total_usage": total_usage,
        "customer_id": customer_account["id"]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f" Error posting to {url}: {e}")
        return None
