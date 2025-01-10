
from django.urls import path
from tasks.views import show_task,specific_task

urlpatterns = [
    path("show-task/", show_task),
    path("sp_task/<int:id>/", specific_task)
]