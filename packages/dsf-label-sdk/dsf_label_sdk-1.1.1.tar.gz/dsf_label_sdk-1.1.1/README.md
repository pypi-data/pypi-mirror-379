# README.md
"""
# DSF Label SDK

Professional Python SDK for the DSF Label Adaptive Formula API.

## Installation

```bash
pip install dsf-label-sdk
```

## Quick Start

```python
from dsf_label_sdk import LabelSDK

# Community tier (free)
sdk = LabelSDK()

# Evaluate data
result = sdk.evaluate(
    data={'temperature': 25, 'pressure': 1.0},
    config={
        'temperature': {'default': 20, 'weight': 1.0, 'criticality': 1.5},
        'pressure': {'default': 1.0, 'weight': 0.8, 'criticality': 1.2}
    }
)

print(f"Score: {result.score:.2f}")
print(f"Above threshold: {result.is_above_threshold}")
```

## Professional & Enterprise Tiers

```python
# Initialize with license
sdk = LabelSDK(
    license_key='PRO-2026-12-31-XXXX-XXXX',
    tier='professional'
)

# Batch evaluation (premium feature)
results = sdk.batch_evaluate(
    data_points=[
        {'temperature': 25, 'pressure': 1.0},
        {'temperature': 22, 'pressure': 0.9},
    ],
    config=config
)

# Get performance metrics
metrics = sdk.get_metrics()
print(f"Average score: {metrics['avg_score']:.3f}")
```

## Using the Config Builder

```python
from dsf_label_sdk import LabelSDK

sdk = LabelSDK()

# Build configuration fluently
config = (sdk.create_config()
    .add_field('temperature', default=20, weight=1.0, criticality=1.5)
    .add_field('pressure', default=1.0, weight=0.8)
    .add_field('humidity', default=0.5, weight=0.6)
)

result = sdk.evaluate(data, config)
```

## Context Manager

```python
with LabelSDK(license_key='...', tier='enterprise') as sdk:
    result = sdk.evaluate(data, config)
    # Connection automatically cleaned up
```

## Error Handling

```python
from dsf_label_sdk import LabelSDK, LicenseError, ValidationError

try:
    sdk = LabelSDK(license_key='invalid', tier='professional')
    result = sdk.evaluate(data, config)
except LicenseError as e:
    print(f"License error: {e}")
except ValidationError as e:
    print(f"Invalid input: {e}")
```

## Features by Tier

| Feature             | Community | Professional | Enterprise |
|---------------------|-----------|--------------|------------|
| Single evaluation   |     ✅    |      ✅     |     ✅     |
| Batch evaluation    |     ❌    |      ✅     |     ✅     |
| Performance metrics |     ❌    |      ✅     |     ✅     |
| ML optimization     |     ❌    |      ✅     |     ✅     |
| Weight calibration  |     ❌    |      ❌     |     ✅     |
| Adaptive thresholds |     ❌    |      ✅     |     ✅     |

## License

MIT License - see LICENSE file for details.
"""