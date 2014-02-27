from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangobootstrap2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


'''
To just play around with base.html file to check if bootstrap is functioning properly, add :

from django.views.generic import TemplateView
url(r'^base/', TemplateView.as_view(template_name="base.html")),

in this urls.py file
'''
