from django.urls import path
from .views import TaskView, UpdateTaskView, DeleteTaskView, CreateTaskView, UserRegistrationView

urlpatterns = [
    path('accounts/registration', UserRegistrationView.as_view(), name='register'),

    path('', TaskView.as_view()),
    path('todo/create_todo', CreateTaskView.as_view(), name='create'),
    path('todo/update_todo/<int:pk>', UpdateTaskView.as_view(), name='update'),
    path('todo/delete_todo/<int:pk>', DeleteTaskView.as_view(), name='delete'),




]
