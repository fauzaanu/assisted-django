import os
from dotenv import load_dotenv
from openai import ChatCompletion, OpenAI


class Prompter:
    """

    The `Prompter` class is used to generate content for Django files using OpenAI's GPT-3.5 language model. It provides methods to generate content for specific files (`models.py`, `forms
    *.py`, `views.py`, `urls.py`, `admin.py`). The generated content is based on a given purpose.

    Usage Example:
    ```
    prompter = Prompter()
    models_content = prompter.models_prompt("Provide content for models.py file")
    forms_content = prompter.forms_prompt("Provide content for forms.py file")
    views_content = prompter.views_prompt("Provide content for views.py file")
    urls_content = prompter.urls_prompt("Provide content for urls.py file")
    admin_content = prompter.admin_prompt("Provide content for admin.py file")
    ```

    Methods:
        - `read_file_content(file_path)`: Reads the content of the file at the given `file_path` and returns it as a string.

        - `build_prompt(filename, purpose)`: Builds the prompt for generating content for the specified `filename` based on the given `purpose`. The prompt includes the dependent content
    * from other files. If an example file exists for the specified `filename`, the content of the example file is also included in the prompt. Returns the built prompt as a string.

        - `generate_content(filename, purpose)`: Generates the content for the specified `filename` based on the given `purpose`. Uses OpenAI's GPT-3.5 language model to generate the content
    *. Returns the generated content as a string.

        - `models_prompt(purpose)`: Generates the content for the `models.py` file based on the given `purpose`. Returns the generated content as a string.

        - `forms_prompt(purpose)`: Generates the content for the `forms.py` file based on the given `purpose`. Returns the generated content as a string.

        - `views_prompt(purpose)`: Generates the content for the `views.py` file based on the given `purpose`. Returns the generated content as a string.

        - `urls_prompt(purpose)`: Generates the content for the `urls.py` file based on the given `purpose`. Returns the generated content as a string.

        - `admin_prompt(purpose)`: Generates the content for the `admin.py` file based on the given `purpose`. Returns the generated content as a string.
    """

    def __init__(self):
        load_dotenv()
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.model = 'gpt-3.5-turbo'
        self.temperature = 0.1
        self.max_tokens = 2000
        self.content = {
            'models.py': '',
            'forms.py': '',
            'views.py': '',
            'urls.py': '',
            'admin.py': '',
        }

    def read_file_content(self, file_path):
        """
        Reads the content of a file.

        :param file_path: The path of the file to be read.
        :type file_path: str
        :return: The content of the file.
        :rtype: str
        """
        with open(file_path, 'r') as file:
            return file.read()

    def build_prompt(self, filename, purpose):
        """

        :param filename: The name of the file for which the prompt is being built.
        :type filename: str
        :param purpose: The purpose of the prompt.
        :type purpose: str
        :return: The built prompt.
        :rtype: str

        """
        dependent_content = ""

        if filename == 'forms.py':
            dependent_content = self.content['models.py']
        elif filename == 'views.py':
            dependent_content = self.content['models.py'] + "\n" + self.content['forms.py']
        elif filename in ['urls.py', 'tests.py']:
            dependent_content = self.content['models.py'] + "\n" + self.content['views.py']
        elif filename == 'admin.py':
            dependent_content = self.content['models.py'] + "\n" + self.content['views.py']

        prompt = f"{purpose}\n{dependent_content}"

        # Check if the example file exists
        example_file_path = os.path.join('examples', filename)
        if os.path.exists(example_file_path):
            example_content = self.read_file_content(example_file_path)
            instructions = "\nKeep your response exactly and strictly in the following format: "
            prompt = "\n".join([prompt, instructions, example_content])

        return prompt

    def generate_content(self, filename, purpose):
        """
        Generate content for a given file.

        :param filename: The name of the file.
        :type filename: str
        :param purpose: The purpose of the file.
        :type purpose: str
        :return: The generated content for the file.
        :rtype: str
        """
        prompt = self.build_prompt(filename, purpose)
        messages = [
            {"role": "system",
             "content": f"You are a django code generation application."},
            {"role": "user", "content": prompt}
        ]

        response = self.openai.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content

    def models_prompt(self, purpose):
        """
        Generates content for 'models.py' file based on the specified purpose.

        :param purpose: The purpose for generating the content.
        :type purpose: str

        :return: The generated content for 'models.py' file.
        :rtype: str
        """
        self.content['models.py'] = self.generate_content('models.py', purpose)
        return self.content['models.py']

    def forms_prompt(self, purpose):
        """
        :param purpose: The purpose of the generated forms.py file.
        :type purpose: str
        :return: The generated content of forms.py.
        :rtype: str
        """
        self.content['forms.py'] = self.generate_content('forms.py', purpose)
        return self.content['forms.py']

    def views_prompt(self, purpose):
        """
        Prompt the user for input and generate the content of the 'views.py' file.

        :param purpose: The purpose of the 'views.py' file.
        :type purpose: str
        :return: The generated content of the 'views.py' file.
        :rtype: str
        """
        self.content['views.py'] = self.generate_content('views.py', purpose)
        return self.content['views.py']

    def urls_prompt(self, purpose):
        """
        Function to prompt the user for input and generate the content for 'urls.py' file.

        :param purpose: The purpose or description of the generated 'urls.py' file.
        :type purpose: str
        :return: The generated content for 'urls.py' file.
        :rtype: str
        """
        self.content['urls.py'] = self.generate_content('urls.py', purpose)
        return self.content['urls.py']

    def admin_prompt(self, purpose):
        """
        :param purpose: The purpose of the admin_prompt method.
        :type purpose: str
        :return: The content of the 'admin.py' file generated by the method.
        :rtype: str
        """
        self.content['admin.py'] = self.generate_content('admin.py', purpose)
        return self.content['admin.py']
