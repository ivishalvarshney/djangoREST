# djangoREST
This repo have python django 2.1 framework with REST features. This is mostly for the beginners who want to integrate django-rest-framework.

###### Prerequisites : 
1)	Python version >= 3.6.5
Check the version by python --version
2)	Django version >= 2.1
Check the version by python -m django –version
3) Django-rest-framework

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
