from django.shortcuts import render
from userStory.models import UserStory
from login.models import User
from project.models import User_of_project,Project
from project.views import getNowUser,createPro
from sprint.models import Sprint,UserStory_of_Sprint
from msgAdmin.models import msg
from django.contrib import messages




def returnHomeProject(request):
    userName=getNowUser()
    return createPro(request)


def userStoryPage(request,nameProject):
    my_stories = UserStory.objects.filter(nameProject=nameProject)
    global project
    project=Project.objects.get(name=nameProject)
    userOfProject=User_of_project.objects.filter(pk_project=nameProject) 
    sprint =Sprint.objects.filter(nameProject=nameProject).last()
    return render(request,'storiesView/storiesView.html',{'sprint':sprint,'stories':(my_stories),'project':(project),'userOfProject':(userOfProject),'user':getNowUser()})


def insertStory(request):
    ufp = User_of_project.objects.filter(pk_project=project.name)
    my_users=[]
    for x in ufp:
        my_users+=[User.objects.get(userName=x.pk_user)]
    return render(request,'createStory/createStory.html',{'users':(my_users),'range':(range(1,6))}) 


def submit_story(request):
    AssignTo = request.POST.get('Assign', None)
    Priority = request.POST.get('Priority', None) 
    Content = request.POST.get('Content', None) 
    if AssignTo!="None" and Priority!="None":
        story = UserStory(nameProject=project.name,content=Content,priority=Priority,assign=AssignTo)
        story.save()
        return userStoryPage(request,project.name)
    messages.error(request,"You are missing priority or assing to user ")
    return insertStory(request)

def delete_story(request,id):
    obj = UserStory.objects.get(id=id)
    obj.delete()
    obj = UserStory_of_Sprint.objects.filter(pk_userStory=id)
    obj.delete()
    return userStoryPage(request,project.name) 

def delete_user(request,id):
    userDelete = User_of_project.objects.get(id=id)
    userDelete.delete()
    return userStoryPage(request,project.name)
    

def updateToDone(request,id):
    obj = UserStory.objects.get(id=id)
    obj.status = "Done"
    obj.save()
    return userStoryPage(request,project.name)



def allStories(request):
    return userStoryPage(request,project.name)


def FilterNotDone(request):
    objects = UserStory.objects.filter(nameProject=project.name)
    container = []
    for o in objects:
        if o.status == "Not Done":
            container+=[o]
    userOfProject=User_of_project.objects.filter(pk_project=project.name) 
    sprint =Sprint.objects.filter(nameProject=project.name).last()

    return render(request,'storiesView/storiesView.html',{'sprint':sprint ,'user':getNowUser(),'stories':(container),'project':(project),'userOfProject':(userOfProject)}) 

def filterMyUserStory(request):
    user=getNowUser()
    my_stories = UserStory.objects.filter(nameProject=project.name).filter(assign=user.userName)
    userOfProject=User_of_project.objects.filter(pk_project=project.name) 
    sprint =Sprint.objects.filter(nameProject=project.name).last()

    return render(request,'storiesView/storiesView.html',{'sprint':sprint,'user':getNowUser(),'stories':(my_stories),'project':(project),'userOfProject':(userOfProject)})

def updateUserStory(request,id):
    user_story =  UserStory.objects.get(id=id)
    ufp = User_of_project.objects.filter(pk_project=project.name)
    my_users=[]
    for x in ufp:
        my_users+=[User.objects.get(userName=x.pk_user)]
    return render(request,'createStory/createStory.html',{'user_story':(user_story),'users':(my_users),'range':(range(1,6))}) 

def updateAction(request,id):
    user_story =  UserStory.objects.get(id=id)
    user_story.assign = request.POST.get('Assign', None)
    user_story.priority= request.POST.get('Priority', None) 
    user_story.content = request.POST.get('Content', None) 
    user_story.save()    
    return userStoryPage(request,project.name)

def getProject():
    return project  

def setNowProject(pro):
    global project
    project=pro

def testF(request):
    xx=UserStory.objects.all()
    for x in xx:
        x.delete()

    xx=Project.objects.all()
    for x in xx:
        x.delete()
    
    xx=User_of_project.objects.all()
    for x in xx:
        x.delete()
        
    xx=Sprint.objects.all()
    xx.delete()

    xx=UserStory_of_Sprint.objects.all()
    xx.delete()
    
    xx=msg.objects.all()
    xx.delete()
    
    
    return render(request,'storiesView/test.html',{})
    
    
    