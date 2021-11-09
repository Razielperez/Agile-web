from django.test import TestCase
from django.test import Client
from userStory.models import *
from django.urls import reverse
from login.models import User
from project.models import Project,User_of_project
import datetime
from project.views import setNowUserProject
from login.views import setNowUser

class userStoryTestCreate(TestCase): 
    def setUp(self):
        self.teamLeader = User.objects.get_or_create(
            firstName='test_teamLeader_firstName',
            lastName='test_teamLeader_lastName',
            userName='test_teamLeader_userName',
            password='test_teamLeader_password',
            role='teamLeader'
            )

        self.teammate = User.objects.get_or_create(
            firstName='test_teammate_firstName',
            lastName='test_teammate_lastName',
            userName='test_teammate_userName',
            password='test_teammate_password',
            role='teammate'
            )
        self.project = Project.objects.get_or_create(
            name='test_project_name',
            teamLeader='test_project_teamLeader',
            date = datetime.datetime.now(),
            )
        self.teamLeader_project = User_of_project.objects.get_or_create(
            pk_user = 'test_teamLeader_userName',
            pk_project = 'test_project_name'
        )
        self.teammate_project = User_of_project.objects.get_or_create(
            pk_user = 'test_teammate_userName',
            pk_project = 'test_project_name'
        )
        self.userStoryTest = UserStory.objects.get_or_create(
            id = '0',
            nameProject = 'testProjectName',
            content = 'test_userStoryTest_content',
            priority = 'test_userStoryTest_priority',
            assign = 'test_teammate_userName',
            status = 'Not Done'
        )
        self.userStoryTest[0].save()
        
#------------------------------------------------------------------------------#
    def test_check_userStory_created(self):
        userStoryTest = UserStory.objects.get(nameProject='testProjectName')
        self.assertEqual(userStoryTest.assign,'test_teammate_userName')    
#------------------------------------------------------------------------------#


class userStoryTestUrl(TestCase):
    def setUp(self):
        self.userStoryTest = UserStory.objects.get_or_create(
            nameProject = 'testProjectName',
            content = 'test_userStoryTest_content',
            priority = 'test_userStoryTest_priority',
            assign = 'test_teammate_userName',
            status = 'Not Done'
        )
        self.userStoryTest[0].save()
#------------------------------------------------------------------------------#
    def test_insertStoryUrl_loads_properly(self):
        response =reverse('userStory:insertStory')
        self.assertEqual(response, '/userStory/insertStory')
        
        
    def test_insertStoryUrl_doesnt_loads_properly(self):
        response =reverse('userStory:insertStory')
        self.assertNotEqual(response, '/userStory/notInsert')
#------------------------------------------------------------------------------#
    def test_submit_storyUrl_loads_properly(self):
        response =reverse('userStory:submit_story')
        self.assertEqual(response, '/userStory/submit_story')
        
        
    def test_submit_storyUrl_doesnt_loads_properly(self):
        response =reverse('userStory:insertStory')
        self.assertNotEqual(response, '/userStory/not_submit_story')
#------------------------------------------------------------------------------#
    def test_filterMyStoryUrl_loads_properly(self):
        response =reverse('userStory:filterMyStory')
        self.assertEqual(response, '/userStory/filterMyStory')
        
        
    def test_filterMyStoryUrl_doesnt_loads_properly(self):
        response =reverse('userStory:filterMyStory')
        self.assertNotEqual(response, '/userStory/not_filterMyStory')
#------------------------------------------------------------------------------#
    def test_FilterNotDoneUrl_loads_properly(self):
        response =reverse('userStory:FilterNotDone')
        self.assertEqual(response, '/userStory/FilterNotDone')
        
        
    def test_FilterNotDoneUrl_doesnt_loads_properly(self):
        response =reverse('userStory:FilterNotDone')
        self.assertNotEqual(response, '/userStory/not_FilterNotDone')
#------------------------------------------------------------------------------#
    def test_allStoriesUrl_loads_properly(self):
        response =reverse('userStory:allStories')
        self.assertEqual(response, '/userStory/allStories')
        
        
    def test_allStoriesUrl_doesnt_loads_properly(self):
        response =reverse('userStory:allStories')
        self.assertNotEqual(response, '/userStory/not_allStories')
#------------------------------------------------------------------------------#
    def test_returnHomeProjectUrl_loads_properly(self):
            response =reverse('userStory:returnHomeProject')
            self.assertEqual(response, '/userStory/returnHomeProject')
            
            
    def test_returnHomeProjectUrl_doesnt_loads_properly(self):
            response =reverse('userStory:returnHomeProject')
            self.assertNotEqual(response, '/userStory/not_returnHomeProject')
#------------------------------------------------------------------------------#
    def test_delete_storyUrl_loads_properly(self):
        response =reverse('userStory:delete_story',kwargs={'id': '0'})
        self.assertEqual(response, '/userStory/delete_story/0/')
        
    def test_delete_storyUrl_doesnt_loads_properly(self):
        response =reverse('userStory:delete_story',kwargs={'id': '0'})
        self.assertNotEqual(response, '/userStory/delete_story/1/')
#------------------------------------------------------------------------------#
    def test_userStoryPageUrl_loads_properly(self):
        response =reverse('userStory:userStoryPage',kwargs={'nameProject':'testProjectName'})
        self.assertEqual(response, '/userStory/userStoryPage/testProjectName/')

    def test_userStoryPageUrl_doesnt_loads_properly(self):
        response =reverse('userStory:userStoryPage',kwargs={'nameProject':'testProjectName'})
        self.assertNotEqual(response, '/userStory/userStoryPage/Not_testProjectName/')
#------------------------------------------------------------------------------#
    def test_updateToDoneUrl_loads_properly(self):
        response =reverse('userStory:updateToDone',kwargs={'id':'0'})
        self.assertEqual(response, '/userStory/updateToDone/0/')

    def test_updateToDoneUrl_doesnt_loads_properly(self):
        response =reverse('userStory:updateToDone',kwargs={'id':'0'})
        self.assertNotEqual(response, '/userStory/updateToDone/1/')
        
#------------------------------------------------------------------------------#
    def test_updateUserStoryUrl_loads_properly(self):
        response =reverse('userStory:updateUserStory',kwargs={'id':'0'})
        self.assertEqual(response, '/userStory/updateUserStory/0/')

    def test_updateUserStoryUrl_doesnt_loads_properly(self):
        response =reverse('userStory:updateUserStory',kwargs={'id':'0'})
        self.assertNotEqual(response, '/userStory/updateUserStory/1/')
#------------------------------------------------------------------------------#
    def test_updateActionUrl_loads_properly(self):
        response =reverse('userStory:updateAction',kwargs={'id':'0'})
        self.assertEqual(response, '/userStory/updateAction/0/')

    def test_updateActionUrl_doesnt_loads_properly(self):
        response =reverse('userStory:updateAction',kwargs={'id':'0'})
        self.assertNotEqual(response, '/userStory/updateAction/1/')