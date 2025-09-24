"""
ProcessGPT Agent SDK

이 패키지는 ProcessGPT 시스템과 통합하기 위한 Agent Framework를 제공합니다.
"""

from .processgpt_agent_framework import (
    ProcessGPTAgentServer,
    ProcessGPTRequestContext,
    ProcessGPTEventQueue,
    TodoListRowContext,
)

from .database import (
    initialize_db,
    polling_pending_todos,
    record_event,
    save_task_result,
    update_task_error,
    get_consumer_id,
    fetch_agent_data,
    fetch_all_agents,
    fetch_form_types,
    fetch_tenant_mcp_config,
    fetch_human_users_by_proc_inst_id,
)

__version__ = "0.3.12"

__all__ = [
    # Framework classes
    "ProcessGPTAgentServer",
    "ProcessGPTRequestContext", 
    "ProcessGPTEventQueue",
    "TodoListRowContext",
    # Database functions
    "initialize_db",
    "polling_pending_todos",
    "record_event",
    "save_task_result",
    "update_task_error",
    "get_consumer_id",
    "fetch_agent_data",
    "fetch_all_agents",
    "fetch_form_types",
    "fetch_tenant_mcp_config",
    "fetch_human_users_by_proc_inst_id",
]
