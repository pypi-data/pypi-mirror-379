import requests
from agent_tracing.database import trace_store
from agent_tracing.load_env import load_env
import os


load_env()

def send_data_to_robonito(workflow_id=None):
    if workflow_id:
        data = trace_store.get_workflow(workflow_id=workflow_id)
    else:
        data = trace_store.get_workflow()
    url = os.environ.get("ROBONITO_URL")   or 'http://localhost:3001/add-data'

    print("URL:", url)
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Unable to send the data:", e)
