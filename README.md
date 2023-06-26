# README.md

---

## Backend API Parser for React Code Generation

This script is an innovative solution that converts backend Python code into frontend React components. 

The concept is straightforward: It reads the docstrings from each function of a FastAPI router and generates respective React code. The docstring needs to follow a specific format, providing a brief description of what the function does, an example of the JSON output, and a visual description of the expected frontend component.

Here is an example of the required docstring structure:

```python
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
```

## How it works?

The script starts by importing functions from the backend FastAPI router, using Python's `inspect` module to access the docstrings. It then parses the docstring into a description, an example, and a visual description. The visual description gets converted into corresponding React code by a chain generator - `FrontendGenChainCreator`.

Here is an example of how the Python function with a properly formatted docstring will be converted into a React component.

Consider this Python function in your FastAPI router:

```python
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
```

The script will parse the docstring of this function and generate the following React component:

```jsx
<div style={{textAlign: 'center'}}>
  <form>
    <label htmlFor="task_name">Task Name:</label><br />
    <input type="text" id="task_name" name="task_name" /><br />
    <label htmlFor="task_description">Task Description:</label><br />
    <textarea id="task_description" name="task_description"></textarea><br />
    <button style={{backgroundColor: 'green', color: 'white'}} type="submit">Create Task</button>
  </form>
</div>
```

## Usage

The core logic resides in the `if __name__ == "__main__":` block. The script goes through all the functions in the FastAPI router, parses their docstrings, and generates the corresponding React components. It prints these components on the console and appends them in a file named `react_code.txt` for later reference.

## Limitations & Future Work

The current version assumes that the backend code uses FastAPI and the frontend code is based on React. Also, it requires a specific docstring format. In future versions, we plan to generalize this tool to be compatible with different backend and frontend frameworks, and also allow for more flexibility in the docstring format.

## Conclusion

This tool has the potential to reduce development time