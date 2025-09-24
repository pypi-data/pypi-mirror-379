# HLA-Compass Python SDK

[![PyPI version](https://badge.fury.io/py/hla-compass.svg)](https://badge.fury.io/py/hla-compass)
[![Python Versions](https://img.shields.io/pypi/pyversions/hla-compass.svg)](https://pypi.org/project/hla-compass/)
[![Downloads](https://pepy.tech/badge/hla-compass)](https://pepy.tech/project/hla-compass)

The official Python SDK for developing modules on the HLA-Compass platform.

## Requirements

- Python 3.8 or higher (3.8, 3.9, 3.10, 3.11, 3.12, 3.13 supported)
- pip package manager

## Installation

### Install from PyPI (Recommended)

```bash
pip install hla-compass
```

For development tools:
```bash
pip install hla-compass[dev]
```

For data export features (DataFrame/Excel support):
```bash
pip install hla-compass[data]
```

For machine learning modules:
```bash
pip install hla-compass[ml]
```

### Install from Source (Latest Development Version)

```bash
# Clone the repository
git clone https://github.com/AlitheaBio/HLA-Compass-platform.git
cd HLA-Compass-platform/sdk/python

# Install in development mode
pip install -e .
```

## Quick Start

```bash
# Install SDK
pip install hla-compass

# Create module
hla-compass init my-module --template no-ui --compute lambda

# Test locally
cd my-module
hla-compass test --local

# Build package
hla-compass build
```

📚 **For complete development guide, see: [/docs/MODULE_DEVELOPMENT_GUIDE.md](https://github.com/AlitheaBio/HLA-Compass-platform/blob/main/docs/MODULE_DEVELOPMENT_GUIDE.md)**

## Quick Start Workflow

The fastest path from blank slate to a published module:

```bash
# 1. Authenticate against the platform environment you plan to target
hla-compass auth login --env dev

# 2. Generate local SDK config, signing keys, and defaults
hla-compass configure

# 3. Scaffold a module interactively (prompts choose template/type)
hla-compass init -i

# 4. Run the hot-reload dev server (add --verbose to stream webpack logs)
cd <your-module>
hla-compass dev [--verbose]

# 5. Publish a signed build to the platform
hla-compass publish --env dev
```

Need the full tour (module APIs, deployment pipelines, best practices)? See [/docs/MODULE_DEVELOPMENT_GUIDE.md](https://github.com/AlitheaBio/HLA-Compass-platform/blob/main/docs/MODULE_DEVELOPMENT_GUIDE.md).

> Tip: `hla-compass dev` starts quietly by default. Use `--verbose` when you need webpack dev-server output (e.g., debugging frontend build failures).

## CLI Commands

### Module Management

```bash
# Create new module
hla-compass init <name> [options]
# Options: --yes (skip prompts), --template, --type, --compute

# Validate module structure
hla-compass validate [--json]  # --json for machine-readable output

# Test module (auto-detects local vs remote based on auth)
hla-compass test [--input FILE] [--verbose]

# Test locally without API
hla-compass test --local [--input FILE]

# Test against real API (requires auth)
# Note: Remote mode currently executes locally with API authentication context
# Full remote execution on the platform is on the roadmap
hla-compass test --remote [--input FILE]

# Output as JSON for CI/automation
hla-compass test --json [--input FILE]

# Package signing
hla-compass sign <package-file>

# Deploy module
hla-compass deploy <package-file> [--env ENV]

# List deployed modules
hla-compass list [--env ENV]
```

### Development Server

```bash
# Offline dev server (quiet by default)
hla-compass dev

# Stream webpack/aiohttp logs
hla-compass dev --verbose

# Proxy selected routes to the live API (read-only by default)
hla-compass dev --online --env dev --proxy-routes=auth,data

# Serve UI bundle from a custom webpack port
hla-compass dev --frontend-port 3100
```

### Authentication

```bash
# Login to platform
hla-compass auth login --env dev

# Logout
hla-compass auth logout

# Register as a developer (self-service)
hla-compass auth register [--env ENV]
```

## CLI Feature Matrix

| Command | Description | Status |
|---|---|---|
| `hla-compass configure` | Initialize SDK config and signing keys | Available |
| `hla-compass init` | Scaffold a new module from templates | Available |
| `hla-compass validate` | Validate module structure and manifest | Available |
| `hla-compass test --local` | Run module locally without API | Available |
| `hla-compass test --remote` | Run locally with API auth context | Available (executes locally) |
| `hla-compass auth login/logout/register` | Authentication flows | Available |
| `hla-compass build` | Build package; signs manifest by default | Available |
| `hla-compass sign` | Sign an existing package/directory | Available |
| `hla-compass publish` | Build/sign and publish to platform | Available |
| `hla-compass deploy` | Deploy published module to environment | Available |
| `hla-compass list` | List deployed modules | Available |
| `hla-compass test` | Test module execution (local/remote) | Available |
| `hla-compass templates list` | List module templates | Planned |
| `hla-compass local-services` | Start local DB/S3 dev services | Planned |

Notes:
- `--remote` test currently executes locally with API authentication context; full remote execution is on the roadmap.
- For end-to-end deployments, prefer the `publish` path integrated with the platform pipelines.

## Testing

### Unit Testing

```python
# tests/test_module.py
import pytest
from hla_compass.testing import ModuleTester, MockContext

def test_module_execution():
    tester = ModuleTester()
    
    input_data = {
        'sequence': 'MLLSVPLLL',
        'threshold': 0.5
    }
    
    result = tester.test_local(
        'backend/main.py',
        input_data
    )
    
    assert result['status'] == 'success'
    assert len(result['results']) > 0
```

### Integration Testing

```python
# Test with mock API data
def test_with_mock_data():
    context = MockContext.create(
        api_data={
            'peptides': [
                {'id': '1', 'sequence': 'MLLSVPLLL'},
                {'id': '2', 'sequence': 'SIINFEKL'}
            ]
        }
    )
    
    result = tester.test_local(
        'backend/main.py',
        {'min_length': 8},
        context
    )
    
    assert len(result['results']) == 2
```

Need to exercise the devkit container or real S3/MinIO buckets? Opt in explicitly so tests don’t accidentally touch production services:

```python
tester.configure_local_devkit(use_real_storage=True)
context = MockContext.create(use_devkit=True, use_real_storage=True)
```

### Performance Testing

```python
# Benchmark module performance
def test_performance():
    tester = ModuleTester()
    
    results = tester.benchmark(
        'backend/main.py',
        input_data,
        iterations=100
    )
    
    assert results['average_time'] < 0.1  # 100ms
```

## Advanced Features

### Module Types

#### Lambda Modules (Quick Analysis)
- Execution time: <15 minutes
- Memory: 128MB - 10GB
- Best for: Simple calculations, data filtering

#### Fargate Modules (Long Running)
- Execution time: <8 hours
- Memory: 512MB - 30GB
- Best for: Complex pipelines, batch processing

#### SageMaker Modules (ML Inference)
- GPU support available
- Pre-trained model hosting
- Best for: Machine learning predictions

### UI Module Bundles

UI-capable modules ship a React bundle the platform loads dynamically. Keep the generated webpack configuration’s `ModuleUI` UMD export intact so the host application can mount your UI. When running `hla-compass dev`, pass `--verbose` to stream webpack output if the UI fails to load (helpful for diagnosing “ModuleUI UMD not found” and other build issues).

### Custom Validation

```python
class MyModule(Module):
    def validate_inputs(self, input_data):
        # Call parent validation
        validated = super().validate_inputs(input_data)
        
        # Custom validation
        sequence = validated.get('sequence', '')
        if not all(aa in 'ACDEFGHIKLMNPQRSTVWY' for aa in sequence):
            raise ValidationError("Invalid amino acids in sequence")
        
        return validated
```

## Best Practices

1. **Input Validation**: Always validate inputs thoroughly
2. **Error Handling**: Use try-except blocks and provide clear error messages
3. **Logging**: Use appropriate logging levels (debug, info, warning, error)
4. **Performance**: Process data in batches when possible
5. **Memory**: Stream large results instead of loading all into memory
6. **Security**: Never hardcode credentials or sensitive data
7. **Testing**: Write comprehensive tests for all functionality
8. **Documentation**: Document inputs, outputs, and algorithms clearly

## Environment Variables

- `HLA_COMPASS_ENV`: Default environment (dev, staging, prod) - takes precedence over HLA_ENV
- `HLA_ENV`: Alternative environment variable (used if HLA_COMPASS_ENV not set)
- `HLA_COMPASS_CONFIG_DIR`: Configuration directory (default: ~/.hla-compass)
- `HLA_COMPASS_LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `HLA_CORRELATION_ID`: Optional global correlation ID propagated as `X-Correlation-Id`

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are in requirements.txt
2. **Timeout Errors**: Increase timeout in manifest.json or optimize code
3. **Memory Errors**: Process data in smaller chunks or increase memory
4. **Authentication Errors**: Run `hla-compass auth login` to refresh tokens

### Debug Mode

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Request Headers & Tracing

The SDK standardizes outbound request headers and retry behavior.

- Accept: Always `application/json` (session default)
- User-Agent: `hla-compass-sdk/<version> python/<version> os/<platform>`
- Content-Type: `application/json` for JSON requests (per-call)
- X-Request-Id: Unique UUID per HTTP attempt (changes on retry)
- X-Correlation-Id: Optional global correlation ID for cross-service tracing
  - Set environment variable `HLA_CORRELATION_ID` to propagate a stable value
  - Added to both SDK auth requests and APIClient requests
- Idempotency-Key: Added to POST requests to make retries safe
  - A stable UUID is generated per SDK call and reused across retry attempts
  - Server-side should de-duplicate requests using this key

### Retry Policy

- GET/HEAD/OPTIONS: Retries enabled (connection/read) with exponential backoff via `urllib3.Retry`
- 401 Unauthorized: One automatic token refresh (`Auth.refresh_token`) and retry
- 429 Too Many Requests: Honors `Retry-After` (falls back to exponential backoff)
- 5xx Server Errors: Exponential backoff; for POST, retries only when an `Idempotency-Key` is present (the SDK adds one per call)
- Timeouts/Network errors: Limited retries with backoff for transient connection issues

Tip: For end-to-end traceability, set `HLA_CORRELATION_ID` in your environment and pass it across your systems.

## Deployment Note: SimpleDeployer (Deprecated / Dev-only)

The legacy `hla_compass.deployer.SimpleDeployer` utility is disabled by default and intended only for local development experiments. It bypasses platform authentication and infrastructure pipelines.

- Disabled by default; to enable explicitly set `HLA_ENABLE_SIMPLE_DEPLOYER=1`.
- Recommended path: use `hla-compass build` + `hla-compass publish/deploy` and the platform’s Serverless/Terraform pipelines.

## Support

- **Complete Guide**: [/docs/MODULE_DEVELOPMENT_GUIDE.md](https://github.com/AlitheaBio/HLA-Compass-platform/blob/main/docs/MODULE_DEVELOPMENT_GUIDE.md)
- **Examples**: [/modules/examples/](https://github.com/AlitheaBio/HLA-Compass-platform/tree/main/modules/examples)
- **Issues**: [GitHub Issues](https://github.com/AlitheaBio/HLA-Compass-platform/issues)
- **Quick Start**: [/docs/MODULE_DEVELOPMENT_GUIDE.md#quick-start](https://github.com/AlitheaBio/HLA-Compass-platform/blob/main/docs/MODULE_DEVELOPMENT_GUIDE.md#quick-start)

## License

Copyright © 2024 Alithea Bio. All rights reserved.
