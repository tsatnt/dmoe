"""DE_001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from model_app import views as model_views
from apscheduler.scheduler import Scheduler

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', model_views.gate),
    url(r'^login/', model_views.login),
    url(r'^acount/', model_views.acount),
    url(r'^manual/', model_views.manual),
    url(r'^market/', model_views.market),
    url(r'^md0001d/', model_views.md0001d),
    url(r'^md0001m/$', model_views.md0001m),
    url(r'^md0002d/', model_views.md0002d),
    url(r'^md0002m/$', model_views.md0002m),
    url(r'^md0003d/', model_views.md0003d),
    url(r'^md0003m/$', model_views.md0003m),
    url(r'^md0004d/', model_views.md0004d),
    url(r'^md0004m/$', model_views.md0004m),
    url(r'^md0005d/', model_views.md0005d),
    url(r'^md0005m/$', model_views.md0005m),
    url(r'^md0006d/', model_views.md0006d),
    url(r'^md0006m/$', model_views.md0006m),
    url(r'^md0007d/', model_views.md0007d),
    url(r'^md0007m/$', model_views.md0007m),
]

urlpatterns += staticfiles_urlpatterns()
