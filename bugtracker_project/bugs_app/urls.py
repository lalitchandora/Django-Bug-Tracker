from django.urls import path
from bugs_app import views

urlpatterns = [
    path('<int:id>/',views.list_bugs,name='bug_list'),
    path('addbug/<int:project_id>/',views.bug_add,name='bugform')
]