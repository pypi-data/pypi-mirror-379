# FastAPI Yieldable Response

A middleware for FastAPI that sends early responses from route handlers.

## Overview

FastAPI Yieldable Response allows you to send immediate responses to clients while continuing to execute background processing in your route handlers. This is particularly useful when you want to:

- Send quick acknowledgments to clients before performing time-consuming operations
- Improve perceived response times by returning data immediately
- Execute cleanup or logging tasks after the response has been sent

## Installation

```bash
pip install fastapi_yieldable_response
```

## Quick Start

```python
from fastapi import FastAPI
from fastapi_yieldable_response import yieldable_response

app = FastAPI()

@app.get("/")
@yieldable_response
async def root():
    # This response is sent immediately to the client
    yield {"message": "Hello!"}
    
    # This code runs in the background after the response is sent
    import time
    time.sleep(2)
    print("Background task completed!")
```

## How It Works

The `@yieldable_response` decorator transforms your route handler into a function that:

1. **Immediate Response**: The first `yield` statement sends an immediate response to the client
2. **Background Execution**: Any code after the `yield` continues executing as a background task
3. **Automatic Cleanup**: Uses FastAPI's `BackgroundTasks` to ensure proper resource management

## Features

-  **Zero Dependencies**: Only requires FastAPI (no additional dependencies)
-  **Async/Sync Support**: Works with both async and sync route handlers
-  **Type Safety**: Maintains original function signatures and type hints
-  **FastAPI Integration**: Uses FastAPI's built-in `BackgroundTasks` system
-  **Simple API**: Just add the decorator to your existing routes

## Usage Examples

### Async Route Handler

```python
@app.get("/async-example")
@yieldable_response
async def async_example():
    yield {"status": "processing", "id": 123}
    
    # Background processing
    await some_async_operation()
    await send_notification()
```

### Sync Route Handler

```python
@app.get("/sync-example/{item_id}")
@yieldable_response
def sync_example(item_id: str):
    yield {"message": f"Processing item {item_id}"}
    
    # Background processing
    process_item(item_id)
    log_operation(item_id)
```

### With Path Parameters

```python
@app.get("/users/{user_id}")
@yieldable_response
async def get_user(user_id: int):
    # Send immediate response
    yield {"user_id": user_id, "status": "found"}
    
    # Log access in background
    await log_user_access(user_id)
    await update_analytics(user_id)
```

## Requirements

- Python 3.10+
- FastAPI 0.68.0+

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Repository

- **Homepage**: <https://github.com/lucamattiazzi/fastapi_yieldable_response>
- **Issues**: <https://github.com/lucamattiazzi/fastapi_yieldable_response/issues>
