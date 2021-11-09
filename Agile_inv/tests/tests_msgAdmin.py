from django.test import TestCase
from django.test import Client
from django.urls import reverse
from msgAdmin.models import msg
from login.models import User
import datetime


class msgAdminTestCreate(TestCase): 
    def setUp(self):
        self.teamLeader = User.objects.get_or_create(
            firstName='test_teamLeader_firstName',
            lastName='test_teamLeader_lastName',
            userName='test_teamLeader_userName',
            password='test_teamLeader_password',
            role='teamLeader'
            )
        self.teamLeader[0].save()
        
        self.msgToAdmin = msg.objects.get_or_create(
            id = '0',
            teamLeader='test_teamLeader_userName',
            content='test_msgToAdmin_content',
            date = datetime.datetime.now(),
            )
        
        self.msgToAdmin[0].save()
        
#------------------------------------------------------------------------------#
    def test_check_msg_created(self):
        testing_msg = msg.objects.get(id='0')
        self.assertEqual(testing_msg.content,'test_msgToAdmin_content')    
#------------------------------------------------------------------------------#


class msgAdminTestUrl(TestCase):
    def setUp(self):
        self.msgToAdmin = msg.objects.get_or_create(
            id = '0',
            teamLeader='test_teamLeader_userName',
            content='test_msgToAdmin_content',
            date = datetime.datetime.now(),
            )
        
        self.msgToAdmin[0].save()
#------------------------------------------------------------------------------#
    def test_messagesPageUrl_loads_properly(self):
        response =reverse('msg:messagesPage')
        self.assertEqual(response, '/msgAdmin/messagesPage')
        
        
    def test_messagesPageUrl_doesnt_loads_properly(self):
        response =reverse('msg:messagesPage')
        self.assertNotEqual(response, '/msgAdmin/notMessagesPage')
#------------------------------------------------------------------------------#
    def test_messageSaveUrl_loads_properly(self):
        response =reverse('msg:messageSave')
        self.assertEqual(response, '/msgAdmin/messageSave')
        
        
    def test_messageSaveUrl_doesnt_loads_properly(self):
        response =reverse('msg:messagesPage')
        self.assertNotEqual(response, '/msgAdmin/notMessageSave')
