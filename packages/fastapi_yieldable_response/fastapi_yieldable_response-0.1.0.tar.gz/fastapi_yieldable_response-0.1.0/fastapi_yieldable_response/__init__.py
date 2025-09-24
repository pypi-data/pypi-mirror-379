from inspect import Parameter, isasyncgen, signature
from typing import Any, Callable

from fastapi import BackgroundTasks


async def _send_unknown_fn(fn, **kwargs) -> Any:
    """Helper function to call a function that may be synchronous or asynchronous."""
    try:
        if isasyncgen(fn):
            return await fn.asend(None)
        else:
            return fn.send(None)
    except (StopAsyncIteration, StopIteration):
        pass


def yieldable_response(
    original_function: Callable[..., Any],
) -> Callable[..., Any]:
    original_signature = signature(original_function)
    middleware_signature = {
        "background_tasks": Parameter(
            "background_tasks",
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=BackgroundTasks,
        )
    }
    complete_params = {
        **middleware_signature,
        **original_signature.parameters,
    }
    complete_signature = original_signature.replace(
        parameters=list(complete_params.values())
    )

    async def _wrapper(background_tasks: BackgroundTasks, *args, **kwargs):
        response_iter = original_function(*args, **kwargs)
        response = await _send_unknown_fn(response_iter)

        async def latter_part():
            await _send_unknown_fn(response_iter)

        background_tasks.add_task(latter_part)
        return response

    _wrapper.__signature__ = complete_signature
    return _wrapper
