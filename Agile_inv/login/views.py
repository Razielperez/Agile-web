from django.shortcuts import render
from login.models import User
from userStory.models import UserStory
from django.contrib import messages
from project.models import Project,User_of_project
from sprint.models import Sprint,UserStory_of_Sprint
from msgAdmin.models import msg
def homePage(request):
    return render(request,'loginPage/login.html',{}) 

def calculateInformation(user):
    myStats = {}
    userStoryDone = (UserStory.objects.filter(assign=user.userName).filter(status='Done')).count()
    userStoryAll = (UserStory.objects.filter(assign=user.userName).count())
    myStats["allUserStories"] = userStoryAll   
    if userStoryAll == 0:
        myStats['userStoryComplete'] = 0
    else:
        myStats['userStoryComplete'] = int((userStoryDone / userStoryAll) * 100)
        
    projectDone = 0
    projectAll = (User_of_project.objects.filter(pk_user=user.userName))
    myStats["allProjects"] = projectAll.count()
    for p in projectAll:
        project = Project.objects.get(name = p.pk_project)
        if UserStory.objects.filter(nameProject = project.name).filter(status="Not Done").count() == 0:
            projectDone += 1
                
    if projectAll.count() == 0:
        myStats['projectCompleted'] = 0
    else:
        myStats['projectCompleted'] = int((projectDone / projectAll.count()) * 100)

     
    allsprints=[]
    for p in projectAll:
        project = Project.objects.get(name = p.pk_project)
        allsprints += Sprint.objects.filter(nameProject=project.name)
    myStats["sprints"] = len(allsprints)
    
    
    sprintDone=0
    for s in allsprints:
        userStorySprint= UserStory_of_Sprint.objects.filter(pk_sprint=s.id)
        if not ([u for u in userStorySprint if UserStory.objects.get(id=u.pk_userStory).status=="Not Done"]) :
            sprintDone+=1
   
    
    if len(allsprints) == 0:
        myStats['sprintCompleted'] = 0
    else:
        myStats['sprintCompleted'] = int((sprintDone / len(allsprints)) * 100)
        
    
    myStats['messagesCount'] = msg.objects.filter(teamLeader=now_user.userName).count()
    
    return myStats
    
def submit_login(request):
    # כפתור התחברות אחרי שהכנסנו נתונים
    userName=request.POST.get('username', None)
    password=request.POST.get('password', None)
    user=User.objects.filter(userName=userName).filter(password=password)
    if not user:
        return render(request,'loginPage/login.html',{})
    global now_user
    now_user=user[0]
    
    return render(request,f'users/teamLeader.html',{'user':(user[0]),'state':(calculateInformation(now_user))}) 

def returnOverview(request):
    return render(request,f'users/teamLeader.html',{'user':(now_user),'state':(calculateInformation(now_user))}) 

def submit_registration(request):
    #כפתור הרשמה אחרי שמלאנו פרטים 
    user=User()
    user.firstName=request.POST['firstName']
    user.lastName=request.POST['lastName']
    user.userName=request.POST['userName']
    user.password=request.POST['password']
    user.role=request.POST['role']
    userTest=User.objects.filter(userName=user.userName)
    if user.role=="choose":
        messages.success(request, 'You need to choose role!')
        return render(request,'registerPage/register.html',{})
    if userTest :
        #הודעה שהשם משתמש כבר תפוס
        messages.success(request, 'User Already In Registered')
        return render(request,'registerPage/register.html',{})
    user.save()
    return render(request,'loginPage/login.html',{}) 
def setNowUser(user):
    global now_user
    now_user=user
def getNowUser():
    return now_user
def isName(str):
    return str.isalpha()
def isRole(str):
    return not (str=="Choose role")
def isUserName(str):
    return str[:1].isalpha()

# Create your views here.
