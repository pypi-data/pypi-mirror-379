# oytel-esim

Official Oytel eSIM API SDK for Python.

[![PyPI version](https://badge.fury.io/py/oytel-esim.svg)](https://badge.fury.io/py/oytel-esim)
[![Python Support](https://img.shields.io/pypi/pyversions/oytel-esim.svg)](https://pypi.org/project/oytel-esim/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

### Installation

```bash
pip install oytel-esim
```

### Basic Usage

```python
from oytel import OytelClient

# Initialize client with your API key
client = OytelClient(api_key="sk_sandbox_your_api_key_here")

# Get available plans
plans = client.get_plans()
print(f"Found {len(plans['plans'])} plans")

# Provision an eSIM
esim = client.provision_esim(
    plan_id="eu-roam-50",
    customer_email="customer@example.com",
    customer_name="John Doe"
)

print(f"eSIM ID: {esim['esim']['esim_id']}")
print(f"QR Code: {esim['esim']['qr_code_url']}")
print(f"Activation Code: {esim['esim']['activation_code']}")
print(f"Cost: ${esim['billing']['cost_usd']}")

# Check eSIM status
status = client.get_esim_status(esim['esim']['esim_id'])
print(f"Status: {status['esim']['status']}")

if status['esim']['usage']:
    usage = status['esim']['usage']
    print(f"Data used: {usage['used_mb']}MB / {usage['total_mb']}MB")
    print(f"Usage: {usage['usage_percentage']}%")
```

## 📖 API Reference

### Client Initialization

```python
from oytel import OytelClient

client = OytelClient(
    api_key="sk_sandbox_your_key_here",  # Required: Your API key
    base_url="https://api.oytel.co.uk",  # Optional: API base URL
    environment="sandbox",               # Optional: Auto-detected from API key
    timeout=30                          # Optional: Request timeout in seconds
)
```

### Methods

#### `get_plans() -> PlansResponse`

Get all available eSIM plans.

```python
plans = client.get_plans()

# Access plan data
for plan in plans['plans']:
    print(f"{plan['name']}: ${plan['pricing']['base_price']}")
    print(f"Coverage: {plan['coverage']}")
    print(f"Data: {plan['data_allowance']}")
    print(f"Validity: {plan['validity_days']} days")
```

#### `provision_esim(...) -> ProvisionResponse`

Provision a new eSIM for a customer.

```python
esim = client.provision_esim(
    plan_id="eu-roam-50",
    customer_email="customer@example.com",
    customer_name="John Doe",
    reference_id="order-123",  # Optional
    webhook_url="https://your-app.com/webhook"  # Optional
)

# Access eSIM details
esim_info = esim['esim']
billing_info = esim['billing']

print(f"eSIM ID: {esim_info['esim_id']}")
print(f"ICCID: {esim_info['iccid']}")
print(f"QR Code URL: {esim_info['qr_code_url']}")
print(f"Manual Code: {esim_info['activation_code']}")
print(f"Cost: ${billing_info['cost_usd']}")
print(f"Remaining Balance: ${billing_info['remaining_balance']}")
```

#### `get_esim_status(esim_id: str) -> StatusResponse`

Get detailed status and usage information for an eSIM.

```python
status = client.get_esim_status("esim_123456")

esim_status = status['esim']
print(f"Status: {esim_status['status']}")
print(f"Activated: {esim_status['activation']['activated']}")

# Check data usage (if available)
if esim_status['usage']:
    usage = esim_status['usage']
    print(f"Data used: {usage['used_mb']}MB")
    print(f"Data remaining: {usage['remaining_mb']}MB")
    print(f"Usage percentage: {usage['usage_percentage']}%")

# Check connection info (if available)
if esim_status['connection']:
    conn = esim_status['connection']
    print(f"Connection status: {conn['status']}")
    if conn['current_network']:
        network = conn['current_network']
        print(f"Current network: {network['operator']} ({network['country_name']})")
        print(f"Signal strength: {network['signal_strength']}/5")
```

## 🔑 Authentication

### API Keys

Get your API keys from the [Oytel Developer Dashboard](https://oytel.co.uk/developers/dashboard):

- **Sandbox**: `sk_sandbox_...` - Free testing with mock data
- **Production**: `sk_live_...` - Real billing with test eSIMs

### Environment Detection

```python
# Sandbox client
sandbox_client = OytelClient(api_key="sk_sandbox_...")
print(sandbox_client.get_environment())  # "sandbox"

# Production client  
prod_client = OytelClient(api_key="sk_live_...")
print(prod_client.get_environment())  # "production"
```

## 🛡️ Error Handling

The SDK provides specific exception types for different error scenarios:

```python
from oytel import OytelClient, OytelError, OytelAPIError, OytelAuthError

client = OytelClient(api_key="sk_sandbox_...")

try:
    esim = client.provision_esim(
        plan_id="invalid-plan",
        customer_email="test@example.com", 
        customer_name="Test User"
    )
except OytelAuthError as e:
    print(f"Authentication error: {e}")
except OytelAPIError as e:
    print(f"API error: {e}")
    print(f"Status code: {e.status_code}")
    print(f"Error code: {e.error_code}")
except OytelError as e:
    print(f"General error: {e}")
```

### Exception Types

- **`OytelError`**: Base exception for all SDK errors
- **`OytelAPIError`**: API-specific errors (4xx, 5xx responses)
- **`OytelAuthError`**: Authentication and authorization errors

## 💰 Billing & Costs

### Sandbox Environment
- **Free unlimited testing**
- **$100 fake credits** (never depleted)
- **Mock eSIMs** (realistic responses but non-functional)

### Production Environment
- **Real money billing** from your account balance
- **Test eSIMs** (safe - no real inventory used)
- **Minimum $200 balance** required for production access
- **$25 minimum balance** to continue API usage

## 📱 eSIM Integration Examples

### Display QR Code

```python
import qrcode
from PIL import Image
import requests

# Provision eSIM
esim = client.provision_esim(
    plan_id="eu-roam-50",
    customer_email="customer@example.com",
    customer_name="John Doe"
)

# Generate QR code from activation code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(esim['esim']['activation_code'])
qr.make(fit=True)

# Create QR code image
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("esim_qr_code.png")

# Or download the provided QR code URL
qr_response = requests.get(esim['esim']['qr_code_url'])
with open("esim_qr_from_api.png", "wb") as f:
    f.write(qr_response.content)
```

### Monitor Usage

```python
import time

def monitor_esim_usage(client, esim_id, threshold=80):
    """Monitor eSIM usage and alert when threshold is reached."""
    
    while True:
        try:
            status = client.get_esim_status(esim_id)
            
            if status['esim']['usage']:
                usage = status['esim']['usage']
                usage_percent = usage['usage_percentage']
                
                print(f"Current usage: {usage_percent}%")
                
                if usage_percent >= threshold:
                    print(f"⚠️  WARNING: Usage exceeded {threshold}%!")
                    print(f"Data used: {usage['used_mb']}MB / {usage['total_mb']}MB")
                    break
                    
        except Exception as e:
            print(f"Error checking usage: {e}")
        
        # Check every hour
        time.sleep(3600)

# Start monitoring
monitor_esim_usage(client, "esim_123456", threshold=80)
```

### Batch Provisioning

```python
def provision_bulk_esims(client, customers, plan_id):
    """Provision eSIMs for multiple customers."""
    
    results = []
    
    for customer in customers:
        try:
            esim = client.provision_esim(
                plan_id=plan_id,
                customer_email=customer['email'],
                customer_name=customer['name'],
                reference_id=customer.get('order_id')
            )
            
            results.append({
                'customer': customer,
                'esim_id': esim['esim']['esim_id'],
                'qr_code': esim['esim']['qr_code_url'],
                'activation_code': esim['esim']['activation_code'],
                'success': True
            })
            
        except Exception as e:
            results.append({
                'customer': customer,
                'error': str(e),
                'success': False
            })
    
    return results

# Example usage
customers = [
    {'name': 'John Doe', 'email': 'john@example.com', 'order_id': 'ORD001'},
    {'name': 'Jane Smith', 'email': 'jane@example.com', 'order_id': 'ORD002'},
]

results = provision_bulk_esims(client, customers, "eu-roam-50")

for result in results:
    if result['success']:
        print(f"✅ {result['customer']['name']}: {result['esim_id']}")
    else:
        print(f"❌ {result['customer']['name']}: {result['error']}")
```

## 🔄 Context Manager Usage

```python
# Use with context manager for automatic cleanup
with OytelClient(api_key="sk_sandbox_...") as client:
    plans = client.get_plans()
    print(f"Found {len(plans['plans'])} plans")
    
    esim = client.provision_esim(
        plan_id="eu-roam-50",
        customer_email="test@example.com",
        customer_name="Test User"
    )
    print(f"Provisioned: {esim['esim']['esim_id']}")

# Session automatically closed when exiting the context
```

## 🌍 Supported Regions

Available eSIM plans cover:

- **Europe**: 27+ countries with high-speed data
- **Global**: 190+ countries worldwide coverage
- **Regional**: Asia, Americas, Middle East specific plans  
- **Country-specific**: UK, USA, and other individual countries

## 🌐 About Oytel

**Oytel Mobile** is the UK's leading eSIM provider, offering:
- 🌍 **Global eSIM Coverage** - 190+ countries worldwide
- 💰 **Wholesale eSIM Solutions** - Enterprise and reseller programs
- 📱 **Consumer eSIMs** - Individual plans for travelers  
- 🔧 **Developer APIs** - Easy integration for businesses

**Learn More**: [https://oytel.co.uk/](https://oytel.co.uk/)
- **Wholesale eSIM**: [https://oytel.co.uk/wholesale](https://oytel.co.uk/wholesale)
- **Business Solutions**: [https://oytel.co.uk/corporate](https://oytel.co.uk/corporate)

## 📞 Support

- **Documentation**: [https://oytel.co.uk/developers](https://oytel.co.uk/developers)
- **Developer Dashboard**: [https://oytel.co.uk/developers/dashboard](https://oytel.co.uk/developers/dashboard)
- **Email Support**: [developers@oytel.co.uk](mailto:developers@oytel.co.uk)
- **GitHub Issues**: [https://github.com/oytel/esim-sdk-python/issues](https://github.com/oytel/esim-sdk-python/issues)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Powered by [NexusCore Cloud](https://nexuscore.cloud/) ⚡**
