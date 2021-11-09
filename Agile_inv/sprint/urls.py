from django.urls import path
from django.conf.urls import url,include
from sprint import views

app_name="sprint"
urlpatterns = [
    url(r'^addSprint$', views.addSprint,name='addSprint'),
    url(r'^showSprint$', views.showSprint,name='showSprint'),
    url(r'^saveSprint$', views.saveSprint,name='saveSprint'),

]