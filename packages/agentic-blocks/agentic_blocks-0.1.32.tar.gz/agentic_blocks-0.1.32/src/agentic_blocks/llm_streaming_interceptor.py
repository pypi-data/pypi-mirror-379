"""
LLM streaming call interception utilities for AgentFlow.

This module provides utilities to intercept LLM streaming calls within PocketFlow nodes
without modifying the node interface, allowing flow-level event streaming.
"""

import asyncio
import threading
from typing import List, Iterator, Optional, Any, AsyncIterator, Union
from contextlib import contextmanager, asynccontextmanager
from queue import Queue, Empty
import inspect

from .llm_agno import (
    StreamEvent,
    StreamResponse,
    call_llm_stream,
    call_llm_stream_events,
    AssistantResponseEvent,
    ToolCallStartedEvent,
    ToolCallCompletedEvent,
    ModelResponseCompleteEvent,
)
from .ai_sdk_events import AiSdkEvent, StreamEventTransformer
from .messages import Messages


class StreamEventCollector:
    """Collects streaming events from intercepted LLM calls"""

    def __init__(self):
        self._events: Queue = Queue()
        self._active = False
        self._lock = threading.Lock()

    def start_collection(self):
        """Start collecting events"""
        with self._lock:
            self._active = True
            # Clear any previous events
            while not self._events.empty():
                try:
                    self._events.get_nowait()
                except Empty:
                    break

    def stop_collection(self):
        """Stop collecting events"""
        with self._lock:
            self._active = False

    def add_event(self, event: StreamEvent):
        """Add a streaming event to the collection"""
        with self._lock:
            if self._active:
                self._events.put(event)

    def get_events(self) -> List[StreamEvent]:
        """Get all collected events and clear the collection"""
        events = []
        while not self._events.empty():
            try:
                events.append(self._events.get_nowait())
            except Empty:
                break
        return events

    def has_events(self) -> bool:
        """Check if there are any collected events"""
        return not self._events.empty()


# Global event collector instance
_event_collector = StreamEventCollector()


class InterceptedStreamResponse:
    """Wrapper for StreamResponse that intercepts events"""

    def __init__(self, original_response: StreamResponse, collector: StreamEventCollector):
        self._original = original_response
        self._collector = collector
        self._cached_tool_calls = None

    def tool_calls(self) -> List[Any]:
        """Get tool calls from original response"""
        if self._cached_tool_calls is None:
            self._cached_tool_calls = self._original.tool_calls()
        return self._cached_tool_calls

    @property
    def event_stream(self) -> Iterator[StreamEvent]:
        """Get event stream that intercepts and collects events"""
        for event in self._original.event_stream:
            # Add to collector if active
            self._collector.add_event(event)
            yield event

    def print_content_stream(self):
        """Print content stream (delegates to original)"""
        self._original.print_content_stream()

    @property
    def content(self) -> str:
        """Get content from original response"""
        return self._original.content


def _intercept_call_llm_stream(
    messages: Union[List[Any], Messages],
    tools: Optional[List[Any]] = None,
    model: Optional[str] = None,
    **kwargs,
) -> StreamResponse:
    """Intercepted version of call_llm_stream that collects events"""
    # Call original function
    original_response = call_llm_stream(messages, tools, model, **kwargs)

    # Return wrapped response that intercepts events
    return InterceptedStreamResponse(original_response, _event_collector)


def _intercept_call_llm_stream_events(
    messages: Union[List[Any], Messages],
    tools: Optional[List[Any]] = None,
    model: Optional[str] = None,
    **kwargs,
) -> Iterator[StreamEvent]:
    """Intercepted version of call_llm_stream_events that collects events"""
    # Call original function
    for event in call_llm_stream_events(messages, tools, model, **kwargs):
        # Add to collector if active
        _event_collector.add_event(event)
        yield event


@contextmanager
def llm_streaming_context():
    """
    Context manager for intercepting LLM streaming calls.

    Usage:
        with llm_streaming_context():
            # Any LLM calls within this context will have their events collected
            result = some_node.exec(input_data)
            events = get_collected_events()
    """
    # Store original functions
    import agentic_blocks.llm_agno as llm_module
    original_call_llm_stream = llm_module.call_llm_stream
    original_call_llm_stream_events = llm_module.call_llm_stream_events

    try:
        # Start collecting
        _event_collector.start_collection()

        # Replace functions with intercepted versions
        llm_module.call_llm_stream = _intercept_call_llm_stream
        llm_module.call_llm_stream_events = _intercept_call_llm_stream_events

        yield _event_collector

    finally:
        # Restore original functions
        llm_module.call_llm_stream = original_call_llm_stream
        llm_module.call_llm_stream_events = original_call_llm_stream_events

        # Stop collecting
        _event_collector.stop_collection()


@asynccontextmanager
async def async_llm_streaming_context():
    """
    Async context manager for intercepting LLM streaming calls.

    Usage:
        async with async_llm_streaming_context() as collector:
            # Any LLM calls within this context will have their events collected
            result = await some_async_node.exec(input_data)
            events = collector.get_events()
    """
    # Store original functions
    import agentic_blocks.llm_agno as llm_module
    original_call_llm_stream = llm_module.call_llm_stream
    original_call_llm_stream_events = llm_module.call_llm_stream_events

    try:
        # Start collecting
        _event_collector.start_collection()

        # Replace functions with intercepted versions
        llm_module.call_llm_stream = _intercept_call_llm_stream
        llm_module.call_llm_stream_events = _intercept_call_llm_stream_events

        yield _event_collector

    finally:
        # Restore original functions
        llm_module.call_llm_stream = original_call_llm_stream
        llm_module.call_llm_stream_events = original_call_llm_stream_events

        # Stop collecting
        _event_collector.stop_collection()


def get_collected_events() -> List[StreamEvent]:
    """Get all collected streaming events from intercepted LLM calls"""
    return _event_collector.get_events()


def has_collected_events() -> bool:
    """Check if there are any collected streaming events"""
    return _event_collector.has_events()


class NodeExecutionInterceptor:
    """Intercepts node execution to capture streaming events"""

    def __init__(self, transformer: Optional[StreamEventTransformer] = None):
        self.transformer = transformer or StreamEventTransformer()
        self._collected_events: List[StreamEvent] = []

    async def execute_node_with_streaming(
        self,
        node: Any,
        shared: dict,
        step_name: str = None,
        step_type: str = None
    ) -> AsyncIterator[AiSdkEvent]:
        """
        Execute a PocketFlow node while capturing streaming events.

        Args:
            node: PocketFlow Node instance
            shared: Shared state dictionary
            step_name: Optional step name for events
            step_type: Optional step type for events

        Yields:
            AiSdkEvent objects during node execution
        """
        # Emit step start
        yield self.transformer.create_step_start(step_name, step_type)

        # Execute node with LLM interception
        with llm_streaming_context() as collector:
            # Standard PocketFlow node execution
            prep_result = node.prep(shared)
            exec_result = node._exec(prep_result)
            post_result = node.post(shared, prep_result, exec_result)

            # Get collected events
            events = collector.get_events()

            # Transform and yield events
            for event in events:
                ai_sdk_events = self.transformer.transform_event(event)
                for ai_sdk_event in ai_sdk_events:
                    yield ai_sdk_event

        # Emit step finish
        yield self.transformer.create_step_finish(step_name, step_type)

    def execute_node_sync_with_streaming(
        self,
        node: Any,
        shared: dict,
        step_name: str = None,
        step_type: str = None
    ) -> tuple:
        """
        Execute a PocketFlow node synchronously while capturing streaming events.

        Args:
            node: PocketFlow Node instance
            shared: Shared state dictionary
            step_name: Optional step name for events
            step_type: Optional step type for events

        Returns:
            Tuple of (post_result, collected_ai_sdk_events)
        """
        ai_sdk_events = []

        # Step start
        ai_sdk_events.append(self.transformer.create_step_start(step_name, step_type))

        # Execute node with LLM interception
        with llm_streaming_context() as collector:
            # Standard PocketFlow node execution
            prep_result = node.prep(shared)
            exec_result = node._exec(prep_result)
            post_result = node.post(shared, prep_result, exec_result)

            # Get collected events
            events = collector.get_events()

            # Transform events
            for event in events:
                transformed_events = self.transformer.transform_event(event)
                ai_sdk_events.extend(transformed_events)

        # Step finish
        ai_sdk_events.append(self.transformer.create_step_finish(step_name, step_type))

        return post_result, ai_sdk_events


# Convenience functions
def create_node_interceptor() -> NodeExecutionInterceptor:
    """Create a new node execution interceptor"""
    return NodeExecutionInterceptor()


async def execute_node_streaming(
    node: Any,
    shared: dict,
    step_name: str = None,
    step_type: str = None
) -> AsyncIterator[AiSdkEvent]:
    """
    Convenience function to execute a node with streaming.

    Args:
        node: PocketFlow Node instance
        shared: Shared state dictionary
        step_name: Optional step name for events
        step_type: Optional step type for events

    Yields:
        AiSdkEvent objects during node execution
    """
    interceptor = NodeExecutionInterceptor()
    async for event in interceptor.execute_node_with_streaming(node, shared, step_name, step_type):
        yield event