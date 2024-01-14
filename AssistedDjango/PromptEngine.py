from AssistedDjango.BasePromptEngine.BasePromptEngine import ModelBriefPromptEngine, \
    BriefPromptEngine
from AssistedDjango.examples import VIEWS_EXAMPLE, URLS_EXAMPLE, ADMIN_EXAMPLE, TESTS_EXAMPLE, FORMS_EXAMPLE, \
    MODEL_EXAMPLE, SIGNALS_EXAMPLE


class ModelPromptEngine(BriefPromptEngine):
    # Models.py should have access to the brief
    def __init__(self, brief):
        super().__init__(brief)
        self.file = 'models.py'
        self.example = MODEL_EXAMPLE


class FormsPromptEngine(BriefPromptEngine):
    # Forms.py should have access to the models.py
    def __init__(self, generated_models_file):
        super().__init__(generated_models_file)
        self.file = 'forms.py'
        self.example = FORMS_EXAMPLE


class ViewsPromptEngine(ModelBriefPromptEngine):
    # Views.py should have access to the brief and models.py
    def __init__(self, generated_models_file, brief):
        super().__init__(generated_models_file, brief)
        self.file = 'views.py'
        self.example = VIEWS_EXAMPLE


class URLPromptEngine(ViewsPromptEngine):
    # Urls.py should have access to the views.py
    def __init__(self, generated_views_file, brief):
        super().__init__(generated_views_file, brief)
        self.file = 'urls.py'
        self.example = URLS_EXAMPLE


class AdminPromptEngine(BriefPromptEngine):
    # Admin.py should have access to the models.py
    def __init__(self, generated_models_file):
        super().__init__(generated_models_file)
        self.file = 'views.py'
        self.example = ADMIN_EXAMPLE


class TestPromptEngine(ViewsPromptEngine):
    # Tests.py should have access to the views.py
    def __init__(self, generated_views_file, brief):
        super().__init__(generated_views_file, brief)
        self.file = 'tests.py'
        self.example = TESTS_EXAMPLE


class SignalsPromptEngine(ModelBriefPromptEngine):
    # Views.py should have access to the brief and models.py
    def __init__(self, generated_models_file, brief):
        super().__init__(generated_models_file, brief)
        self.file = 'signals.py'
        self.example = SIGNALS_EXAMPLE
