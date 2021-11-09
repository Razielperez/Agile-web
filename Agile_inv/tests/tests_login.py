from django.test import TestCase
from django.test import Client
from login import views
from login.models import User

class loginTestCreate(TestCase):
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
    def test_check_teammate_project_is_created(self):
        teammate = User.objects.get(userName='test_teammate_userName')
        self.assertEqual(teammate.userName,'test_teammate_userName')    
    
    def test_isName(self):
        res =views.isName("toer")
        self.assertTrue(res)
    def test_isRole(self):
        res =views.isRole("teammate")
        self.assertTrue(res)
    def test_isUserName(self):
        res =views.isUserName("UserName")
        self.assertTrue(res)
    def test_index_loads_properly(self):
        c = Client()
        response = c.post('', {'username': '', 'password': ''})
        response.status_code
        self.assertEqual(response.status_code, 200) 
    def test_index_loads(self):
        c = Client()
        response = c.post('registration', {'firstName': 'tomeriko', 'lastName': 'ttt','userName':'tomer123','password':'123','role':'teamLeader'})
        response.status_code
        self.assertNotEqual(response.status_code, 200)       
    

