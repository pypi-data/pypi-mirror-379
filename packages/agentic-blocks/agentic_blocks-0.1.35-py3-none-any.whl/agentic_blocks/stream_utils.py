"""
Stream processing utilities for AI agent events using RxPY.

This module provides utilities to convert event streams from call_llm_stream_events
into RxPY observables for powerful reactive stream processing.
"""

from typing import List, Dict, Any, Iterator, Optional
import json
import reactivex as rx
from reactivex import operators as ops

from .llm_agno import (
    StreamEvent,
    StreamEventType,
    ToolCallStartedEvent,
    ToolCallCompletedEvent,
    AssistantResponseEvent,
    ModelResponseCompleteEvent,
)


class AgentStreamProcessor:
    """
    Utility class for processing AI agent event streams with RxPY.

    Provides methods to convert event iterators to observables and
    common stream processing patterns for AI agent workflows.
    """

    @staticmethod
    def from_event_iterator(event_iterator: Iterator[StreamEvent]) -> rx.Observable:
        """
        Convert an event iterator to an RxPY Observable.

        Args:
            event_iterator: Iterator yielding StreamEvent objects

        Returns:
            RxPY Observable that emits the events
        """
        def subscribe(observer, scheduler=None):
            try:
                for event in event_iterator:
                    observer.on_next(event)
                observer.on_completed()
            except Exception as e:
                observer.on_error(e)

            # Return a disposable
            return lambda: None

        return rx.create(subscribe)

    @staticmethod
    def from_event_list(events: List[StreamEvent]) -> rx.Observable:
        """
        Convert a list of events to an RxPY Observable.

        Args:
            events: List of StreamEvent objects

        Returns:
            RxPY Observable that emits the events
        """
        return rx.from_iterable(events)

    @staticmethod
    def extract_tool_calls(observable: rx.Observable) -> rx.Observable:
        """
        Extract completed tool calls in OpenAI format from event stream.

        Args:
            observable: Observable emitting StreamEvent objects

        Returns:
            Observable that emits a list of tool calls in OpenAI format
        """
        return observable.pipe(
            ops.filter(lambda e: e.event_type == StreamEventType.tool_call_completed),
            ops.map(lambda e: {
                "id": e.tool_call_id,
                "type": "function",
                "function": {
                    "name": e.tool_name,
                    "arguments": json.dumps(e.tool_args)
                }
            }),
            ops.to_list()
        )

    @staticmethod
    def aggregate_content(observable: rx.Observable) -> rx.Observable:
        """
        Aggregate all assistant content into a single string.

        Args:
            observable: Observable emitting StreamEvent objects

        Returns:
            Observable that emits the aggregated content string
        """
        return observable.pipe(
            ops.filter(lambda e: e.event_type == StreamEventType.assistant_response),
            ops.map(lambda e: e.content),
            ops.reduce(lambda acc, content: acc + content, "")
        )

    @staticmethod
    def get_tool_events(observable: rx.Observable) -> rx.Observable:
        """
        Filter to tool-related events only (started and completed).

        Args:
            observable: Observable emitting StreamEvent objects

        Returns:
            Observable that emits only tool call events
        """
        return observable.pipe(
            ops.filter(lambda e: e.event_type in [
                StreamEventType.tool_call_started,
                StreamEventType.tool_call_completed
            ])
        )

    @staticmethod
    def get_content_events(observable: rx.Observable) -> rx.Observable:
        """
        Filter to assistant content events only.

        Args:
            observable: Observable emitting StreamEvent objects

        Returns:
            Observable that emits only assistant response events
        """
        return observable.pipe(
            ops.filter(lambda e: e.event_type == StreamEventType.assistant_response)
        )

    @staticmethod
    def create_multi_consumer(observable: rx.Observable) -> rx.Observable:
        """
        Create a shared observable for multiple consumers.

        Args:
            observable: Observable to share

        Returns:
            Shared observable that can be subscribed to multiple times
        """
        return observable.pipe(ops.share())

    @staticmethod
    def buffer_tool_calls(observable: rx.Observable, count: int = 5) -> rx.Observable:
        """
        Buffer tool calls for batch processing.

        Args:
            observable: Observable emitting StreamEvent objects
            count: Number of tool calls to buffer before emitting batch

        Returns:
            Observable that emits lists of tool call events
        """
        return observable.pipe(
            ops.filter(lambda e: e.event_type == StreamEventType.tool_call_completed),
            ops.buffer_with_count(count)
        )

    @staticmethod
    def map_to_openai_format(tool_event: ToolCallCompletedEvent) -> Dict[str, Any]:
        """
        Convert a tool call event to OpenAI format.

        Args:
            tool_event: ToolCallCompletedEvent object

        Returns:
            Dictionary in OpenAI tool call format
        """
        return {
            "id": tool_event.tool_call_id,
            "type": "function",
            "function": {
                "name": tool_event.tool_name,
                "arguments": json.dumps(tool_event.tool_args)
            }
        }


def create_tool_extraction_pipeline(events: Iterator[StreamEvent]) -> rx.Observable:
    """
    Create a complete pipeline for extracting tool calls from an event stream.

    Args:
        events: Iterator of StreamEvent objects

    Returns:
        Observable that emits extracted tool calls in OpenAI format
    """
    processor = AgentStreamProcessor()
    stream = processor.from_event_iterator(events)
    return processor.extract_tool_calls(stream)


def create_content_aggregation_pipeline(events: Iterator[StreamEvent]) -> rx.Observable:
    """
    Create a pipeline for aggregating assistant content from an event stream.

    Args:
        events: Iterator of StreamEvent objects

    Returns:
        Observable that emits the aggregated content string
    """
    processor = AgentStreamProcessor()
    stream = processor.from_event_iterator(events)
    return processor.aggregate_content(stream)


def create_multi_output_pipeline(events: Iterator[StreamEvent]) -> Dict[str, rx.Observable]:
    """
    Create multiple processing pipelines from a single event stream.

    Args:
        events: Iterator of StreamEvent objects

    Returns:
        Dictionary with different observable streams:
        - 'tool_calls': Observable emitting tool calls in OpenAI format
        - 'content': Observable emitting aggregated content
        - 'tool_events': Observable emitting tool-related events
        - 'all_events': Observable emitting all events
    """
    processor = AgentStreamProcessor()
    shared_stream = processor.create_multi_consumer(
        processor.from_event_iterator(events)
    )

    return {
        'tool_calls': processor.extract_tool_calls(shared_stream),
        'content': processor.aggregate_content(shared_stream),
        'tool_events': processor.get_tool_events(shared_stream),
        'all_events': shared_stream
    }


# Convenience functions for common patterns
def extract_tool_calls_sync(events: List[StreamEvent]) -> List[Dict[str, Any]]:
    """
    Synchronously extract tool calls from a list of events.

    Args:
        events: List of StreamEvent objects

    Returns:
        List of tool calls in OpenAI format
    """
    processor = AgentStreamProcessor()
    stream = processor.from_event_list(events)
    tool_calls_observable = processor.extract_tool_calls(stream)

    result = []
    tool_calls_observable.subscribe(on_next=lambda x: result.extend(x))
    return result


def aggregate_content_sync(events: List[StreamEvent]) -> str:
    """
    Synchronously aggregate content from a list of events.

    Args:
        events: List of StreamEvent objects

    Returns:
        Aggregated content string
    """
    processor = AgentStreamProcessor()
    stream = processor.from_event_list(events)
    content_observable = processor.aggregate_content(stream)

    result = [""]
    content_observable.subscribe(on_next=lambda x: result.__setitem__(0, x))
    return result[0]


# AI-SDK Event Processing Extensions
class AiSdkStreamProcessor:
    """
    Utility class for processing AI-SDK event streams with RxPY.

    Provides methods to convert AI-SDK event streams to observables and
    common stream processing patterns for AI-SDK compatible workflows.
    """

    @staticmethod
    def from_ai_sdk_event_iterator(event_iterator) -> rx.Observable:
        """
        Convert an AI-SDK event iterator to an RxPY Observable.

        Args:
            event_iterator: Iterator yielding AiSdkEvent objects

        Returns:
            RxPY Observable that emits the events
        """
        def subscribe(observer, scheduler=None):
            try:
                for event in event_iterator:
                    observer.on_next(event)
                observer.on_completed()
            except Exception as e:
                observer.on_error(e)

            # Return a disposable
            return lambda: None

        return rx.create(subscribe)

    @staticmethod
    def from_ai_sdk_event_list(events) -> rx.Observable:
        """
        Convert a list of AI-SDK events to an RxPY Observable.

        Args:
            events: List of AiSdkEvent objects

        Returns:
            RxPY Observable that emits the events
        """
        return rx.from_iterable(events)

    @staticmethod
    def filter_by_event_type(observable: rx.Observable, event_types) -> rx.Observable:
        """
        Filter AI-SDK events by event type.

        Args:
            observable: Observable emitting AiSdkEvent objects
            event_types: Single event type string or list of event types to include

        Returns:
            Observable that emits only events of specified types
        """
        if isinstance(event_types, str):
            event_types = [event_types]

        return observable.pipe(
            ops.filter(lambda e: e.type in event_types)
        )

    @staticmethod
    def extract_tool_events(observable: rx.Observable) -> rx.Observable:
        """
        Extract tool-related events from AI-SDK stream.

        Args:
            observable: Observable emitting AiSdkEvent objects

        Returns:
            Observable that emits only tool-related events
        """
        tool_event_types = [
            "tool-input-start",
            "tool-input-delta",
            "tool-input-available",
            "tool-output-available"
        ]
        return AiSdkStreamProcessor.filter_by_event_type(observable, tool_event_types)

    @staticmethod
    def extract_text_events(observable: rx.Observable) -> rx.Observable:
        """
        Extract text streaming events from AI-SDK stream.

        Args:
            observable: Observable emitting AiSdkEvent objects

        Returns:
            Observable that emits only text-related events
        """
        text_event_types = ["text-start", "text-delta", "text-end"]
        return AiSdkStreamProcessor.filter_by_event_type(observable, text_event_types)

    @staticmethod
    def extract_flow_events(observable: rx.Observable) -> rx.Observable:
        """
        Extract flow control events from AI-SDK stream.

        Args:
            observable: Observable emitting AiSdkEvent objects

        Returns:
            Observable that emits only flow control events
        """
        flow_event_types = ["start", "start-step", "finish-step", "finish"]
        return AiSdkStreamProcessor.filter_by_event_type(observable, flow_event_types)

    @staticmethod
    def aggregate_text_content(observable: rx.Observable) -> rx.Observable:
        """
        Aggregate text content from AI-SDK text-delta events.

        Args:
            observable: Observable emitting AiSdkEvent objects

        Returns:
            Observable that emits the aggregated text content
        """
        return observable.pipe(
            ops.filter(lambda e: e.type == "text-delta"),
            ops.map(lambda e: e.data.get("delta", "")),
            ops.reduce(lambda acc, delta: acc + delta, "")
        )

    @staticmethod
    def track_step_progress(observable: rx.Observable) -> rx.Observable:
        """
        Track step execution progress in the flow.

        Args:
            observable: Observable emitting AiSdkEvent objects

        Returns:
            Observable that emits step progress information
        """
        return observable.pipe(
            ops.filter(lambda e: e.type in ["start-step", "finish-step"]),
            ops.scan(lambda acc, e: {
                "total_steps": acc["total_steps"] + (1 if e.type == "start-step" else 0),
                "completed_steps": acc["completed_steps"] + (1 if e.type == "finish-step" else 0),
                "current_event": e
            }, {"total_steps": 0, "completed_steps": 0, "current_event": None})
        )

    @staticmethod
    def create_multi_consumer(observable: rx.Observable) -> rx.Observable:
        """
        Create a shared observable for multiple consumers.

        Args:
            observable: Observable to share

        Returns:
            Shared observable that can be subscribed to multiple times
        """
        return observable.pipe(ops.share())

    @staticmethod
    def buffer_events_by_type(observable: rx.Observable, event_type: str, count: int = 5) -> rx.Observable:
        """
        Buffer events of a specific type for batch processing.

        Args:
            observable: Observable emitting AiSdkEvent objects
            event_type: Event type to buffer
            count: Number of events to buffer before emitting batch

        Returns:
            Observable that emits lists of buffered events
        """
        return observable.pipe(
            ops.filter(lambda e: e.type == event_type),
            ops.buffer_with_count(count)
        )


def create_ai_sdk_multi_output_pipeline(events) -> Dict[str, rx.Observable]:
    """
    Create multiple processing pipelines from a single AI-SDK event stream.

    Args:
        events: Iterator or list of AiSdkEvent objects

    Returns:
        Dictionary with different observable streams:
        - 'tool_events': Observable emitting tool-related events
        - 'text_events': Observable emitting text streaming events
        - 'flow_events': Observable emitting flow control events
        - 'text_content': Observable emitting aggregated text content
        - 'step_progress': Observable emitting step progress information
        - 'all_events': Observable emitting all events
    """
    processor = AiSdkStreamProcessor()

    # Create shared stream from input
    if hasattr(events, '__iter__') and not hasattr(events, '__next__'):
        # It's a list or similar
        shared_stream = processor.create_multi_consumer(
            processor.from_ai_sdk_event_list(events)
        )
    else:
        # It's an iterator
        shared_stream = processor.create_multi_consumer(
            processor.from_ai_sdk_event_iterator(events)
        )

    return {
        'tool_events': processor.extract_tool_events(shared_stream),
        'text_events': processor.extract_text_events(shared_stream),
        'flow_events': processor.extract_flow_events(shared_stream),
        'text_content': processor.aggregate_text_content(shared_stream),
        'step_progress': processor.track_step_progress(shared_stream),
        'all_events': shared_stream
    }


# Convenience functions for AI-SDK events
def extract_text_content_sync(events) -> str:
    """
    Synchronously extract and aggregate text content from AI-SDK events.

    Args:
        events: List or iterator of AiSdkEvent objects

    Returns:
        Aggregated text content string
    """
    processor = AiSdkStreamProcessor()

    if hasattr(events, '__iter__') and not hasattr(events, '__next__'):
        stream = processor.from_ai_sdk_event_list(events)
    else:
        stream = processor.from_ai_sdk_event_iterator(events)

    content_observable = processor.aggregate_text_content(stream)

    result = [""]
    content_observable.subscribe(on_next=lambda x: result.__setitem__(0, x))
    return result[0]


def extract_tool_calls_from_ai_sdk_events(events) -> List[Dict[str, Any]]:
    """
    Extract tool calls from AI-SDK events.

    Args:
        events: List or iterator of AiSdkEvent objects

    Returns:
        List of tool call information dictionaries
    """
    processor = AiSdkStreamProcessor()

    if hasattr(events, '__iter__') and not hasattr(events, '__next__'):
        stream = processor.from_ai_sdk_event_list(events)
    else:
        stream = processor.from_ai_sdk_event_iterator(events)

    tool_calls = []

    # Extract tool-input-available events (they contain complete tool call info)
    tool_available_observable = stream.pipe(
        ops.filter(lambda e: e.type == "tool-input-available"),
        ops.map(lambda e: {
            "tool_call_id": e.data.get("toolCallId"),
            "tool_name": e.data.get("toolName"),
            "input": e.data.get("input", {})
        })
    )

    tool_available_observable.subscribe(on_next=lambda tc: tool_calls.append(tc))
    return tool_calls