"""
This script is a Proof of Concept for generating a React component from a Python function given the visual description
of the component in natural language. The json output of a python function, the python function and it's docstring.

We will be making the iconic TODO app.  Python will be used for the Create, Update, Delete and Read operations.
The frontend will create buttons with react having the onclick functions to call the python functions.
The python functions will be using FastAPI to create the API endpoints.

Each python function will have an example of it's json output in the docstring.
"""
# The fast api code
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter

class Task(BaseModel):
    task_name: str
    task_description: str

# The "database"
tasks = []


router = APIRouter()


@router.post("/create_task")
def create_task(task_name: str, task_description: str) -> dict:
    """
    Does:
        Creates a task with the given name and description.
        Adds the task to the tasks list.

    Example:
        {
            "task_name": "task_name",
            "task_description": "task_description"
        }

    Visual Description:
        A form with two input fields, one for the task name and one for the task description.
        A button to submit the form. The button will say "Create Task".
        Using Inline styling, the button will be green and the form will be centered.
    """
    task = {
        "task_name": task_name,
        "task_description": task_description
    }
    tasks.append(task)
    return task

@router.put("/update_task")
def update_task(task_name: str, task_description: str) -> dict:
    """
    Does:
        Updates a task with the given name and description in the tasks list.

    Example:
        {
            "task_name": "task_name",
            "task_description": "task_description"
        }

    Visual Description:
        A form with two input fields, one for the task name and one for the task description.
        A button to submit the form. The button will say "Update Task".
        Using Inline styling, the button will be blue and the form will be centered.
    """
    task = {
        "task_name": task_name,
        "task_description": task_description
    }
    for i in range(len(tasks)):
        if tasks[i]["task_name"] == task_name:
            tasks[i] = task
            break
    return task

@router.delete("/delete_task")
def delete_task(task_name: str) -> dict:
    """
    Does:
        Deletes a task with the given name from the tasks list.

    Example:
        {
            "task_name": "task_name",
            "task_description": "task_description"
        }
        
    Visual Description:
        A form with one input field for the task name.
        A button to submit the form. The button will say "Delete Task".
        Using Inline styling, the button will be red and the form will be centered.
    """
    task = {
        "task_name": task_name
    }
    for i in range(len(tasks)):
        if tasks[i]["task_name"] == task_name:
            tasks.pop(i)
            break
    return task

@router.get("/read_task")
def read_task(task_name: str) -> dict:
    """
    Does:
        Reads a task with the given name from the tasks list.

    Example:
        {
            "task_name": "task_name"
        }
    
    Visual Description:
       A paragraph with the task name and task description.
       Using inline styling, the paragraph will be centered, the task name will be bold and the task description will be italic.
    """
    task = None
    for i in range(len(tasks)):
        if tasks[i]["task_name"] == task_name:
            task = tasks[i]
            break
    return task

# create the fastapi app, and pull in the routes from the router
def create_app():
    app = FastAPI()
    app.include_router(router)
    return app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="127.0.0.1", port=8000)