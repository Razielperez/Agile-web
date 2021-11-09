from django.test import TestCase
from django.test import Client
from project.models import *
from django.urls import reverse
from login.models import User
import datetime
from project.views import setNowUserProject
from login.views import setNowUser

class ProjectTestCreate(TestCase): 
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
        
        
    def test_check_teammate_project_is_created(self):
        teammate_project = User_of_project.objects.get(pk_user='test_teammate_userName')
        self.assertEqual(teammate_project.pk_user,'test_teammate_userName')    
    
        
    def test_check_teamLeader_is_created(self):
        teamLeader = User.objects.get(userName='test_teamLeader_userName')
        self.assertEqual(teamLeader.userName,'test_teamLeader_userName')

    def test_check_teammate_is_created(self):
        teammate = User.objects.get(userName='test_teammate_userName')
        self.assertEqual(teammate.userName,"test_teammate_userName")
        
    def test_check_project_is_created(self):
        project = Project.objects.get(name='test_project_name')
        self.assertEqual(project.name,"test_project_name")
        
        
    def test_check_teamLeader_project_is_created(self):
        teamLeader_project = User_of_project.objects.get(pk_user='test_teamLeader_userName')
        self.assertEqual(teamLeader_project.pk_user,'test_teamLeader_userName')
        
class ProjectTestUrl(TestCase):
    def setUp(self):
        self.project = Project.objects.get_or_create(
                name='test_project_name',
                teamLeader='test_project_teamLeader',
                date = datetime.datetime.now(),
                )
        self.project[0].save()  

    def test_myProjectPageUrl_loads_properly(self):
        response =reverse('project:createPro')
        self.assertEqual(response, '/createProject/projectsPage')
    def test_myProjectPageUrl_dosent_loads_properly(self):
        response =reverse('project:createPro')
        self.assertNotEqual(response, '/createProject/projectsPage/nonepage')

############################################################################################
    def test_addProjectPageUrl_loads_properly(self):
        response =reverse('project:buttonAddProject')
        self.assertEqual(response, '/createProject/addProject')
    def test_addProjectPageUrl_dosent_loads_properly(self):
        response =reverse('project:buttonAddProject')
        self.assertNotEqual(response, '/createProject/addProject/nonepage')

############################################################################################
    def test_deleteProjectPageUrl_loads_properly(self):
        response =reverse('project:deleteProject',kwargs={'nameProject': 'testProjectName'})
        self.assertEqual(response, '/createProject/deleteProject/testProjectName')
    def test_deleteProjectPageUrl_dosent_loads_properly(self):
        response =reverse('project:deleteProject', kwargs={'nameProject': 'testProjectName'})
        self.assertNotEqual(response, '/createProject/deleteProject/not_name_of_project/')

############################################################################################
    def test_saveProjectPageUrl_loads_properly(self):
        response =reverse('project:saveNewProject')
        self.assertEqual(response, '/createProject/saveNewProject')
    def test_saveProjectPageUrl_dosent_loads_properly(self):
        response =reverse('project:saveNewProject')
        self.assertNotEqual(response, '/createProject/saveNewProject_nonepage')

############################################################################################
    

class ProjectTestViews(TestCase):
    def setUp(self):
        self.teamLeader = User.objects.get_or_create(
            firstName='test_teamLeader_firstName',
            lastName='test_teamLeader_lastName',
            userName='test_teamLeader_userName',
            password='test_teamLeader_password',
            role='teamLeader'
            )
        #self.teamLeader.save()

        self.teammate = User.objects.get_or_create(
            firstName='test_teammate_firstName',
            lastName='test_teammate_lastName',
            userName='test_teammate_userName',
            password='test_teammate_password',
            role='teammate'
            )
        self.project = Project.objects.get_or_create(
            name='testProjectName',
            teamLeader='test_project_teamLeader',
            date = datetime.datetime.now(),
            )
        self.project[0].save()
        self.teamLeader_project = User_of_project.objects.get_or_create(
            pk_user = 'test_teamLeader_userName',
            pk_project = 'testProjectName'
        )
        self.teammate_project = User_of_project.objects.get_or_create(
            pk_user = 'test_teammate_userName',
            pk_project = 'testProjectName'
        )
        self.client=Client()
        setNowUser(self.teamLeader[0])# שינוי בכוח
        
    def test_index_loads_properly(self):
        c = Client()
        response = c.post('', {'username': 'raziel111', 'password': '111'})
        response.status_code
        self.assertEqual(response.status_code, 200)

    def test_login_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_404_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/nonepage')
        self.assertEqual(response.status_code, 404)
    
#--------------------------------------------------------------------------------------------------------#    
        
    def test_myProjectPage_loads_properly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])# שינוי בכוח
        response = c.get('/createProject/projectsPage')
        response.status_code
        self.assertEqual(response.status_code, 200)
    def test_myProjectPage_loads_Notproperly(self):
        c = Client()
        setNowUserProject(self.teammate[0])
        response = c.get('/createProject/projectsPage2')
        response.status_code
        self.assertEqual(response.status_code, 404)
#--------------------------------------------------------------------------------------------------------#    
    def test_addProject_loads_properly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])# שינוי בכוח
        response = c.get('/createProject/addProject')
        response.status_code
        self.assertEqual(response.status_code, 200)
    def test_addProject_loads_not_properly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])
        response = c.get('/createProject/2addProject')
        response.status_code
        self.assertEqual(response.status_code, 404)
#--------------------------------------------------------------------------------------------------------#    
    def test_deleteProject_loads_properly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])# שינוי בכוח
        response = c.post(f'http://127.0.0.1:8000/createProject/deleteProject/{(self.project[0]).name}')
        response.status_code
        self.assertEqual(response.status_code, 200)
    def test_myProjectPage_loads_not_properly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])# שינוי בכוח
        response = c.post('http://127.0.0.1:8000/createProject/deleteProject_none',{'nameProject':'testProjectName'})
        response.status_code
        self.assertEqual(response.status_code, 404)
#--------------------------------------------------------------------------------------------------------#    
    def test_saveProjectPage_loads_properly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])# שינוי בכוח
        response = c.post('http://127.0.0.1:8000/createProject/saveNewProject',{'nameProject':'testProjectName','users':['test_teammate_userName','test_teamLeader_userName']})
        response.status_code
        self.assertEqual(response.status_code, 200)
    def test_saveProjectPage_loads_not_roperly(self):
        c = Client()
        setNowUserProject(self.teamLeader[0])# שינוי בכוח
        response = c.post('http://127.0.0.1:8000/createProject/saveNewProject_none',{'nameProject':'testProjectName','users':['test_teammate_userName','test_teamLeader_userName']})
        response.status_code
        self.assertEqual(response.status_code, 404)
#--------------------------------------------------------------------------------------------------------#    

        

        