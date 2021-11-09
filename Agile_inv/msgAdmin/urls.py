from django.urls import path
from django.conf.urls import url,include
from  msgAdmin import views
from django.views.generic import TemplateView
app_name="msg"
urlpatterns = [
    url(r'^messagesPage$', views.messagesPage,name='messagesPage'),
    url(r'^messageSave$', views.messageSave,name='messageSave'),
]