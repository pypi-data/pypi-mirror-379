# Lens Reasoning SDK

A Python SDK for the Lens Reasoning System that provides query processing and reasoning capabilities.

## Installation

```bash
# Install from PyPI
pip install lens-reasoning-sdk

# Or install from source
cd /path/to/lens-sdk
pip install -e .
```

## Prerequisites

- Python 3.8+
- Internet access to the Lens Reasoning System production API (`https://api.tupl.xyz`)

## Quick Start

```python
from query_processor import LensQueryProcessor
from exceptions import ProcessingError

try:
    # Initialize the query processor
    processor = LensQueryProcessor("https://api.tupl.xyz")

    # Process a query
    result = processor.process_query("What are the implications of AI in healthcare?")

    print(f"Answer: {result['final_answer']}")
    print(f"Confidence: {result['confidence_overall']}")
    print(f"Contract ID: {result['contract_id']}")

except ProcessingError as e:
    print(f"Processing failed: {e}")
finally:
    processor.close()
```

## Available Methods

- `process_query(query, **kwargs)` - Process a query through the reasoning system
- `get_contract(contract_id)` - Get complete contract details
- `get_reasoning_trace(contract_id)` - Get detailed reasoning trace
- `list_contracts(workflow_id=None, limit=20)` - List existing contracts

## Requirements

- Python 3.8+
- httpx>=0.25.0
- pydantic>=2.0.0

## License

MIT License