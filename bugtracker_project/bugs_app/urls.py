from django.urls import path
from bugs_app import views

urlpatterns = [
    path('<int:id>/',views.list_bugs),
]