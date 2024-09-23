from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.task, name='tasks'),
    path('tasks_completed/', views.task_completed, name='task_completed'),
    path('tasks/create/', views.create_task, name='tasks/create'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete_tasks'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task')

]
