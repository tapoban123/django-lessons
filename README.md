# Learning Django

1. Install [virutalenv](https://virtualenv.pypa.io/en/latest/user_guide.html)
   ```
   pip install virtualenv
   ```
2. Activate env

3. Install django
   ```
   pip install django
   ```
4. Create a django project
    ```
    django-admin startproject <project_name>
    ```

5. Create an app inside project.
    ```
    python manage.py startapp <app_name>
    ```

    Each feature (e.g. home, auth, etc.) is treated as an app inside a django project.

6. Run the django server in localhost.
    ```
    python manage.py runserver <0.0.0.0:5000> [MENTION PORT OPTIONAL]
    ```

7. Add all your apps inside settings.py -> Installed apps
    ``` python
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    EXTERNAL_APPS = [
        "home",
    ] 

    INSTALLED_APPS += EXTERNAL_APPS
    ```

