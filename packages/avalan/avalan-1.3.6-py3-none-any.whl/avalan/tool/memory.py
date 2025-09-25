from . import Tool, ToolSet
from ..compat import override
from ..entities import ToolCallContext
from ..memory.manager import MemoryManager
from ..memory.permanent import Memory, VectorFunction

from contextlib import AsyncExitStack


class MessageReadTool(Tool):
    """Fetch user information and preferences from previous messages.

    Args:
        search: What information to fetch. For example: "user's name".

    Returns:
        The search results, if any. This might be part of a message,
        so extract the information from it. For example, you may be
        getting "my name is Leo", not simply "Leo" as the user's name.
        If no result returned (indicated by the string "NOT_FOUND"), the
        information could not be found, so you should ask for it.
    """

    _memory_manager: MemoryManager
    _NOT_FOUND = "NOT_FOUND"

    def __init__(self, memory_manager: MemoryManager) -> None:
        super().__init__()
        self._memory_manager = memory_manager
        self.__name__ = "message.read"

    async def __call__(self, search: str, context: ToolCallContext) -> str:
        if (
            not context.agent_id
            or not context.session_id
            or not context.participant_id
        ):
            return MessageReadTool._NOT_FOUND

        results = await self._memory_manager.search_messages(
            agent_id=context.agent_id,
            exclude_session_id=context.session_id,
            function=VectorFunction.L2_DISTANCE,
            participant_id=context.participant_id,
            search=search,
            search_user_messages=True,
            limit=1,
        )
        if results and results[0].message:
            return results[0].message.content

        return MessageReadTool._NOT_FOUND


class MemoryReadTool(Tool):
    """Search permanent memories for stored knowledge.

    Args:
        search: What information to fetch. For example: "usage instructions".

    Returns:
        The search results, if any.
    """
    
    _memory_manager: MemoryManager

    def __init__(self, memory_manager: MemoryManager) -> None:
        super().__init__()
        self._memory_manager = memory_manager
        self.__name__ = "read"

    async def __call__(
        self,
        namespace: str,
        search: str,
        *,
        context: ToolCallContext,
        limit: int | None = None,
        function: VectorFunction = VectorFunction.L2_DISTANCE,
    ) -> list[Memory]:
        """Return permanent memories that match the search query."""
        if (
            not namespace
            or not namespace.strip()
            or not search
            or not search.strip()
        ):
            return []

        if not context.participant_id:
            return []

        try:
            memories = await self._memory_manager.search(
                search,
                participant_id=context.participant_id,
                namespace=namespace,
                function=function,
                limit=limit,
            )
        except KeyError:
            return []

        return memories


class MemoryToolSet(ToolSet):
    @override
    def __init__(
        self,
        memory_manager: MemoryManager,
        *,
        exit_stack: AsyncExitStack | None = None,
        namespace: str | None = None,
    ) -> None:
        tools = [
            MessageReadTool(memory_manager),
            MemoryReadTool(memory_manager),
        ]
        super().__init__(
            exit_stack=exit_stack, namespace=namespace, tools=tools
        )
