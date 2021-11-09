from django.urls import path
from django.conf.urls import url,include
from  login import views
from django.views.generic import TemplateView
app_name="login"
urlpatterns = [
    path('', views.homePage,name='homePage'),
    path('login', views.submit_login,name='submit_login'),
    path('registration', views.submit_registration,name='submit_registration'),
    url(r'^registerpage/$', TemplateView.as_view(template_name='registerPage/register.html'), name='register'),
    path('overview', views.returnOverview,name='returnOverview'),
]