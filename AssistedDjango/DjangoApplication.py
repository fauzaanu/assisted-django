import os
import logging

from AssistedDjango.Prompter import Prompter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')


class DjangoApplication:
    """
    :class: DjangoApplication

    A class that represents a Django application.

    :param name: The name of the Django application.
    :type name: str
    :param purpose: The purpose of the Django application.
    :type purpose: str
    :param directory: The directory path of the Django application.
    :type directory: str

    :ivar name: The name of the Django application.
    :ivar purpose: The purpose of the Django application.
    :ivar directory: The directory path of the Django application.
    :ivar filepath_mapping: A dictionary mapping file names to their absolute file paths.
    :ivar prompter: An instance of Prompter class.

    .. automethod:: improve_app
    .. automethod:: improve_file
    .. automethod:: _write_to_file
    """
    def __init__(self, name, purpose, directory):
        self.name = name
        self.purpose = purpose
        self.directory = directory
        self.filepath_mapping = {}
        self.prompter = Prompter()

    def improve_app(self, cycles=1):
        """
        Improve the application by calling improve_file method for given number of cycles.

        :param cycles: Number of cycles to run the improve_file method.
        :type cycles: int
        :return: None
        :rtype: None
        """
        for _ in range(cycles):
            for filename in ['models.py', 'forms.py', 'views.py', 'urls.py', 'tests.py', 'admin.py', 'apps.py']:
                self.improve_file(filename)

    def improve_file(self, filename):
        """
        Improve the content of a file.

        :param filename: The name of the file to be improved.
        :type filename: str
        :return: None
        :rtype: None
        """
        absolute_file_path = os.path.join(self.directory, filename)

        # Ensure the file exists
        if not os.path.isfile(absolute_file_path):
            logging.error(f"{filename} does not exist in {self.name} application directory.")
            return

        # Ensure the method to prompt improved content exists
        prompt_method = getattr(self.prompter, f"{filename.split('.')[0]}_prompt", None)
        if not prompt_method:
            logging.error(f"No corresponding method found in Prompter for improving {filename}")
            return

        # Generate improved content
        improved_content = prompt_method(self.purpose)

        # Write the improved content to the file (overwriting existing content)
        try:
            with open(absolute_file_path, 'w') as f:
                f.write(improved_content)
            self.filepath_mapping[filename] = absolute_file_path
            logging.info(f"Updated file {absolute_file_path}")  # Log the absolute file path
        except Exception as e:
            logging.error(f"Failed to update file {absolute_file_path}: {str(e)}")

    def _write_to_file(self, file_path, content):
        """
        :param file_path: The path to the file where the content will be written.
        :type file_path: str
        :param content: The content to be written to the file.
        :type content: str
        :return: None
        :rtype: None

        This method writes the given content to the specified file. It replaces any occurrence of "```" and "```python" with an empty string in the content before writing it to the file. After
        * successful writing, it updates the filepath_mapping dictionary with the file name as the key and the absolute file path as the value. It also logs the absolute file path using the
        * logging module. If an exception occurs during the writing process, an error message is logged.
        """
        try:
            # TODO:replace possible backslashes with forward slashes left by openai
            # ``` and ```python
            content = content.replace("```", "").replace("```python", "")
            with open(file_path, 'w') as f:
                f.write(content)
            file_name = os.path.basename(file_path)  # Extract file_name from the absolute file_path
            self.filepath_mapping[file_name] = file_path
            logging.info(f"Updated file {file_path}")  # Log the absolute file path
        except Exception as e:
            logging.error(f"Failed to update file {file_path}: {str(e)}")
