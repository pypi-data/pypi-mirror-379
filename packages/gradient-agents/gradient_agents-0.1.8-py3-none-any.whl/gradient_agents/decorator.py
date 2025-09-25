"""
Gradient entrypoint decorator for creating FastAPI agents.

Simple decorator that wraps a function with FastAPI endpoints.
"""

from __future__ import annotations
import inspect
from typing import Callable
from fastapi import FastAPI, HTTPException, Request
import uvicorn

from .runtime.manager import get_runtime_manager
from .runtime.context import get_current_context


def entrypoint(func: Callable) -> Callable:
    """
    Decorator that creates a FastAPI app from a function and automatically
    makes it available as 'app' in the module.

    The decorated function must accept exactly 2 parameters:
    1. data: The request data (dict)
    2. context: The request context object

    Example:
        @entrypoint
        def my_agent(data, context):
            return {"message": "Hello", "data": data}

        # Now 'app' is automatically available for uvicorn:
        # uvicorn main:app
    """
    # Validate that the function has exactly 2 parameters
    sig = inspect.signature(func)
    params = list(sig.parameters.keys())
    if len(params) != 2:
        raise ValueError(
            f"Entrypoint function '{func.__name__}' must have exactly 2 parameters (data, context), "
            f"but has {len(params)}: {params}"
        )

    # Create FastAPI app
    fastapi_app = FastAPI(
        title=f"Gradient Agent - {func.__name__}",
        description=f"AI Agent powered by Gradient - {func.__doc__ or 'No description'}",
        version="1.0.0",
    )

    @fastapi_app.post("/completions", response_model=None)
    async def completions(req: Request):
        runtime_manager = get_runtime_manager()
        try:
            # Get raw JSON body
            try:
                body = await req.json()
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid JSON: {e}")

            context = get_current_context()

            # Call the user's function
            result = await runtime_manager.run_entrypoint(func, body, context)
            return result

        except Exception as e:
            print(f"Error in entrypoint: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")

    @fastapi_app.get("/health")
    async def health():
        """Health check endpoint."""
        return {"status": "healthy", "entrypoint": func.__name__}

    # Automatically inject 'app' into the module where this function is defined
    import sys

    frame = sys._getframe(1)  # Get the calling frame (where @entrypoint was used)
    module_globals = frame.f_globals
    module_globals["app"] = fastapi_app

    # Return the original function (so the user can still call it if needed)
    return func


def run_server(app: FastAPI, host: str = "0.0.0.0", port: int = 8080, **kwargs):
    """
    Run a FastAPI server.

    Args:
        app: The FastAPI app to run
        host: Host to bind to
        port: Port to bind to
        **kwargs: Additional arguments to pass to uvicorn.run()
    """
    uvicorn.run(app, host=host, port=port, **kwargs)
