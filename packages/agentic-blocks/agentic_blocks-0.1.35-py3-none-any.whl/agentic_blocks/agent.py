from typing import AsyncIterator
from pocketflow import Node, Flow
from agentic_blocks.llm_agno import call_llm_stream
from agentic_blocks.utils.tools_utils import (
    create_tool_registry,
    execute_pending_tool_calls,
    agno_tools_to_openai_format,
)
from agentic_blocks.messages import Messages
from agentic_blocks.streaming_node_mixin import StreamingNodeMixin
from agentic_blocks.streaming_flow import StreamingFlow


class Agent:
    """Modern Agent with streaming capabilities"""

    def __init__(self, system_prompt: str, tools: list):
        self.system_prompt = system_prompt
        self.tools = tools
        self.tool_registry = create_tool_registry(tools)
        self.openai_tools = agno_tools_to_openai_format(tools)
        self.flow = self._create_flow()

    def _create_flow(self) -> Flow:
        """Create the agent flow with streaming nodes"""

        class LLMNode(Node, StreamingNodeMixin):
            def __init__(self, system_prompt, openai_tools):
                super().__init__()
                self.system_prompt = system_prompt
                self.openai_tools = openai_tools

            def prep(self, shared):
                return shared["messages"]

            def exec(self, messages: Messages) -> tuple[Messages, object]:
                stream_response = call_llm_stream(messages.get_messages(), tools=self.openai_tools)

                if stream_response.tool_calls():
                    self.stream_llm_response(stream_response)
                    messages.add_tool_calls(stream_response.tool_calls())
                else:
                    messages.add_assistant_message(stream_response.content)

                return messages, stream_response

            def post(self, shared, prep_res, exec_res):
                shared["messages"], shared["stream_response"] = exec_res
                return "use_tool" if shared["messages"].has_pending_tool_calls() else "answer_node"

        class ToolNode(Node, StreamingNodeMixin):
            def __init__(self, tool_registry):
                super().__init__()
                self.tool_registry = tool_registry

            def prep(self, shared):
                return shared["messages"]

            def exec(self, messages: Messages) -> Messages:
                # Stream tool input events (start, delta, available)
                self.stream_tool_input_events(messages)

                # Stream loading state BEFORE execution
                self.stream_tool_loading(messages)

                # Execute tools (separate from streaming)
                tool_responses = execute_pending_tool_calls(messages, self.tool_registry)

                # Stream completion AFTER execution
                self.stream_tool_execution(tool_responses)

                # Add responses to messages
                messages.add_tool_responses(tool_responses)
                return messages

            def post(self, shared, prep_res, messages):
                return "llm_node"

        class AnswerNode(Node, StreamingNodeMixin):
            def prep(self, shared):
                self.stream_llm_response(shared["stream_response"])

                messages = shared["messages"]
                shared["answer"] = messages.get_messages()[-1]
                return messages

            def exec(self, messages):
                return messages

        # Create nodes
        llm_node = LLMNode(self.system_prompt, self.openai_tools)
        tool_node = ToolNode(self.tool_registry)
        answer_node = AnswerNode()

        # Set up flow routing
        llm_node - "use_tool" >> tool_node
        tool_node - "llm_node" >> llm_node
        llm_node - "answer_node" >> answer_node

        return Flow(start=llm_node)

    async def run_stream_sse(self, user_prompt: str) -> AsyncIterator[str]:
        """Run the agent and stream SSE events"""
        # Create messages
        messages = Messages(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt
        )

        shared = {"messages": messages}

        # Stream the flow execution
        wrapper = StreamingFlow(self.flow)
        async for sse_event in wrapper.run_stream_sse(shared):
            yield sse_event