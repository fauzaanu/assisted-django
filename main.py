from AssistedDjango.DjangoApplication import DjangoApplication


def enhance_django_app():
    app_name = "checklist"  # replace with your actual Django app name
    app_directory = "Basic/manual_checklist"  # replace with your actual Django app directory

    with open("checklist", "r") as f:  # Replace "README.md" with your actual README file
        purpose = f.read()

    django_app = DjangoApplication(app_name, purpose, app_directory)
    django_app.generate()


if __name__ == '__main__':
    enhance_django_app()
