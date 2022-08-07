from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),    
    path('AdvisoryCommittee', views.index), 
    path('DifferentiallyAbledPersons', views.index), 
    path('RemedialCoaching', views.index), 
    path('CoachingForNET', views.index), 
    path('CoachingForEntryIntoService', views.index), 
    path('SOCE', views.index), 
    path('SocePrograms', views.index), 
    path('Gallery', views.index), 
    path('Contact', views.index), 
    path('Feedback', views.index), 
    path('Innovations', views.index)
    

   

]
