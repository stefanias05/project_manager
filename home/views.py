from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from project_manager.context_processors import get_user_project, get_user_tasks, allusers


# Create your views here.

def index(request):
    html_template = loader.get_template('home/index.html')
    context = {
    }
    return HttpResponse(html_template.render(context, request))

@login_required
def dashboard(request):
    user = request.user
    projects = get_user_project(request)
    tasks = get_user_tasks(request)
    users = allusers(request)
    return render(request, 'dashboard/dashboard.html',
                  {'ownerprojects': projects["allprojects"],
                   'member_projects':projects['project_member'],
                   'alltasks': tasks['alltasks'],
                   'ownerprojectteam': projects['team'],
                   'number_project': projects['number_projects'],
                   'number_task': tasks['number_task'],
                   'members': users['allmembers'],'user': user
                   })


