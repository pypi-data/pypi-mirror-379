# API Validator SDK

Enterprise-grade API request validation using adaptive scoring algorithms. Replace complex if/else chains with intelligent, maintainable validation rules.

## Installation

```bash
pip install api-validator-sdk

# For optimized performance (requires C++ compiler)
pip install api-validator-sdk[optimized]
```

## Quick Start

### Community Edition (Free)
```python
from api_validator import APIValidator

validator = APIValidator()

request = {
    'auth_token_present': True,
    'token_age_minutes': 10,
    'user_verified': True,
    'requests_per_minute': 25,
    'payload_size_kb': 800,
    'ip_reputation_score': 85
}

result = validator.validate_request(request)
print(f"Valid: {result.is_valid} | Score: {result.score:.3f}")
```

### Professional Edition
```python
validator = APIValidator(
    tier='professional',
    license_key='PRO-2026-12-31-XXXX-XXXX'
)

# Batch validation
results = validator.validate_batch(requests)

# DataFrame support
results = validator.validate_dataframe(df)

# Access metrics
metrics = validator.get_metrics()
print(f"Adaptive threshold: {metrics.current_threshold:.3f}")
```

### Enterprise Edition
```python
validator = APIValidator(
    tier='enterprise', 
    license_key='ENT-2026-12-31-XXXX-XXXX'
)

# Adjust weight optimization
validator.set_adjustment_factor(0.4)  # 60% expert, 40% algorithm

# Get weight evolution metrics
metrics = validator.get_metrics()
print(f"Weight changes: {metrics.weight_changes}")
```

## Tier Comparison

| Feature                 | Community  |      Professional       |        Enterprise       |
|-------------------------|------------|-------------------------|-------------------------|
| **Validations/month**   | Unlimited* |       Unlimited         |         Unlimited       |
| **Data formats**        | Dict only  | Dict, DataFrame, Series | Dict, DataFrame, Series |
| **Batch processing**    |     ❌     |          ✅            |           ✅            |
| **Adaptive threshold**  |     ❌     |          ✅            |           ✅            |
| **Weight optimization** |     ❌     |          ❌            |           ✅            |
| **Performance metrics** |     ❌     |          ✅            |           ✅ Enhanced   |
| **Adjustment factor**   |     ❌     |          ❌            |           ✅            |
| **Rate limits**         |    60/min  |        200/min          |        1000/min         |
| **Support**             |  Community |         Email           |        Priority         |
| **Price**               |    Free    |       $299/month        |      Contact sales      |

*Community tier free for evaluation. Production use requires registration.

## Core Features

### Authentication Validation
```python
auth_valid, score = validator.check_auth({
    'token_present': True,
    'token_age_minutes': 5,
    'user_verified': True
})
```

### Rate Limiting
```python
within_limits, score = validator.check_rate_limit({
    'requests_per_minute': 45,
    'daily_requests': 2000
})
```

### Risk Assessment
```python
risk_score = validator.calculate_risk_score({
    'ip_reputation_score': 30,
    'failed_attempts': 5,
    'suspicious_patterns': True
})
```

### Security Modes
```python
validator.adjust_sensitivity('strict')  # relaxed/normal/strict/lockdown
```

## Custom Validation Rules

```python
from api_validator import Field

custom_fields = [
    Field('api_version', '2.0', importance=3.0, sensitivity=4.0),
    Field('client_id', 'valid_client', importance=5.0, sensitivity=5.0)
]

validator = APIValidator(
    custom_fields=custom_fields,
    tier='professional',
    license_key='your-license-key'
)
```

## Predefined Configurations

```python
from api_validator import FieldPresets

# Public API endpoints
validator = APIValidator(
    custom_fields=FieldPresets.public_api()
)

# Webhook validation
validator = APIValidator(
    custom_fields=FieldPresets.webhook()
)

# GraphQL endpoints
validator = APIValidator(
    custom_fields=FieldPresets.graphql()
)
```

## Performance

| Metric           |  Community   | Professional |  Enterprise  |
|------------------|--------------|--------------|--------------|
| Validations/sec  |   ~20,000    |    ~50,000   |   ~100,000   |
| Memory usage     |    <10MB     |     <15MB    |    <20MB     |
| Latency          |   ~0.05ms    |     ~0.02ms  |   ~0.01ms    |

## API Reference

### APIValidator

**Initialization:**
```python
APIValidator(
    custom_fields=None,
    use_standard_fields=True,
    confidence_level=0.65,
    tier='community',
    license_key=None
)
```

**Methods:**
- `validate_request(request)` - Single validation
- `validate_batch(requests)` - Batch validation (Pro/Ent)
- `validate_dataframe(df)` - DataFrame rows (Pro/Ent)
- `check_auth(token_data)` - Authentication check
- `check_rate_limit(usage_data)` - Rate limit check
- `validate_payload(payload_data)` - Payload validation
- `check_permissions(user_role, endpoint, method)` - Authorization
- `calculate_risk_score(metadata)` - Risk assessment
- `adjust_sensitivity(mode)` - Change strictness
- `set_adjustment_factor(factor)` - Weight calibration (Ent)
- `get_metrics()` - Performance stats (Pro/Ent)
- `get_tier_info()` - Current tier features

### Field

```python
Field(
    name='field_name',
    reference=expected_value,
    importance=1.0,  # 1.0-5.0
    sensitivity=1.5   # 1.0-5.0
)
```

## Licensing

**Professional:** $299/month or $2,999/year
**Enterprise:** Contact sales@apivalidator.ai

**License format:**
- Professional: `PRO-YYYY-MM-DD-XXXX-XXXX`
- Enterprise: `ENT-YYYY-MM-DD-XXXX-XXXX`

## Support

- **Community:** GitHub issues
- **Professional:** support@apivalidator.ai (48h response)
- **Enterprise:** priority@apivalidator.ai (4h response)

## License

MIT for Community Edition. Commercial license for Professional/Enterprise.

© 2025 API Validator. Powered by Adaptive Formula technology.