from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView

from members.models import MemberUser
from tasks.forms import TaskForm, TaskUpdateForm
from tasks.models import Task


# Create your views here.
# class CreateTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     form_class = TaskForm
#     template_name = 'tasks/create_tasks.html'
#     model = Task
#     success_url = reverse_lazy('add-task')
#
#
#     def get_initial(self):
#         super(CreateTask, self).get_initial()
#         user = self.request.user
#         projects = Project.objects.filter(owner_id=user.id)
#         self.initial = {"user": user, "project": projects}
#         return self.initial
#
#     def form_valid(self, form):
#         form.instance.user = MemberUser.objects.get(id=self.request.user.id)
#         return super(CreateTask, self).form_valid(form)
#
#     def get_success_message(self, cleaned_data):
#         task_name = self.object.title
#         status_name = self.object.status
#         success_message = f'You added the task "{task_name}" on your "{status_name}" "list!'
#         return success_message

@login_required
def create_task(request):
    user = request.user
    form = TaskForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = MemberUser.objects.get(id=user.id)
            task_name = form.cleaned_data.get('title')
            form.save()
            messages.success(request, f'You added the task "{task_name}" on your list!')
            return redirect('add-task')
        else:
            form = TaskForm(request.user)
    return render(request, 'tasks/create_tasks.html', {'form': form})


@login_required
def user_task(request):
    user = request.user
    alltasks = Task.objects.filter(user=user)
    return render(request, 'tasks/list_task.html',
                  {'alltasks': alltasks})


class DeleteViewTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete-task.html'
    success_url = reverse_lazy('list-of-taks')


@login_required
def update_task(request, task_id):
    task_id = Task.objects.get(pk=task_id)
    user = request.user
    if request.method == 'POST':
        form = TaskUpdateForm(user, request.POST, instance=task_id)
        if form.is_valid():
            form.save()
            redirect('list-of-taks')
    else:
        form = TaskUpdateForm(user)

    return render(request, 'tasks/update-task.html', {'form': form})


class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail_task.html'
    success_url = reverse_lazy('list-of-taks')
