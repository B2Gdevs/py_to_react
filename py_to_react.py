"""
This script is the backend api parser that parsers the fast api backend code and generates the react frontend code.

We read the docstring of each function and parse the json example and the visual description, pass that to the 
AI, and get the react code.

docstring example:
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

# First we need to import the functions from the backend code
from todo_backend import router
from backend_to_frontend_chains import FrontendGenChainCreator
# from meeting_analyzer_chains import MeetingAnalyzerChainCreator
import inspect

# we around going to use the inspect module to get the docstring of each function from the router
def get_docstring(func):
    return inspect.getdoc(func)

# We need to get the docstring of each function in the router
def get_functions(router):
    functions = []
    for route in router.routes:
        functions.append(route.endpoint)
    return functions

# We need to parse the docstring to get the json example and the visual description
def parse_docstring(docstring):
    # We need to split the docstring into the does, example, and visual description
    docstring = docstring.split("Example:")
    does = docstring[0].split("Does:")[1]
    example = docstring[1].split("Visual Description:")[0]
    visual_description = docstring[1].split("Visual Description:")[1]

    # We need to parse the example to get the json example
    example = example.split("\n")
    example = [line.strip() for line in example]
    example = [line for line in example if line]
    example = "".join(example)
    example = example.replace("'", '"')

    # We need to parse the visual description to get the react code
    visual_description = visual_description.split("\n")
    visual_description = [line.strip() for line in visual_description]
    visual_description = [line for line in visual_description if line]
    visual_description = "".join(visual_description)
    visual_description = visual_description.replace("'", '"')

    return does, example, visual_description

if __name__ == "__main__":
    try:
        react_chain = FrontendGenChainCreator.create_react_component_chain()
        for func in  get_functions(router):
            docstring = get_docstring(func)
            # print(parse_docstring(docstring))
            # print(docstring)
            print("backend function: ", func)
            print("\n\nReact:")
            print(react_chain(docstring))
            with open("react_code.txt", "a") as f:
                f.write(f"\n\n===================\n\n{react_chain(docstring)}")
            # break
    except Exception as e:
        print(e)
        # print(func)