from members.models import MemberUser
from projects.models import Project
from tasks.models import Task


def get_user_project(request):
    user=request.user.id
    allprojects = Project.objects.filter(owner=user) #toate proiectele create de user
    project_member =Project.objects.filter(team_members=user) # toate proiectele la care e alocat userul
    user_projects = allprojects.count() + project_member.count()
    team = []
    for project in allprojects:
        team = project.team_members.all()

    return {'allprojects': allprojects,'project_member':project_member, 'team':team, 'number_projects': user_projects}

def get_user_tasks(request):
    user = request.user.id
    number_user_task = Task.objects.filter(user=user).count()
    return {'alltasks': Task.objects.filter(user=user), 'number_task': number_user_task}

def allusers(request):
    allusers = MemberUser.objects.all().count()
    return {'allmembers': allusers}



