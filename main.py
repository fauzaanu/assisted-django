from AssistedDjango.DjangoApplication import DjangoApplication


def enhance_django_app():
    app_name = "fakebook_clone"  # replace with your actual Django app name
    app_directory = "Basic/fakebook_clone"  # replace with your actual Django app directory

    with open("fakebook_clone", "r") as f:  # Replace "README.md" with your actual README file
        purpose = f.read()

    django_app = DjangoApplication(app_name, purpose, app_directory)
    django_app.generate(better_brief=True)


if __name__ == '__main__':
    enhance_django_app()
