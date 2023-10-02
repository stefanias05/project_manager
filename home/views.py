from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from project_manager.context_processors import get_user_project, get_user_tasks


# Create your views here.

def index(request):
    html_template = loader.get_template('home/index.html')
    context = {
    }
    return HttpResponse(html_template.render(context, request))


def dashboard(request):
    projects = get_user_project(request)
    tasks = get_user_tasks(request)
    return render(request, 'dashboard/dashboard.html', {'ownerprojects': projects["allprojects"], 'alltasks': tasks['alltasks']})
