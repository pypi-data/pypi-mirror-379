"""
Gradient entrypoint decorator for creating FastAPI agents.
"""

from __future__ import annotations
import inspect
from typing import Any, Callable, Optional
from fastapi import FastAPI, HTTPException, Request
import uvicorn

from .runtime.manager import get_runtime_manager
from .runtime.context import get_current_context


# Responses will be plain dict objects; no pydantic model or wrapper.


class EntrypointRegistry:
    """Global registry for entrypoint functions."""

    def __init__(self):
        self._function: Optional[Callable] = None
        self._app: Optional[FastAPI] = None

    def register(self, func: Callable) -> FastAPI:
        """Register an entrypoint function and create the FastAPI app."""
        # Validate that the function has exactly 2 parameters
        sig = inspect.signature(func)
        params = list(sig.parameters.keys())
        if len(params) != 2:
            raise ValueError(
                f"Entrypoint function '{func.__name__}' must have exactly 2 parameters (data, context), "
                f"but has {len(params)}: {params}"
            )

        self._function = func

        self._app = FastAPI(
            title="Gradient Agent",
            description="AI Agent powered by Gradient",
            version="1.0.0",
        )

        @self._app.post("/completions", response_model=None)
        async def completions(req: Request):
            runtime_manager = get_runtime_manager()
            try:
                # Get raw JSON body without any transformation
                try:
                    body = await req.json()
                except Exception:
                    body = {}

                runtime_manager.start_request(
                    entrypoint_name=func.__name__, inputs=body
                )

                # Call user function with data and context - user function must accept exactly 2 parameters
                try:
                    # Get the current context for the second parameter
                    context = get_current_context()
                    result = func(body, context)
                except Exception as e:
                    runtime_manager.end_request(error=str(e))
                    raise HTTPException(status_code=500, detail=str(e)) from e

                # Return result exactly as user provided it
                runtime_manager.end_request(outputs=result)
                return result
            except HTTPException:
                raise
            except Exception as e:
                runtime_manager.end_request(error=str(e))
                raise HTTPException(status_code=500, detail=str(e))

        @self._app.get("/health")
        async def health():
            return {"status": "healthy", "service": "gradient-agent"}

        @self._app.get("/")
        async def root():
            return {
                "service": "gradient-agent",
                "entrypoint": func.__name__ if func else None,
                "endpoints": ["/completions", "/health"],
            }

        return self._app

    def get_app(self) -> FastAPI:
        """Get the registered FastAPI app."""
        if self._app is None:
            raise RuntimeError(
                "No entrypoint function decorated. Use @entrypoint decorator first."
            )
        return self._app


# Global registry instance
_registry = EntrypointRegistry()


def entrypoint(func: Callable) -> Callable:
    """
    Decorator to mark a function as the agent entrypoint.

    The decorated function must accept exactly 2 parameters:
    1. data: The request data (dict)
    2. context: The request context object (can be named anything)

    Example:
        @entrypoint
        def my_agent(data, ctx):
            return f"Processing: {data}"

        @entrypoint
        def my_other_agent(request_data, request_context):
            return {"result": request_data["query"]}
    """
    # Register the function and create the app
    _registry.register(func)

    # Return the original function unchanged
    return func


def get_app() -> FastAPI:
    """Get the FastAPI app instance."""
    # If no app is registered, check if we should auto-import an entrypoint module
    # This happens when uvicorn uses this as a factory function with reload=True
    if _registry._app is None:
        import os

        entrypoint_module = os.environ.get("GRADIENT_ENTRYPOINT_MODULE")
        if entrypoint_module:
            try:
                import importlib
                import sys
                from pathlib import Path

                # Set up the environment for importing
                current_dir = str(Path.cwd())
                project_root = os.environ.get("GRADIENT_PROJECT_ROOT", current_dir)

                # Ensure project root is in sys.path (should be first)
                if project_root not in sys.path:
                    sys.path.insert(0, project_root)

                # Change to project root to help with relative imports
                original_cwd = os.getcwd()
                os.chdir(project_root)

                print(f"🔄 Auto-importing entrypoint module: {entrypoint_module}")
                print(f"📂 Project root: {project_root}")
                print(f"🐍 Python path: {sys.path[:3]}...")  # Show first 3 entries

                try:
                    # For dot-relative imports, we need to treat the module as part of a package
                    # Try different import strategies

                    # Strategy 1: Import as-is (works for absolute imports)
                    try:
                        importlib.import_module(entrypoint_module)
                        print(
                            f"✅ Successfully imported {entrypoint_module} (absolute)"
                        )
                    except (ImportError, ValueError) as e1:
                        print(f"❌ Absolute import failed: {e1}")

                        # Strategy 2: Try importing as __main__ (helps with relative imports)
                        try:
                            import runpy

                            module_path = (
                                Path(project_root)
                                / f"{entrypoint_module.replace('.', '/')}.py"
                            )
                            if module_path.exists():
                                print(f"🔄 Trying runpy.run_path: {module_path}")
                                runpy.run_path(str(module_path), run_name="__main__")
                                print(
                                    f"✅ Successfully executed {entrypoint_module} via runpy"
                                )
                            else:
                                raise ImportError(
                                    f"Module file not found: {module_path}"
                                )
                        except Exception as e2:
                            print(f"❌ runpy import failed: {e2}")

                            # Strategy 3: Manual file execution (last resort)
                            try:
                                module_path = (
                                    Path(project_root)
                                    / f"{entrypoint_module.replace('.', '/')}.py"
                                )
                                if module_path.exists():
                                    print(f"🔄 Trying manual execution: {module_path}")
                                    with open(module_path, "r") as f:
                                        code = f.read()

                                    # Create a module-like namespace
                                    module_globals = {
                                        "__name__": "__main__",
                                        "__file__": str(module_path),
                                        "__package__": None,
                                    }

                                    exec(code, module_globals)
                                    print(
                                        f"✅ Successfully executed {entrypoint_module} manually"
                                    )
                                else:
                                    raise ImportError(
                                        f"All import strategies failed for {entrypoint_module}"
                                    )
                            except Exception as e3:
                                print(f"❌ Manual execution failed: {e3}")
                                raise ImportError(
                                    f"All import strategies failed: {e1}, {e2}, {e3}"
                                )

                except Exception as final_error:
                    print(f"❌ Final import error: {final_error}")
                    raise
                finally:
                    # Always restore original working directory
                    os.chdir(original_cwd)

                # Now the registry should have the app
                if _registry._app is not None:
                    return _registry._app
            except Exception as e:
                print(
                    f"Failed to auto-import entrypoint module '{entrypoint_module}': {e}"
                )
                import traceback

                traceback.print_exc()

    return _registry.get_app()


def run_server(host: str = "0.0.0.0", port: int = 8080, **kwargs):
    """
    Run the FastAPI server with the decorated entrypoint.

    Args:
        host: Host to bind to
        port: Port to bind to
        **kwargs: Additional arguments to pass to uvicorn.run()
    """
    # If reload=True is passed, use import string + factory
    if kwargs.get("reload"):
        # figure out this module's import path
        import pathlib, sys

        module_name = pathlib.Path(__file__).stem  # e.g. "entrypoint"
        package = __package__  # e.g. "gradient"
        target = (
            f"{package}.{module_name}:get_app" if package else f"{module_name}:get_app"
        )

        uvicorn.run(
            target,
            host=host,
            port=port,
            factory=True,
            **kwargs,
        )
    else:
        app = get_app()
        uvicorn.run(app, host=host, port=port, **kwargs)
