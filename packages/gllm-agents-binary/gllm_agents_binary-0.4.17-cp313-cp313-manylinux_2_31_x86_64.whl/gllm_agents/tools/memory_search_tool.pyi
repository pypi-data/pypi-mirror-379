from _typeshed import Incomplete
from collections.abc import Callable as Callable
from gllm_agents.memory.constants import MemoryDefaults as MemoryDefaults
from gllm_agents.memory.mem0_memory import Mem0Memory as Mem0Memory
from gllm_agents.utils.datetime import is_valid_date_string as is_valid_date_string
from gllm_agents.utils.datetime.date_range_parser import next_day_iso as next_day_iso, resolve_natural_date_range as resolve_natural_date_range
from gllm_agents.utils.logger_manager import LoggerManager as LoggerManager
from langchain_core.tools import BaseTool
from pydantic import BaseModel
from typing import Any

logger: Incomplete

class Mem0SearchInput(BaseModel):
    """Input schema for Mem0 unified retrieval tool.

    Supports both semantic search (with query) and pure date-based recall (without query).
    Time periods can be specified using either natural language or explicit dates.
    """
    query: str | None
    time_period: str | None
    start_date: str | None
    end_date: str | None
    limit: int | None
    categories: list[str] | None
    metadata: dict[str, Any] | None

class Mem0SearchTool(BaseTool):
    """LangChain tool for unified Mem0 memory retrieval with flexible time filtering.

    Supports both semantic search (with query) and pure date-based recall (without query).
    """
    name: str
    description: str
    args_schema: type[Mem0SearchInput]
    memory: Mem0Memory
    default_user_id: str | None
    user_id_provider: Callable[[], str | None] | None
    def __init__(self, memory: Mem0Memory, *, default_user_id: str | None = None, user_id_provider: Callable[[], str | None] | None = None, **kwargs: Any) -> None:
        """Initialize the Mem0 search tool for the provided memory backend."""
