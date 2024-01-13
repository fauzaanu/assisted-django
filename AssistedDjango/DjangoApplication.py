import os
import logging

from AssistedDjango.PromptEngine import ModelPromptEngine, FormsPromptEngine, ViewsPromptEngine, URLPromptEngine, \
    TestPromptEngine, AdminPromptEngine
from AssistedDjango.Prompter import Prompter, OpenAISettings

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')


class DjangoApplication:
    """
    This class represents a Django application.
    """

    def __init__(self, name, purpose, directory):
        self.name = name
        self.purpose = purpose
        self.directory = directory
        self.filepath_mapping = {}
        self.prompter = Prompter()

    def improve_app(self):
        """
        Improve the application by calling improve_file method for given number of cycles.

        :param cycles: Number of cycles to run the improve_file method.
        :type cycles: int
        :return: None
        :rtype: None
        """
        # openai client
        oai_client = OpenAISettings()

        # 1. Create the models for the project brief
        models_prompt = ModelPromptEngine(self.purpose)
        system, prompt = models_prompt.get_prompt()
        models_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'models.py'), 'w') as f:
            f.write(models_file_content)

        # 2. Create the forms for the models
        forms_prompt = FormsPromptEngine(models_file_content)
        system, prompt = forms_prompt.get_prompt()
        forms_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'forms.py'), 'w') as f:
            f.write(forms_file_content)

        # 3. Create the views for the forms
        views_prompt = ViewsPromptEngine(models_file_content, self.purpose)
        system, prompt = views_prompt.get_prompt()
        views_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'views.py'), 'w') as f:
            f.write(views_file_content)

        # 4. Create the urls for the views
        urls_prompt = URLPromptEngine(views_file_content)
        system, prompt = urls_prompt.get_prompt()
        urls_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'urls.py'), 'w') as f:
            f.write(urls_file_content)

        # 5. Create the admin for the models
        admin_prompt = AdminPromptEngine(models_file_content)
        system, prompt = admin_prompt.get_prompt()
        admin_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'admin.py'), 'w') as f:
            f.write(admin_file_content)

        # 6. Create the tests for the views
        tests_prompt = TestPromptEngine(views_file_content)
        system, prompt = tests_prompt.get_prompt()
        tests_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'tests.py'), 'w') as f:
            f.write(tests_file_content)
