# Django Project Setup and Configuration

This guide provides a step-by-step process to set up a Django project, integrate Tailwind CSS, and configure PostgreSQL as the database backend.

---

## Setting Up the Django Project

### 1. Install Python
Ensure Python is installed on your system and verify the installation:
```bash
python --version
```

### 2. Create a Virtual Environment
```bash
python -m venv env_name
```

### 3. Activate the Virtual Environment
```bash
cd env_name/Scripts/activate
```

### 4. Install Django
```bash
pip install Django
```

### 5. Verify Django Installation
```bash
pip list
```

### 6. Create a New Django Project
To create a new project in the current folder:
```bash
django-admin startproject project_name .
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

### 8. Create a New App
```bash
django-admin startapp app_name
```

### 9. Register the App in Settings
Add the app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ..., 
    "polls.apps.PollsAppConfig", 
    ..., 
]
```

### 10. Register App URLs in Main URLs
Add the following to `urlpatterns` in `urls.py`:
```python
urlpatterns = [
    path('task/', include("task.urls"))
]
```

### 11. Create URLs in the App
In the app's `urls.py`, define your routes:
```python
urlpatterns = [
    path('task/', task)
]
```

### 12. Generate and Install Requirements
Generate a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```
Install dependencies from the file:
```bash
pip install -r requirements.txt
```

---

## Integrating Tailwind CSS

### 13. Create HTML Templates
Organize templates within your app or at the project level:
```
app_name/templates/
```

### 14. Register Templates Folder in Settings
In `settings.py`, update the `TEMPLATES` configuration:
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            # Additional options
        },
    },
]
```

### 15. Disable Prettier (if applicable)
If using Prettier, ensure it is disabled to avoid conflicts.

### 16. Configure Static Files
Create a folder structure:
```
static/
  css/
  js/
  images/
```
Add to `settings.py`:
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

### 17. Load Static Files in Templates
At the top of your template:
```django
{% load static %}
```
Example usage:
```html
<a href="{% static 'css/style.css' %}"></a>
```

### 18. Install Tailwind CSS
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

### 19. Configure PostCSS
Update `postcss.config.js`:
```javascript
module.exports = {
    plugins: {
        tailwindcss: {},
        autoprefixer: {},
    },
};
```

### 20. Configure Tailwind Template Path
In `tailwind.config.js`:
```javascript
module.exports = {
    content: [
        "./templates/**/*.html",
        "./**/templates/**/*.html",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
```

### 21. Add Tailwind Directives
In `static/css/tailwind.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 22. Build Tailwind CSS
Update `package.json`:
```json
{
  "scripts": {
    "build:tailwind": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --minify",
    "watch:tailwind": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch"
  }
}
```
Run the build process:
```bash
npm run build:tailwind
```
Use the built CSS:
```django
<link href="{% static 'css/output.css' %}" rel="stylesheet">
```
Start the watch process:
```bash
npm run watch:tailwind
```

---

## Configuring PostgreSQL Database

### 23. Update Database Settings
In `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_management',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

### 24. Install PostgreSQL Driver
```bash
pip install psycopg-binary
```

### 25. Apply Migrations
Generate migration files:
```bash
python manage.py makemigrations
```
Apply migrations to the database:
```bash
python manage.py migrate
```

---

## Additional Tools and Debugging

### 26. Open Django Shell
```bash
python manage.py shell
```

### 27. Install Django Debug Toolbar
```bash
pip install django-debug-toolbar
```

### 28. Configure Debug Toolbar
Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    "debug_toolbar",
]
```

Update `urls.py`:
```python
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    ...
] + debug_toolbar_urls()
```

Add middleware:
```python
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
```
Configure internal IPs:
```python
INTERNAL_IPS = [
    "127.0.0.1",
]
```

---

## Database Reset

### 29. Delete Database Migrations
Delete the database and all migration files except `__init__.py` in each app's migrations folder.

### 30. Recreate Migrations
Generate migration files:
```bash
python manage.py makemigrations
```
Apply migrations:
```bash
python manage.py migrate
```

---

## Additional Libraries

### 31. Install Faker Library
```bash
pip install Faker
