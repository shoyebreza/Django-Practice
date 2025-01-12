from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# work with database
# transform data
# data pass
# Http response

def manager_dashboard(request):
    return render(request, "dashboard.html")

def user_dashboard(request):
    return render(request, "user-dashboard.html")

