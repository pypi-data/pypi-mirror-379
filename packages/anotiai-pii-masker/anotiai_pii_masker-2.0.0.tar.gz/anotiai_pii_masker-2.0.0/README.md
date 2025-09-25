# AnotiAI PII Masker - Cloud-Powered Privacy Protection

A lightweight Python package for detecting and masking personally identifiable information (PII) in text using cloud-based AI models with optional local fallback.

[![PyPI version](https://badge.fury.io/py/anotiai-pii-masker.svg)](https://badge.fury.io/py/anotiai-pii-masker)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **☁️ Cloud-Powered**: Uses state-of-the-art AI models hosted on RunPod for maximum accuracy
- **⚡ Lightning Fast**: ~2-3 seconds inference time (after model warm-up)
- **💡 Intelligent**: Combines multiple detection approaches (rule-based, ML, transformers)
- **🔄 Reversible**: Mask and unmask PII while preserving data structure
- **🛡️ Privacy-First**: No data storage - all processing is ephemeral
- **📦 Lightweight**: Minimal dependencies for cloud mode (~10MB vs ~5GB local)
- **🔧 Flexible**: Support for both cloud and local inference modes

## 🔧 Installation

### Cloud Mode (Recommended)
```bash
pip install anotiai-pii-masker
```

### Local Mode (Full Dependencies)
```bash
pip install anotiai-pii-masker[local]
```

### Development
```bash
pip install anotiai-pii-masker[dev]
```

## 🚀 Quick Start

### Cloud Inference (Default)

```python
from anotiai_pii_masker import WhosePIIGuardian

# Option 1: Direct API configuration
guardian = WhosePIIGuardian(
    api_key="your_runpod_api_key",
    endpoint_id="your_endpoint_id"
)

# Option 2: Environment variables (recommended)
import os
os.environ["ANOTIAI_API_KEY"] = "your_runpod_api_key"
os.environ["ANOTIAI_ENDPOINT_ID"] = "your_endpoint_id"

guardian = WhosePIIGuardian()

# Mask PII in text
text = "Hi, I'm John Doe and my email is john.doe@company.com"
masked_text, pii_map = guardian.mask_text(text)

print(f"Original: {text}")
print(f"Masked: {masked_text}")
# Output: "Hi, I'm [REDACTED_PERSON_1] and my email is [REDACTED_EMAIL_1]"

# Unmask when needed
original_text = guardian.unmask_text(masked_text, pii_map)
print(f"Unmasked: {original_text}")
```

### Local Inference (Fallback)

```python
# Requires pip install anotiai-pii-masker[local]
guardian = WhosePIIGuardian(local_mode=True)

# Same API as cloud mode
masked_text, pii_map = guardian.mask_text(text)
```

## 🔑 Getting API Credentials

1. Sign up at [RunPod](https://runpod.io/)
2. Get your API key from the dashboard
3. Use endpoint ID: `r2ol4vgslj001p` (AnotiAI public endpoint)
4. Set environment variables:
   ```bash
   export ANOTIAI_API_KEY="your_runpod_api_key"
   export ANOTIAI_ENDPOINT_ID="r2ol4vgslj001p"
   ```

## 📖 Advanced Usage

### Configuration File
```python
# Create ~/.anotiai/config.json
{
    "api_key": "your_key",
    "endpoint_id": "your_endpoint",
    "timeout": 60,
    "retry_attempts": 3
}

guardian = WhosePIIGuardian()  # Automatically loads config
```

### Detection Only
```python
# Get detected entities without masking
result = guardian.detect_pii(text)
print(f"Found {result['entities_found']} PII entities")

for token, entity in result['pii_map'].items():
    print(f"- {entity['label']}: {entity['value']} (confidence: {entity['confidence']})")
```

### Error Handling
```python
from anotiai_pii_masker import WhosePIIGuardian, APIError, NetworkError

try:
    guardian = WhosePIIGuardian()
    masked_text, pii_map = guardian.mask_text(text)
except APIError as e:
    print(f"API Error: {e}")
except NetworkError as e:
    print(f"Network Error: {e}")
```

### Health Check
```python
# Check if the service is healthy
health = guardian.health_check()
print(f"Service status: {health['status']}")
```

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │    │  anotiai-pii-    │    │   RunPod Cloud  │
│                 │───▶│     masker       │───▶│                 │
│ guardian.mask() │    │   (lightweight)  │    │ GPU Models      │
└─────────────────┘    └──────────────────┘    │ • DeBERTa       │
                                               │ • RoBERTa       │
                                               │ • Presidio      │
                                               │ • spaCy         │
                                               └─────────────────┘
```

## 📊 Supported PII Types

- **Personal**: Names, dates of birth, addresses
- **Contact**: Email addresses, phone numbers, URLs
- **Financial**: Credit card numbers, bank accounts
- **Government**: SSNs, passport numbers, license numbers
- **Healthcare**: Medical license numbers
- **Technical**: IP addresses, crypto addresses

## 🔒 Security & Privacy

- **No Data Storage**: All processing is ephemeral
- **Encrypted Transit**: HTTPS/TLS for all API communications
- **Reversible Masking**: Original data can be restored when needed
- **Configurable Thresholds**: Adjust sensitivity based on your needs

## 🚨 Migration from v1.x

Version 2.0 introduces cloud-first architecture. To migrate:

```python
# v1.x (local only)
from anotiai_pii_masker import WhosePIIGuardian
guardian = WhosePIIGuardian()

# v2.x (cloud-first with local fallback)
guardian = WhosePIIGuardian(
    api_key="your_key",
    endpoint_id="your_endpoint",
    local_fallback=True  # Falls back to v1.x behavior if cloud fails
)
```

## 📈 Performance

| Mode | Setup Time | Inference Time | Memory Usage | Accuracy |
|------|------------|----------------|--------------|----------|
| Cloud | ~1s | ~2-3s | ~50MB | 99.5% |
| Local | ~30s | ~5-10s | ~8GB | 99.5% |


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Documentation**: [GitHub README](https://github.com/anotiai/anotiai-pii-masker#readme)
- **Issues**: [GitHub Issues](https://github.com/anotiai/anotiai-pii-masker/issues)
- **Email**: emmanuel@anotiai.com

---

**Protect your users' privacy with AnotiAI PII Masker** 🛡️