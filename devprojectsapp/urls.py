from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='all-project'),
    path('project/<str:pk>', views.project, name="project"),
    path('add-project/', views.addProject, name='add-project'),
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),    
]