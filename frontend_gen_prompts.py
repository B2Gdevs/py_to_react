from formatted_prompt_template import FormattedPromptTemplate

class FrontendGenTemplateCreator:
    @staticmethod
    def create_react_component_prompt_template() -> FormattedPromptTemplate:
        react_format = """
        This format is react jsx and replace the text with the appropriate component given the json data that will come from a backend API.
        Wrap the generated component in a div tag in the provided format.
        Components will be functional components.
        Do not return anything but the component formmatted in jsx to copy and paste in to the codebase.

        """

        action_template = """
        You are a helpful assistant creates react components given a docstring with the following format:
        
        {format}
        """
        return FormattedPromptTemplate(action_template=action_template, format=react_format)