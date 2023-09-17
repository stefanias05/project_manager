from django.shortcuts import render

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from members.forms import MemberRegisterForm
from members.models import MemberUser
from projects.models import Project


# Create your views here.
class MemberAccountForm(SuccessMessageMixin,CreateView):
    form_class = MemberRegisterForm
    model = MemberUser
    template_name = 'members/register_form.html'
    success_url = reverse_lazy('create-project')

    def get_success_message(self, cleaned_data):
        msg = f'Welcome to Project Manager,{self.object.first_name} {self.object.last_name}.'
        return msg


class MembersListView(ListView):
    model = MemberUser
    template_name = 'members/list_of_members.html'
    context_object_name = 'allmembers'

def completed_member_project(request, member_id):
    """
    Afisarea proiectelor finalizate ale unui utilizator anume
    :param request:
    :param member_id:
    :return:
    """
    member = MemberUser.objects.get(pk=member_id)
    completed_projects = Project.objects.filter(owner_id=member, status='Completed')
    return render(request,'members/member_project_list_completed.html', {'completed_projects':completed_projects, 'member': member})




