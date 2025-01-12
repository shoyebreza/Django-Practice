
from django.urls import path
from tasks.views import manager_dashboard,user_dashboard

urlpatterns = [
    path("dashboard/", manager_dashboard),
    path("user_dashboard/", user_dashboard)
]