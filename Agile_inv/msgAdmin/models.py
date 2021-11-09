from django.db import models


class msg(models.Model):
    teamLeader = models.CharField(max_length = 300)
    content = models.CharField(max_length = 300)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'content: {self.content} , teamLeader: {self.teamLeader} '
    
