# Agent Tracing SDK (Python)

Agent Tracing SDK is a **Python library** designed to **trace and log the complete workflow of LLM-based agents**.

It captures every step of an agent's execution, including:

- LLM responses and reasoning steps
- Agent responses and decisions
- Tool call inputs and outputs
- Memory reads and writes
- Multi-agent interactions and workflow engagement

This SDK is ideal for **agent testing, evaluation, and debugging** in complex LLM systems.

## Features

- **Multi-Agent Workflow Tracing**: Capture interactions between multiple agents in a single workflow
- **LLM Response Logging**: Trace prompts, parameters, and outputs from language models
- **Tool Tracing**: Log external tool calls with input/output and tool name
- **Memory Tracing**: Track reads and writes to the agent's memory
- **Error Tracing**: Capture exceptions and errors during execution
- **In-Memory Storage**: Lightweight, dependency-free, and runtime-safe storage of traces
- **Export & Integration**: Send traces as JSON to evaluation systems or save to file
- **Framework Agnostic**: Works seamlessly with any Python project
- **Zero Dependencies**: Lightweight with no external dependencies (except standard library)

## Installation

Install via pip:

```bash
pip install agent-tracing-sdk
```

## Getting Started

### Step 1: Import the Library

```python
from agent_tracing.database import trace_store
from agent_tracing.tool_tracing import (
    initialize_agent_tracing,
    llm_tracing,
    tool_tracing,
    memory_tracing
)
from agent_tracing.utils import send_data_to_robonito
import json
```

### Step 2: Tracing Agents

Use the `@initialize_agent_tracing` decorator to automatically trace agent functions:

```python
@initialize_agent_tracing(agent_id="agent-1")
def my_agent(input_data):
    print(f"Running agent with {input_data}")
    return f"Processed {input_data}"
```

**Notes:**
- `agent_id="agent-1"` is optional. If omitted, an automatic ID is assigned
- All function calls, input, output, latency, and errors are logged automatically

### Step 3: Tracing LLM Calls

Use `@llm_tracing` on functions that interact with language models:

```python
@llm_tracing
def query_llm(prompt):
    # Your LLM call implementation here
    return f"LLM response to '{prompt}'"
```

**Logs:** prompts, parameters, responses, latency, and exceptions

### Step 4: Tracing Tools / External Systems

Use `@tool_tracing(tool_name)` for functions that call external tools or APIs:

```python
@tool_tracing(tool_name="Calculator")
def add_numbers(a, b):
    return a + b

@tool_tracing(tool_name="WebSearch")
def search_web(query):
    # Your web search implementation
    return f"Search results for: {query}"
```

**Notes:**
- Logs input arguments, output, latency, and exceptions
- `tool_name` is optional; defaults to function name

### Step 5: Tracing Memory Operations

Use `@memory_tracing("READ" | "WRITE")` to trace memory reads or writes:

```python
@memory_tracing("WRITE")
def memory_store(key, value):
    # Your memory write implementation
    return f"stored: {key} = {value}"

@memory_tracing("READ")
def memory_retrieve(key):
    # Your memory read implementation
    return f"retrieved: {key}"
```

**Purpose:** Tracks arguments, results, execution time, and errors to understand agent memory interactions

### Step 6: Inspecting Workflow Traces

All traces are stored in-memory via `trace_store`:

```python
from agent_tracing.database import trace_store

workflow = trace_store.get_workflow()
print(json.dumps(workflow, indent=2))
```

Each workflow contains agents and their logged steps. Steps include type, input, output, latency, timestamp, and tool names if applicable.

### Step 7: Sending Workflow Data to Robonito Server

Use the `send_data_to_robonito` function to send captured workflows to a server:

```python
from agent_tracing.utils import send_data_to_robonito

# Send current workflow
send_data_to_robonito()

# Send specific workflow by ID
send_data_to_robonito(workflow_id="workflow-123")
```

**Environment Configuration:**

Set the `ROBONITO_URL` environment variable:

```bash
export ROBONITO_URL=http://localhost:3001/add-data
```

Or set it in your Python code:

```python
import os
os.environ['ROBONITO_URL'] = 'http://localhost:3001/add-data'
```

## Complete Example

```python
from agent_tracing.tool_tracing import initialize_agent_tracing, tool_tracing, llm_tracing, memory_tracing
from agent_tracing.database import trace_store
from agent_tracing.utils import send_data_to_robonito
import json
import time

@initialize_agent_tracing(agent_id="agent-1")
def agent_one(x, y):
    """Primary agent that performs calculations and queries LLM"""
    time.sleep(1)  # Simulate processing time
    res = add_numbers(x, y)
    memory_store("last_result", res)
    ans = query_llm(f"What is {x}+{y}?")
    return ans

@initialize_agent_tracing(agent_id="agent-2")
def agent_two(query):
    """Secondary agent that reasons based on memory"""
    time.sleep(1)
    mem = memory_retrieve("last_result")
    return query_llm(f"Answer based on memory: {mem}, and query: {query}")

@tool_tracing(tool_name="Calculator")
def add_numbers(a, b):
    """Addition tool"""
    time.sleep(0.5)  # Simulate computation time
    return a + b

@llm_tracing
def query_llm(prompt):
    """LLM query function"""
    time.sleep(2)  # Simulate LLM response time
    return f"LLM says: {prompt}"

@memory_tracing("WRITE")
def memory_store(key, value):
    """Memory write operation"""
    time.sleep(0.1)
    return f"stored: {key} = {value}"

@memory_tracing("READ")
def memory_retrieve(key):
    """Memory read operation"""
    time.sleep(0.1)
    return f"retrieved value for {key}"

def main():
    # Execute agents
    result1 = agent_one(2, 3)
    print(f"Agent 1 result: {result1}")
    
    result2 = agent_two("continue reasoning")
    print(f"Agent 2 result: {result2}")
    
    # Print workflow trace
    workflow = trace_store.get_workflow()
    print("\nWorkflow trace:")
    print(json.dumps(workflow, indent=2))
    
    # Send workflow to Robonito server
    try:
        send_data_to_robonito()
        print("Workflow sent successfully!")
    except Exception as error:
        print(f"Failed to send workflow: {error}")

if __name__ == "__main__":
    main()
```

## Class-Based Usage

The decorators also work with class methods:

```python
class MyAgent:
    @initialize_agent_tracing(agent_id="class-agent")
    def run_task(self, input_data):
        result = self.process_data(input_data)
        return self.generate_response(result)
    
    @tool_tracing(tool_name="DataProcessor")
    def process_data(self, data):
        return f"processed: {data}"
    
    @llm_tracing
    def generate_response(self, processed_data):
        return f"LLM response for: {processed_data}"

# Usage
agent = MyAgent()
result = agent.run_task("hello world")
```

## Configuration

### Environment Variables

- `ROBONITO_URL`: Server endpoint for sending trace data (default: `http://localhost:3001/add-data`)

## API Reference

### Decorators

- `@initialize_agent_tracing(agent_id: str = None)` - Initializes tracing for agent function execution
- `@llm_tracing` - Traces LLM interactions
- `@tool_tracing(tool_name: str = None)` - Traces external tool calls
- `@memory_tracing(operation: str)` - Traces memory operations (`"READ"` or `"WRITE"`)

### Functions

- `trace_store.get_workflow() -> dict` - Retrieves current workflow traces
- `send_data_to_robonito(workflow_id: str = None) -> None` - Sends traces to server
- `trace_store.reset_current_workflow() -> None` - Clears current workflow traces


## Best Practices

1. **Use descriptive agent IDs**: Choose meaningful names for your agents
2. **Tool naming**: Provide clear tool names for better trace readability  
3. **Memory operations**: Always specify "READ" or "WRITE" for memory tracing
4. **Workflow management**: Clear traces between different workflow executions if needed

## Troubleshooting

### Common Issues

1. **Decorators not working**: Ensure you're using the correct import paths
2. **Server connection**: Verify `ROBONITO_URL` is correctly configured
