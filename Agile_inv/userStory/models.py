from django.db import models



class UserStory(models.Model):
    nameProject = models.CharField(max_length = 300)
    content = models.CharField(max_length = 300)
    priority = models.CharField(max_length = 2)
    assign = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100,default="Not Done")
    def __str__(self):
        return f'content: {self.content} , priority: {self.priority} , assign: {self.assign} , status: {self.status}'
    
