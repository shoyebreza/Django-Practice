from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# work with database
# transform data
# data pass
# Http response
def home(request):
    return HttpResponse("wellcome to task management system")

def contact(request):
    return HttpResponse("Contact with Us")


def show_task(request):
    return HttpResponse("This is the tasks page")


def specific_task(request, id):
    print("id", id)
    print("id type", type(id))
    return HttpResponse(f" this is the specific task{id}")