from django.test import TestCase
from django.test import Client
from project.models import *
from django.urls import reverse
from login.models import User
import datetime
from project.views import setNowUserProject
from login.views import setNowUser
from sprint.models import Sprint,UserStory_of_Sprint
import datetime
class SprintTestCreate(TestCase): 
    def setUp(self):
        self.sprint = Sprint.objects.get_or_create(
            nameSprint = 'test_sprint_name',
            nameProject = 'test_project_name',
            dateEnd=datetime.datetime.now()
        )
        self.u_o_s = UserStory_of_Sprint.objects.get_or_create(
            pk_sprint = '1',
            pk_userStory = '1'
        )
        
        
    def test_check_sprint_is_created(self):
        sprint = Sprint.objects.get(nameSprint='test_sprint_name')
        self.assertEqual(self.sprint[0].nameSprint,sprint.nameSprint)    
    
        
    def test_check_uos_is_created(self):
        uos = UserStory_of_Sprint.objects.get(pk_sprint=1)
        self.assertEqual(self.u_o_s[0].pk_sprint,uos.pk_sprint)

        
class ProjectTestUrl(TestCase):
    def setUp(self):
        self.sprint = Sprint.objects.get_or_create(
            nameSprint = 'test_sprint_name',
            nameProject = 'test_project_name',
            dateEnd=datetime.datetime.now()
        )
        self.u_o_s = UserStory_of_Sprint.objects.get_or_create(
            pk_sprint = 1,
            pk_userStory = 1
        )
          

    def test_mySprintPageUrl_loads_properly(self):
        response =reverse('sprint:showSprint')
        self.assertEqual(response, '/sprint/showSprint')
    def test_myProjectPageUrl_dosent_loads_properly(self):
        response =reverse('sprint:showSprint')
        self.assertNotEqual(response, '/sprint/showSprint/nonepage')

############################################################################################
    def test_addSprintPageUrl_loads_properly(self):
        response =reverse('sprint:addSprint')
        self.assertEqual(response, '/sprint/addSprint')
    def test_addSprintPageUrl_dosent_loads_properly(self):
        response =reverse('sprint:addSprint')
        self.assertNotEqual(response, '/sprint/addSprint/nonepage')

############################################################################################
    def test_SaveSprintPageUrl_loads_properly(self):
        response =reverse('sprint:saveSprint')
        self.assertEqual(response, '/sprint/saveSprint')
    def test_SaveSprintPagePageUrl_dosent_loads_properly(self):
        response =reverse('sprint:saveSprint')
        self.assertNotEqual(response, '/sprint/saveSprint/not_name_of_project/')
