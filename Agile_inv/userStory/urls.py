from django.urls import path
from django.conf.urls import url,include
from userStory import views
from django.views.generic import TemplateView
app_name="userStory"
urlpatterns = [
    url(r'^delete_story/(?P<id>\d+)/$', views.delete_story,name='delete_story'),
     url(r'^delete_user/(?P<id>\d+)/$', views.delete_user,name='delete_user'),
    url(r'^userStoryPage/(?P<nameProject>[a-zA-Z0-9]+)/$', views.userStoryPage,name='userStoryPage'),
    path('insertStory', views.insertStory,name='insertStory'),
    path('submit_story', views.submit_story,name='submit_story'),
    path('filterMyStory', views.filterMyUserStory,name='filterMyStory'),
    url(r'^updateToDone/(?P<id>\d+)/$', views.updateToDone,name='updateToDone'),
    path('FilterNotDone', views.FilterNotDone,name='FilterNotDone'),
    path('allStories', views.allStories,name='allStories'),
    url(r'^updateUserStory/(?P<id>\d+)/$', views.updateUserStory,name='updateUserStory'),
    url(r'^updateAction/(?P<id>\d+)/$', views.updateAction,name='updateAction'),
    path('testF', views.testF,name='testF'),
    path('returnHomeProject', views.returnHomeProject,name='returnHomeProject'),

    
]
