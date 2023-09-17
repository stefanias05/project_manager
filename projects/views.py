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


class ListProjectView(ListView):
    template_name = "projects/list_of_projects.html"
    model = Project
    context_object_name = "allprojects"


class CreateProjectView(SuccessMessageMixin, CreateView):
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


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail_project.html'


class UpdateProjectView(SuccessMessageMixin, UpdateView):
    model = Project
    success_url = reverse_lazy('list-of-projects')
    template_name = 'projects/update_project.html'
    form_class = ProjectUpdateForm
    success_message = f'The project {Project.objects.name} was successfuly updated'


class DeleteProjectView(DeleteView):
    model = Project
    template_name = "projects/delete_project.html"
    success_url = reverse_lazy('list-of-projects')


def allocate_member_project(request, project_id):
    """
    Alocare membrii pe proiect.
    :param request:
    :param project_id:
    :return:
    """
    project = Project.objects.get(pk=project_id)
    form = ProjectAllocationMembersForm()
    if request.method == 'POST':
        form = ProjectAllocationMembersForm(request.POST)
        if form.is_valid():
            selected_member = form.cleaned_data['team_members']
            project.team_members.set(selected_member)
            # form.save()
            return redirect('detail-project', project.id)
        else:
            form = ProjectAllocationMembersForm()

    return render(request, 'projects/add_member.html', {'form':form,
                                                        'project': project})


