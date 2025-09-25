# Robonito Agent Tracing SDK

Robonito Agent Tracing SDK is a Python library designed to **trace and log the complete workflow of LLM-based agents**.  
It captures every step of an agent’s execution, including:

- LLM responses and reasoning steps  
- Agent responses and decisions  
- Tool call inputs and outputs  
- Memory reads and writes  
- Multi-agent interactions and workflow engagement  

This SDK is ideal for **agent testing, evaluation, and debugging** in complex LLM systems.

---

## Features

- **Multi-Agent Workflow Tracing**: Capture interactions between multiple agents in a single workflow.  
- **LLM Response Logging**: Trace prompts, parameters, and outputs from language models.  
- **Tool Tracing**: Log external tool calls with input/output and tool name.  
- **Memory Tracing**: Track reads and writes to the agent’s memory.  
- **Error Tracing**: Capture exceptions and errors during execution.  
- **In-Memory Database**: Lightweight, dependency-free, and runtime-safe storage of traces.  
- **Export & Integration**: Send traces as JSON to evaluation systems or save to file.

---

## Installation

```bash
pip install robonito-agent-tracing-sdk
