import os
import logging

from AssistedDjango.PromptEngine import ModelPromptEngine, FormsPromptEngine, ViewsPromptEngine, URLPromptEngine, \
    TestPromptEngine, AdminPromptEngine
from AssistedDjango.Prompter import OpenAISettings

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

    def clean_file(self,file_content):
        clean_string = [
            "```python",
            "```",
        ]
        for string in clean_string:
            if string in file_content:
                logging.info(f"Removing {string} from file")
                file_content = file_content.replace(string, "")

        return file_content

    def generate(self):
        """
        This function generates the content for the Django application.

        :param cycles: Number of cycles to run the improve_file method.
        :type cycles: int
        :return: None
        :rtype: None
        """
        # openai client
        oai_client = OpenAISettings()

        # 1. Create the models for the project brief
        logging.info("Creating models.py")
        models_prompt = ModelPromptEngine(self.purpose)
        system, prompt = models_prompt.get_prompt()
        models_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'models.py'), 'w') as f:
            models_file_content = self.clean_file(models_file_content)
            f.write(models_file_content)
            logging.info("models.py Updated!")

        # 2. Create the forms for the models
        logging.info("Creating forms.py")
        forms_prompt = FormsPromptEngine(models_file_content)
        system, prompt = forms_prompt.get_prompt()
        forms_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'forms.py'), 'w') as f:
            f.write(forms_file_content)
            logging.info("forms.py Updated!")

        # 3. Create the views for the forms
        logging.info("Creating views.py")
        views_prompt = ViewsPromptEngine(models_file_content, self.purpose)
        system, prompt = views_prompt.get_prompt()
        views_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'views.py'), 'w') as f:
            views_file_content = self.clean_file(views_file_content)
            f.write(views_file_content)
            logging.info("views.py Updated!")

        # 4. Create the urls for the views
        logging.info("Creating urls.py")
        urls_prompt = URLPromptEngine(views_file_content, self.purpose)
        system, prompt = urls_prompt.get_prompt()
        urls_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'urls.py'), 'w') as f:
            urls_file_content = self.clean_file(urls_file_content)
            f.write(urls_file_content)
            logging.info("urls.py Updated!")

        # 5. Create the admin for the models
        logging.info("Creating admin.py")
        admin_prompt = AdminPromptEngine(models_file_content)
        system, prompt = admin_prompt.get_prompt()
        admin_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'admin.py'), 'w') as f:
            admin_file_content = self.clean_file(admin_file_content)
            f.write(admin_file_content)
            logging.info("admin.py Updated!")

        # 6. Create the tests for the views
        logging.info("Creating tests.py")
        tests_prompt = TestPromptEngine(views_file_content, self.purpose)
        system, prompt = tests_prompt.get_prompt()
        tests_file_content = oai_client.prompt(system, prompt)
        with open(os.path.join(self.directory, 'tests.py'), 'w') as f:
            tests_file_content = self.clean_file(tests_file_content)
            f.write(tests_file_content)
            logging.info("tests.py Updated!")
