"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from qa import views
admin.autodiscover()
#from qa.urls import url

urlpatterns = [
#	url(r'^/$', views.all_questions, name='all'),
	url(r'^$', views.all_questions, name='all_questions'),
	url(r'^popular/$', views.popular, name='popular'),
	url(r'^question/(?P<question_id>\d+)/$', views.one_question, name='question'),
#	url(r'^$', include('qa.urls')),
	url(r'^login/.*', include('qa.urls')),
	url(r'^signup/.*', include('qa.urls')),
	url(r'^question/\w+/.*', include('qa.urls')),
	url(r'^ask/.*', include('qa.urls')),
	url(r'^popular/.*', include('qa.urls')),
	url(r'^new/.*', include('qa.urls')),
]
