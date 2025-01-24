## Getting Started

### Prerequisites

Download python latest version and install.

### Installation
create main directory for Django project

install python 
check if python installed successfully

01.create virtual environment

python -m venv env_name

02. active virtual environment

cd/env_name/Scripts/activate

03. install Django 

pip install Django

04. check Django installation

pip list

05. create new project (for current folder add .)

django-admin startproject project_name .

06. start development server

python manage.py runserver

07. creating new module (app)

django-admin startapp app_name


08. register app in setting in INSTALLED_APPS=

INSTALLED_APPS = [
    ...,
    "polls.apps.PollsAppConfig",
    ...,
]

09. register app urls in urls 

urlpatterns = [

path('task/',include("task.urls"))

]


10. create urls in app 

urlpatterns = [

path('task/',task)

]


11. generate requirement ( be sure active venv)

pip freeze > requirements.txt

12. install with requirement 

pip install -r requirements.txt



------------------------------------------------------

install and integrate tailwind css

13. create templates for html file in app

templates

14. register folder name in settings

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],  //if create outside app else keep remai empty
        "APP_DIRS": True,
        "OPTIONS": {
            # ... some options here ...
        },
    },
]

15. if used pretier kip it off.

16. static file and folder 

static/
css/
js/
image/


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


17. call static file

at the top of page 

{% static %}

<a href="{% static 'css/style.css' %}">


18. install tailwind 

npm install -D tailwindcss postcss autoprefixer

npx tailwindcss init


19. add tailwind to postcss

postcss.config.js

20. configure code 


module.exports = {
	plugins : {
		tailwindcss: {},
		autoprefixer: {},
	},

};

21. configure template path in tailwind.config.js


/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Templates inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};


22. add tailwind directives -- static/css/tailwind.css


@tailwind base;
@tailwind components;
@tailwind utilities;


23. start tailwind cli build process  -- package.json


{
  "devDependencies": {
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.16"
  },
  "scripts": {
    "build:tailwind": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --minify",
    "watch:tailwind": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch"
  }
}



24. run tailwind build 

npm run build:tailwind

25. use builded css file

{% load static %}

<a href="{% static 'css/output.css' %}">

26. run watch


npm run watch:tailwind



---------------------------------------------------------------

setup database postgreeSQL in setting

27. setup database 


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


28. install database connection plugins

from psycopg - binary

pip install psycopg-binary


29.make  migrate database 

python manage.py makemigrations

30. migration to database 

python manage.py migrate


-------------------------------------
django shell

31. open python shell

python manage.py shell

















































