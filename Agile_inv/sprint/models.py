from django.db import models
from userStory.models import UserStory

class Sprint(models.Model):
    nameSprint = models.CharField(max_length=200 )
    nameProject=models.CharField(max_length=200 )
    dateStart=models.DateField(auto_now_add=True)
    dateEnd=models.DateField()
    def __str__(self):
        return self.nameSprint
    def getUserStory(self):
        ufs=UserStory_of_Sprint.objects.filter(pk_sprint=self.id)
        return [UserStory.objects.get(id=u.pk_userStory) for u in ufs]
        
# Create your models here.
class UserStory_of_Sprint(models.Model):
    pk_sprint = models.CharField(max_length=200 )
    pk_userStory = models.CharField(max_length=200 )
