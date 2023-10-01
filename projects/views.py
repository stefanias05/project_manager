from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from members.models import MemberUser
from projects.forms import ProjectForm, ProjectUpdateForm, ProjectAllocationMembersForm
from projects.models import Project


# Create your views here.


class ListProjectView(LoginRequiredMixin, ListView):
    """
    afisez toate proiectele din BD
    """
    template_name = "projects/list_of_projects.html"
    model = Project
    context_object_name = "allprojects"

    def get_queryset(self):
        allprojects = Project.objects.exclude(status="Completed").all()
        return allprojects


class CreateProjectView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Project
    template_name = 'projects/create_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('create-project')
    success_message = 'The Project {name} has been successfully added!'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(name=self.object.name)

    def form_valid(self, form):
        """
        owner= userul auth si cel care creeaza proiectul
        :param form:
        :return:
        """
        # if isinstance(self.request.user, MemberUser):
        #     Project.owner = self.request.user
        #     Project.save()

        form.instance.owner = self.request.user

        return super(CreateProjectView, self).form_valid(form)



@login_required
def detail_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project_members = project.team_members.all()
    return render(request, 'projects/detail_project.html', {'project': project, 'project_members': project_members})


class UpdateProjectView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Project
    success_url = reverse_lazy('list-of-projects')
    template_name = 'projects/update_project.html'
    form_class = ProjectUpdateForm
    success_message = f'The project {Project.objects.name} was successfuly updated'


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "projects/delete_project.html"
    success_url = reverse_lazy('list-of-projects')


@login_required
def allocate_member_project(request, project_id):
    """
    Alocare membrii disponibili pe proiect.
    :param request:
    :param project_id:
    :return:
    """
    project = Project.objects.get(pk=project_id)
    form = ProjectAllocationMembersForm()
    if request.method == 'POST':
        form = ProjectAllocationMembersForm(request.POST)
        if form.is_valid():
            all_members = list(
                form.cleaned_data['team_members'].values_list('id', flat=True))  # iau toti membrii din aplicatie
            for member_id in all_members:
                # if member.id not in allocate_member_id:
                project.team_members.add(MemberUser.objects.get(id=member_id))
                project.save()
            return redirect('detail-project', project.id)
    else:
        team_members = MemberUser.objects.exclude(
            user_ptr_id__in=project.team_members.values_list("id", flat=False))

        return render(request, 'projects/add_member.html', {'team_members': team_members, "project": project.name})


@login_required()
def user_project(request):
    """
    afisez proiectele utilizatorului logat
    :param request:
    :return:
    """
    user = request.user  # stochez userul autentificat in var
    allprojects = Project.objects.filter(owner=user)
    project_member = Project.objects.filter(team_members=user)
    return render(request, 'projects/user_projects.html',
                  {'allprojects': allprojects, 'projectsmember': project_member})
