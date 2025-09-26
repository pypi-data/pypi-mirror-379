from typing import Optional
import uuid, time

class TraceStore:
    def __init__(self):
        self.data = {}
        self.current_workflow: Optional[str] = None

    def start_workflow(self, workflow_id=None):
        workflow_id = workflow_id or str(uuid.uuid4())
        self.data[workflow_id] = {"workflow_id": workflow_id, "agents": []}
        self.current_workflow = workflow_id
        return workflow_id

    def add_agent(self, agent_id=None):
        if not self.current_workflow:
            raise ValueError("No active workflow. Call start_workflow() first.")
        agent_id = agent_id or f"agent-{len(self.data[self.current_workflow]['agents'])+1}"
        self.data[self.current_workflow]["agents"].append({"agent_id": agent_id, "steps": []})
        return agent_id

    def log_step(self, agent_id, step_type, input_data, output_data, latency = 0,  tool_name=None):
        if not self.current_workflow:
            raise ValueError("No active workflow. Call start_workflow() first.")

        step = {
            "step_id": str(uuid.uuid4()),
            "type": step_type,
            "input": input_data,
            "output": output_data,
            "timestamp": time.time(),
            "latency": latency
        }
        if tool_name:
            step["tool_name"] = tool_name

        for agent in self.data[self.current_workflow]["agents"]:
            if agent["agent_id"] == agent_id:
                agent["steps"].append(step)
                break
        else:
            raise ValueError(f"Agent {agent_id} not found in current workflow {self.current_workflow}")

    def get_workflow(self, workflow_id=None):
        workflow_id = workflow_id or self.current_workflow
        return self.data.get(workflow_id, None)

    def reset_current_workflow(self, workflow_id):
        if workflow_id in self.data:
            del self.data[workflow_id]
        if self.current_workflow == workflow_id:
            self.current_workflow = None

    def reset_store(self):
        self.data.clear()
        self.current_workflow = None

trace_store = TraceStore()
