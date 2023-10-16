
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetDoneView

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView


from members.forms import MemberRegisterForm, UserProfileForm
from members.models import MemberUser
from projects.models import Project


# Create your views here.
class MemberAccountForm(SuccessMessageMixin, CreateView):
    form_class = MemberRegisterForm
    model = MemberUser
    template_name = 'members/register_form.html'
    success_url = reverse_lazy('create-project')

    def get_success_message(self, cleaned_data):
        msg = f'Welcome to Project Manager,{self.object.first_name} {self.object.last_name}.'
        return msg


class MembersListView(LoginRequiredMixin, ListView):
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
    return render(request, 'members/member_project_list_completed.html',
                  {'completed_projects': completed_projects, 'member': member})


# @login_required
# def update_profile_user(request):
#     user = request.user
#     user_profile = MemberUser.objects.get(user_ptr_id=user.id)
#     form = MemberUpdateForm(request.POST, request.FILES, instance=user)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Your profile is updated successfuly')
#             return redirect(to="dashboard")
#         else:
#             form = MemberUpdateForm(instance=user)
#
#     return render(request,'members/update_profile.html', {'form': form,
#                                                           'user': user_profile
#                                                           })


class UpdateUserView(UpdateView, LoginRequiredMixin):
    model = MemberUser
    form_class = UserProfileForm
    template_name = 'members/update_profile.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = self.request.user
        if form.is_valid():
            self.object = form.save()
        return super().form_valid(form)

    def get_object(self):
        """imi afisez datele curente ale userului in interfata"""
        return self.request.user

# class UserPasswordResetDone(PasswordResetDoneView):
#     template_name = 'registration/password_reset_sent.html'