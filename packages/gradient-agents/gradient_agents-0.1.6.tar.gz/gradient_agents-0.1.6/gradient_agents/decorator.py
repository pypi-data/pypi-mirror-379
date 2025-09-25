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


def entrypoint(func: Callable) -> FastAPI:
    """
    Decorator that converts a function into a FastAPI app.

    The decorated function must accept exactly 2 parameters:
    1. data: The request data (dict)
    2. context: The request context object

    Returns a FastAPI app that exposes the function at /completions

    Example:
        @entrypoint
        def my_agent(data, context):
            return {"message": "Hello", "data": data}

        # my_agent is now a FastAPI app
        # Run with: uvicorn main:my_agent
        # Or assign: app = my_agent
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
    app = FastAPI(
        title=f"Gradient Agent - {func.__name__}",
        description=f"AI Agent powered by Gradient - {func.__doc__ or 'No description'}",
        version="1.0.0",
    )

    @app.post("/completions", response_model=None)
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

    @app.get("/health")
    async def health():
        """Health check endpoint."""
        return {"status": "healthy", "entrypoint": func.__name__}

    # Return the FastAPI app directly
    return app


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
