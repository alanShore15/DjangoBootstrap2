                                                  DjangoBootstrap2
========================================================================================================================

Integrating Django with Bootstrap 2.3.2
------------------------------------------------------------------------------------------------------------------------

Django 1.6.1 has been integrated with Bootstrap 2.3.2. 

Since there are major changes in Bootstrap 3, people familiar with Bootstrap 2.3.2 can use this project in their Django 
project.

Bootstrap files have been added in the 'static' folder and the 'base.html' file is used to call these bootstrap files.

To check if this actually works, just add 

from django.views.generic import TemplateView
url(r'^base/', TemplateView.as_view(template_name="base.html")),

in your urls.py file and run http://localhost:8000/base/ or http://127.0.0.1:8000/base/ on your local machine.

-------------------------------------------------------------------------------------------------------------------------
