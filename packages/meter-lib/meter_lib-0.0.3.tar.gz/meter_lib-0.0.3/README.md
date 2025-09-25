## meter-lib — Usage Guide

### Overview

`meter-lib` is a lightweight helper library for sending metering events to the Litewave backend and for looking up a customer account by `tenant_id`.

### Requirements

- Python 3.10+

### Installation

```bash
pip install meter-lib
```

### Parameters Required

```
tenant_id,
device_id,
meter_id,
total_usage
```

### Quickstart

```python
from meter_lib import post_meter_usage

tenant_id = "tenant_123"
device_id = "device_456"
meter_id = "pages.processed.rate.hourly"

result = post_meter_usage(
    tenant_id=tenant_id,
    device_id=device_id,
    meter_id=meter_id,
    total_usage=24,  # integer units as defined by your meter
)

if result is None:
    # Handle network error or non-2xx response
    print("Failed to post meter usage event")
else:
    print("Event accepted:", result)
```

### Error Handling

- `post_meter_usage` returns `None` for network errors or non-success HTTP statuses.
- Prefer explicit checks for `None` and add retries or backoff in your application layer if needed.

### API Reference

#### post_meter_usage(tenant_id: str, device_id: str, meter_id: str, total_usage: int) -> dict | None

- **Description**: Posts a metering event for a device and meter under a given tenant.
- **Headers**:
  - `x-tenant-id`: the tenant identifier (string)
  - `x-device-id`: the device identifier (string)
- **Payload (JSON)**:
  - `meter_id` (string)
  - `total_usage` (integer)
  - `customer_id` (string) — auto-filled by the library.`
- **Returns**: The backend JSON response (`dict`) on success, otherwise `None`.
- **Timeout**: 10 seconds.
- **Notes**:
  - If the customer lookup fails, the call is skipped and `None` is returned.
  - This function is synchronous and will block until the request completes or times out.

### Troubleshooting

- Confirm your `tenant_id`, `device_id`, and `meter_id` values are correct.

### Support

- Homepage: `https://github.com/aiorch/meter-lib`
- Issues: `https://github.com/aiorch/meter-lib/issues`
