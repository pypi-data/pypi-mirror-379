from functools import wraps
import traceback
from agent_tracing.database import trace_store
import time

def initialize_agent_tracing(agent_id=None):
    """
    Decorator for agent functions.
    Starts a workflow if none exists, registers the agent, 
    and logs its final output as an 'AGENT' step.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not trace_store.current_workflow:
                trace_store.start_workflow()
            agent_id_used = trace_store.add_agent(agent_id)

            try:
                current_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                trace_store.log_step(
                    agent_id_used, "AGENT",
                    {"args": args, "kwargs": kwargs},
                    result,
                    latency= (end_time - current_time)*1000
                )
                return result
            except Exception as e:
                trace_store.log_step(
                    agent_id_used, "AGENT_ERROR",
                    {"args": args, "kwargs": kwargs},
                    {"error": str(e), "traceback": traceback.format_exc()}
                )
                raise
        return wrapper
    return decorator


def tool_tracing(tool_name=None):
    """
    Decorator for tool functions (APIs, DB calls, external systems).
    Logs input/output and exceptions as 'TOOL' steps.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            agent_id = trace_store.data[trace_store.current_workflow]["agents"][-1]["agent_id"]

            try:
                current_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                trace_store.log_step(
                    agent_id, "TOOL",
                    {"args": args, "kwargs": kwargs},
                    result,
                    latency= (end_time - current_time)*1000,
                    tool_name=tool_name or func.__name__
                )
                return result
            except Exception as e:
                trace_store.log_step(
                    agent_id, "TOOL_ERROR",
                    {"args": args, "kwargs": kwargs},
                    {"error": str(e), "traceback": traceback.format_exc()},
                    tool_name=tool_name or func.__name__
                )
                raise
        return wrapper
    return decorator


def llm_tracing(func):
    """
    Decorator for LLM calls (wrapping the actual inference function).
    Logs prompts, parameters, and responses.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        agent_id = trace_store.data[trace_store.current_workflow]["agents"][-1]["agent_id"]

        try:
            current_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            trace_store.log_step(
                agent_id, "LLM",
                {"args": args, "kwargs": kwargs},
                result,
                latency= (end_time - current_time) * 1000
            )
            return result
        except Exception as e:
            trace_store.log_step(
                agent_id, "LLM_ERROR",
                {"args": args, "kwargs": kwargs},
                {"error": str(e), "traceback": traceback.format_exc()}
            )
            raise
    return wrapper


def memory_tracing(action):
    """
    Decorator for memory operations (read/write).
    `action` should be 'READ' or 'WRITE'.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            agent_id = trace_store.data[trace_store.current_workflow]["agents"][-1]["agent_id"]

            try:
                current_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                trace_store.log_step(
                    agent_id, f"MEMORY_{action.upper()}",
                    {"args": args, "kwargs": kwargs},
                    result,
                    latency= (end_time - current_time) * 1000
                )
                return result
            except Exception as e:
                trace_store.log_step(
                    agent_id, f"MEMORY_{action.upper()}_ERROR",
                    {"args": args, "kwargs": kwargs},
                    {"error": str(e), "traceback": traceback.format_exc()}
                )
                raise
        return wrapper
    return decorator
