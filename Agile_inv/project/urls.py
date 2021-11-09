from django.urls import path
from django.conf.urls import url,include
from  project import views
from django.views.generic import TemplateView
app_name="project"
urlpatterns = [
    url(r'^deleteProject/(?P<nameProject>[a-zA-Z0-9]+)$', views.deleteProject,name='deleteProject'),
    url(r'^projectsPage$', views.createPro,name='createPro'),
    url(r'^addProject$', views.buttonAddProject,name='buttonAddProject'),
    url(r'^saveNewProject$', views.saveNewProject,name='saveNewProject'),
    


]