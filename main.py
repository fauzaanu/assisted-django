from AssistedDjango.DjangoApplication import DjangoApplication


def enhance_django_app():
    app_name = "calorie_counter_app"  # replace with your actual Django app name
    app_directory = "Project/calorie_counter_app"  # replace with your actual Django app directory

    with open("caloriesapp.txt", "r") as f:  # Replace "README.md" with your actual README file
        purpose = f.read()

    django_app = DjangoApplication(app_name, purpose, app_directory)
    django_app.improve_app(cycles=1)  # Use enhance_django_app() instead of create_app()


if __name__ == '__main__':
    enhance_django_app()
