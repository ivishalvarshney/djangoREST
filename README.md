# djangoREST
This repo have python django 2.1 framework with REST features. This is mostly for the beginners who want to integrate django-rest-framework and want to work on rest API's.

###### Prerequisites : 
1)	Python version >= 3.6.5
Check the version by python --version
2)	Django version >= 2.1
Check the version by python -m django –version
3) [Django-rest-framework] (https://github.com/encode/django-rest-framework/tree/master)

###### To install djangorestframework : 
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

## STEP 1 : Project Installation

If you have already have django app then directly go to STEP 3 and if you are starting django application through scratch follow the below command
-	Go to the directory /home/mycode ( recommended )  or /var/www/html/
-	django-admin startproject <mysite>

## STEP 2 : Configuration

-	Open settings.py file from mysite > mysite directory .
    - Check if your ip is in ALLOWED_HOSTS = [] if not add it.

## STEP 3: App installation and configuration
For module based installation and configuration. Click on the below link.
1. [rest]()
2. [basicREST]()

## STEP 4 : Run server

- Run the command from root directory `python manage.py runserver <IP>:<PORT>`
- Example: `python manage.py runserver 12.34.190.111:9999`

**It will show the output like:**

```
Performing system checks...

System check identified no issues (0 silenced).
January 23, 2019 - 16:11:30
Django version 2.1.2, using settings 'djangoREST.settings'
Starting development server at http://12.34.190.111:9999/
Quit the server with CTRL-BREAK.
```

