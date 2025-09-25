"""
FastAPI integration for AgentFlow streaming with AI-SDK compatibility.

This module provides FastAPI integration functions for streaming AgentFlow execution
with AI-SDK compatible event format using the clean NodeContext approach.
"""

from typing import AsyncGenerator, Dict, Any, Optional
import traceback

from .streaming_flow import StreamingFlow, stream_flow_execution_sse
from .ai_sdk_events import format_ai_sdk_sse_event, create_done_event, AiSdkEvent


async def agent_flow_ai_sdk_streamer(
    flow: Any,
    shared: Dict[str, Any],
    **kwargs: Any,
) -> AsyncGenerator[str, None]:
    """
    Stream AgentFlow execution with AI-SDK compatible SSE format.

    This function executes an AgentFlow and yields Server-Sent Events (SSE)
    formatted strings compatible with AI-SDK frontend libraries.

    Args:
        flow: AgentFlow instance to execute
        shared: Shared state dictionary for the flow
        **kwargs: Additional parameters (for future extensibility)

    Yields:
        SSE-formatted strings in AI-SDK compatible format

    Example:
        ```python
        async def fastapi_endpoint():
            flow = AgentFlow()
            shared = {"messages": messages}

            return StreamingResponse(
                agent_flow_ai_sdk_streamer(flow, shared),
                media_type="text/event-stream"
            )
        ```
    """
    try:
        # Check if flow has native streaming support
        if hasattr(flow, 'run_stream_sse'):
            # Use native streaming method
            async for sse_event in flow.run_stream_sse(shared):
                yield sse_event
        else:
            # Wrap with StreamingFlow
            async for sse_event in stream_flow_execution_sse(flow, shared):
                yield sse_event

    except Exception as e:
        # Log the full traceback for debugging
        traceback.print_exc(limit=3)

        # Create error event in AI-SDK format
        error_event = AiSdkEvent(
            type="error",
            data={
                "error": str(e),
                "type": type(e).__name__
            }
        )
        yield format_ai_sdk_sse_event(error_event)

        # End with DONE
        yield create_done_event()


async def agent_flow_simple_streamer(
    flow: Any,
    shared: Dict[str, Any],
    **kwargs: Any,
) -> AsyncGenerator[Dict[str, Any], None]:
    """
    Stream AgentFlow execution with simple event objects.

    This function executes an AgentFlow and yields simple event dictionaries
    without SSE formatting, useful for direct API consumption or testing.

    Args:
        flow: AgentFlow instance to execute
        shared: Shared state dictionary for the flow
        **kwargs: Additional parameters (for future extensibility)

    Yields:
        Event dictionaries in AI-SDK compatible format

    Example:
        ```python
        async def api_endpoint():
            flow = AgentFlow()
            shared = {"messages": messages}

            events = []
            async for event in agent_flow_simple_streamer(flow, shared):
                events.append(event)

            return {"events": events}
        ```
    """
    try:
        # Check if flow has native streaming support
        if hasattr(flow, 'run_stream'):
            # Use native streaming method
            async for event in flow.run_stream(shared):
                yield event.to_dict()
        else:
            # Wrap with StreamingFlow
            wrapper = StreamingFlow(flow)
            async for event in wrapper.run_stream(shared):
                yield event.to_dict()

    except Exception as e:
        # Yield error event
        yield {
            "type": "error",
            "error": str(e),
            "error_type": type(e).__name__
        }


class FlowStreamingManager:
    """
    Manager for handling multiple concurrent flow streaming sessions.

    This class can be used to manage multiple AgentFlow streaming sessions
    in FastAPI applications with proper resource cleanup.
    """

    def __init__(self):
        self.active_streams: Dict[str, Any] = {}

    async def start_flow_stream(
        self,
        session_id: str,
        flow: Any,
        shared: Dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        """
        Start a managed flow streaming session.

        Args:
            session_id: Unique identifier for the streaming session
            flow: AgentFlow instance to execute
            shared: Shared state dictionary for the flow

        Yields:
            SSE-formatted strings in AI-SDK compatible format
        """
        try:
            # Store session
            self.active_streams[session_id] = {
                "flow": flow,
                "shared": shared,
                "status": "running"
            }

            # Stream events
            async for event in agent_flow_ai_sdk_streamer(flow, shared):
                # Check if session was cancelled
                if session_id not in self.active_streams:
                    break

                yield event

        finally:
            # Clean up session
            if session_id in self.active_streams:
                self.active_streams[session_id]["status"] = "completed"
                del self.active_streams[session_id]

    def cancel_stream(self, session_id: str) -> bool:
        """
        Cancel an active streaming session.

        Args:
            session_id: Session identifier to cancel

        Returns:
            True if session was cancelled, False if not found
        """
        if session_id in self.active_streams:
            del self.active_streams[session_id]
            return True
        return False

    def get_stream_status(self, session_id: str) -> Optional[str]:
        """
        Get the status of a streaming session.

        Args:
            session_id: Session identifier to check

        Returns:
            Status string or None if not found
        """
        session = self.active_streams.get(session_id)
        return session["status"] if session else None

    def list_active_streams(self) -> Dict[str, Dict[str, Any]]:
        """
        List all active streaming sessions.

        Returns:
            Dictionary of session_id -> session_info
        """
        return {
            session_id: {
                "status": session["status"],
                "flow_type": type(session["flow"]).__name__
            }
            for session_id, session in self.active_streams.items()
        }


# Global streaming manager instance
flow_streaming_manager = FlowStreamingManager()


# Convenience functions for FastAPI route integration
def create_flow_streaming_response(flow: Any, shared: Dict[str, Any]):
    """
    Create a FastAPI StreamingResponse for AgentFlow execution.

    Args:
        flow: AgentFlow instance to execute
        shared: Shared state dictionary for the flow

    Returns:
        FastAPI StreamingResponse with AI-SDK compatible events

    Example:
        ```python
        from fastapi import FastAPI
        from fastapi.responses import StreamingResponse

        app = FastAPI()

        @app.post("/agent-flow/stream")
        async def stream_agent_flow(request: FlowRequest):
            flow = AgentFlow()
            shared = {"messages": request.messages}

            return create_flow_streaming_response(flow, shared)
        ```
    """
    from fastapi.responses import StreamingResponse

    return StreamingResponse(
        agent_flow_ai_sdk_streamer(flow, shared),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # Disable nginx buffering
        }
    )


async def create_managed_flow_streaming_response(
    session_id: str,
    flow: Any,
    shared: Dict[str, Any]
):
    """
    Create a managed FastAPI StreamingResponse for AgentFlow execution.

    Args:
        session_id: Unique session identifier
        flow: AgentFlow instance to execute
        shared: Shared state dictionary for the flow

    Returns:
        FastAPI StreamingResponse with session management

    Example:
        ```python
        @app.post("/agent-flow/stream/{session_id}")
        async def stream_agent_flow_managed(session_id: str, request: FlowRequest):
            flow = AgentFlow()
            shared = {"messages": request.messages}

            return await create_managed_flow_streaming_response(session_id, flow, shared)
        ```
    """
    from fastapi.responses import StreamingResponse

    return StreamingResponse(
        flow_streaming_manager.start_flow_stream(session_id, flow, shared),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )