"""
Streaming response utilities for Gradient agents.

Provides a clean abstraction for streaming responses without exposing FastAPI details.
"""

from typing import Iterator, AsyncIterator, Union, Dict, Any
import json


class StreamingResponse:
    """Gradient-specific streaming response wrapper.

    This abstracts away FastAPI's StreamingResponse and provides a clean
    interface for agents to return streaming data.
    """

    def __init__(
        self,
        content: Union[
            Iterator[str], AsyncIterator[str], Iterator[bytes], AsyncIterator[bytes]
        ],
        media_type: str = "text/plain",
        headers: Dict[str, str] = None,
    ):
        """Initialize streaming response.

        Args:
            content: Iterator or async iterator that yields string or bytes chunks
            media_type: MIME type for the response (default: text/plain)
            headers: Optional HTTP headers to include
        """
        self.content = content
        self.media_type = media_type
        self.headers = headers or {}

    def __repr__(self):
        return f"StreamingResponse(media_type='{self.media_type}')"


class JSONStreamingResponse(StreamingResponse):
    """Streaming response for JSON data chunks.

    Automatically formats each chunk as JSON and adds appropriate headers.
    """

    def __init__(
        self, content: Union[Iterator[Dict[str, Any]], AsyncIterator[Dict[str, Any]]]
    ):
        """Initialize JSON streaming response.

        Args:
            content: Iterator that yields dictionaries to be JSON-encoded
        """

        def json_generator():
            for chunk in content:
                yield json.dumps(chunk) + "\n"

        super().__init__(
            json_generator(),
            media_type="application/x-ndjson",  # Newline-delimited JSON
            headers={"Cache-Control": "no-cache"},
        )


class ServerSentEventsResponse(StreamingResponse):
    """Streaming response for Server-Sent Events (SSE).

    Formats data according to SSE specification.
    """

    def __init__(
        self, content: Union[Iterator[Dict[str, Any]], AsyncIterator[Dict[str, Any]]]
    ):
        """Initialize SSE streaming response.

        Args:
            content: Iterator that yields dictionaries to be sent as SSE events
        """

        def sse_generator():
            for chunk in content:
                yield f"data: {json.dumps(chunk)}\n\n"

        super().__init__(
            sse_generator(),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
        )


def stream_json(
    content: Union[Iterator[Dict[str, Any]], AsyncIterator[Dict[str, Any]]],
) -> JSONStreamingResponse:
    """Convenience function to create JSON streaming response.

    Args:
        content: Iterator that yields dictionaries

    Returns:
        JSONStreamingResponse instance
    """
    return JSONStreamingResponse(content)


def stream_events(
    content: Union[Iterator[Dict[str, Any]], AsyncIterator[Dict[str, Any]]],
) -> ServerSentEventsResponse:
    """Convenience function to create Server-Sent Events streaming response.

    Args:
        content: Iterator that yields dictionaries

    Returns:
        ServerSentEventsResponse instance
    """
    return ServerSentEventsResponse(content)
