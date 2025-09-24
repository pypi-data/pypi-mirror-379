import asyncio
from typing import Any, AsyncGenerator, Callable, Coroutine, List, Optional
from assistant_stream.assistant_stream_chunk import (
    AssistantStreamChunk,
    TextDeltaChunk,
    ReasoningDeltaChunk,
    ToolResultChunk,
    DataChunk,
    ErrorChunk,
    SourceChunk,
    ToolCallBeginChunk,
)
from assistant_stream.modules.tool_call import (
    create_tool_call,
    ToolCallController,
    generate_openai_style_tool_call_id,
)
from assistant_stream.state_manager import StateManager


class RunController:
    def __init__(self, queue, state_data, parent_id: Optional[str] = None):
        self._queue = queue
        self._loop = asyncio.get_running_loop()
        self._dispose_callbacks = []
        self._stream_tasks = []
        self._state_manager = StateManager(self._put_chunk_nowait, state_data)
        self._parent_id = parent_id

    def with_parent_id(self, parent_id: str) -> 'RunController':
        """Create a new RunController instance with the specified parent_id."""
        controller = RunController(self._queue, self._state_manager._state_data, parent_id)
        controller._loop = self._loop
        controller._dispose_callbacks = self._dispose_callbacks
        controller._stream_tasks = self._stream_tasks
        controller._state_manager = self._state_manager
        return controller

    def append_text(self, text_delta: str) -> None:
        """Append a text delta to the stream."""
        chunk = TextDeltaChunk(text_delta=text_delta, parent_id=self._parent_id)
        self._flush_and_put_chunk(chunk)

    def append_reasoning(self, reasoning_delta: str) -> None:
        """Append a reasoning delta to the stream."""
        chunk = ReasoningDeltaChunk(reasoning_delta=reasoning_delta, parent_id=self._parent_id)
        self._flush_and_put_chunk(chunk)

    async def add_tool_call(
        self, tool_name: str, tool_call_id: str = None
    ) -> ToolCallController:
        """Add a tool call to the stream."""
        if tool_call_id is None:
            tool_call_id = generate_openai_style_tool_call_id()

        stream, controller = await create_tool_call(tool_name, tool_call_id, self._parent_id)
        self._dispose_callbacks.append(controller.close)

        self.add_stream(stream)
        return controller

    def add_tool_result(self, tool_call_id: str, result: Any) -> None:
        """Add a tool result to the stream."""
        chunk = ToolResultChunk(
            tool_call_id=tool_call_id,
            result=result,
        )
        self._flush_and_put_chunk(chunk)

    def add_stream(self, stream: AsyncGenerator[AssistantStreamChunk, None]) -> None:
        """Append a substream to the main stream."""

        async def reader():
            async for chunk in stream:
                self._flush_and_put_chunk(chunk)

        task = asyncio.create_task(reader())
        self._stream_tasks.append(task)

    def add_data(self, data: Any) -> None:
        """Emit an event to the main stream."""
        chunk = DataChunk(data=data)
        self._flush_and_put_chunk(chunk)

    def add_error(self, error: str) -> None:
        """Emit an error to the main stream."""
        chunk = ErrorChunk(error=error)
        self._flush_and_put_chunk(chunk)
    
    def add_source(self, id: str, url: str, title: Optional[str] = None) -> None:
        """Add a source to the stream."""
        chunk = SourceChunk(
            id=id,
            url=url,
            title=title,
            parent_id=self._parent_id
        )
        self._flush_and_put_chunk(chunk)

    def _put_chunk_nowait(self, chunk):
        """Helper method to put a chunk in the queue without waiting.

        This is used as a callback for the StateManager.
        """
        self._loop.call_soon_threadsafe(self._queue.put_nowait, chunk)

    def _flush_and_put_chunk(self, chunk):
        """Helper method to flush state operations and put a chunk in the queue.

        This ensures state operations are sent before other operations.
        """
        # Flush any pending state operations first
        self._state_manager.flush()
        # Add the chunk to the queue
        self._loop.call_soon_threadsafe(self._queue.put_nowait, chunk)

    @property
    def state(self):
        """Access the state proxy object for making state updates.

        This property provides a proxy object that allows navigating to any path
        in the state, reading values, and setting values, which will trigger the
        appropriate state update operation.

        If the state is None, this property returns None directly.
        You can set the root state directly by assigning to this property.

        Example:
            controller.state = {"user": {"name": "John"},"messages": "Hello"}  # Sets the entire state
            controller.state["user"]["name"] = "Bob"  # Sets the value at path ["user", "name"]
            name = controller.state["user"]["name"]  # Gets the value at path ["user", "name"]
            controller.state["messages"] += " world"  # Appends text at path ["messages"]
        """
        return self._state_manager.state

    @state.setter
    def state(self, value):
        """Set the entire state object.

        Args:
            value: The new state value to set
        """
        self._state_manager.add_operations(
            [{"type": "set", "path": [], "value": value}]
        )


async def create_run(
    callback: Callable[[RunController], Coroutine[Any, Any, None]],
    *,
    state: Any | None = None,
) -> AsyncGenerator[AssistantStreamChunk, None]:
    queue = asyncio.Queue()
    controller = RunController(queue, state_data=state)

    async def background_task():
        try:
            await callback(controller)
        except Exception as e:
            controller.add_error(str(e))
            raise
        finally:
            # Flush any pending state updates before disposing
            controller._state_manager.flush()

            for dispose in controller._dispose_callbacks:
                dispose()
            try:
                for task in controller._stream_tasks:
                    await task
            finally:
                asyncio.get_running_loop().call_soon_threadsafe(queue.put_nowait, None)

    task = asyncio.create_task(background_task())

    while True:
        chunk = await controller._queue.get()
        if chunk is None:
            break
        yield chunk
        controller._queue.task_done()

    await task
