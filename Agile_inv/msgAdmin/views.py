from django.shortcuts import render
from login.views import getNowUser
from msgAdmin.models import msg



def messagesPage(request):
    my_msg = msg.objects.filter(teamLeader = getNowUser().userName ) 
    return render(request,'adminMessages/adminMessages.html',{'user':getNowUser(),'admin_messages':my_msg}) 

def messageSave(request): 
    content = request.POST.get('content', None)
    my_msg=msg(teamLeader=getNowUser().userName,content=content)
    my_msg.save()
    return messagesPage(request)