from django.shortcuts import render
from django.shortcuts import render
import datetime
from django.contrib import messages
from userStory.views import getProject
from userStory.models import UserStory
from sprint.models import Sprint,UserStory_of_Sprint
from login.views import getNowUser

def addSprint(request):
    userStories = UserStory.objects.filter(nameProject=getProject().name).filter(status="Not Done")
    
    return render(request,'addSprint/addSprint.html',{'userStories': userStories,'today':str(datetime.datetime.now().date())})

def saveSprint(request):
    sprintName = request.POST.get('sprintName', None)
    userStoriesChoose = request.POST.getlist('userStoriesChoose', [])
    endDate = request.POST.get('endDate', None)
    now_project = getProject()
    if userStoriesChoose:
        sprint = Sprint(nameSprint = sprintName ,nameProject = now_project.name , dateEnd = endDate)
        sprint.save()
        
        for u in userStoriesChoose:
            story = UserStory.objects.filter(content = u)[0]
            u_o_s = UserStory_of_Sprint(pk_sprint=sprint.id,pk_userStory=story.id)
            u_o_s.save()
        return showSprint(request)
    messages.error(request,"You need to choose user story... try again")
    return addSprint(request)


def showSprint(request): 
    user=getNowUser()
    project=getProject()
    allsprint=reversed(Sprint.objects.filter(nameProject=project.name))
    return render(request,'showSprint/showSprints.html',{'user':user,'project':project,'sprints':allsprint})