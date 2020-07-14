from django.urls import path
from projects_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('createproject/',views.add_project,name='addproject')
]
