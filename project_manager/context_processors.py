from projects.models import Project
from tasks.models import Task


def get_user_project(request):
    user= request.user
    allprojects = Project.objects.filter(owner=user)
    project_member =Project.objects.filter(team_members=user)
    return {'allprojects': allprojects,'project_member':project_member}

def get_user_tasks(request):
    user = request.user
    return {'alltasks': Task.objects.filter(user=user)}


