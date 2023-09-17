from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from tasks.forms import TaskForm
from tasks.models import Task


# Create your views here.
class CreateTask(SuccessMessageMixin,CreateView):
    form_class = TaskForm
    template_name = 'tasks/create_tasks.html'
    module = Task
    success_url = reverse_lazy('add-task')


    def get_success_message(self, cleaned_data):
        task_name = self.object.title
        status_name = self.object.status
        success_message = f'You added the task "{task_name}" on your "{status_name}" "list!'
        return success_message


class ListTaskView(ListView):
    template_name = 'tasks/list_task.html'
    model = Task
    context_object_name = 'alltasks'


class DeleteViewTask(DeleteView):
    model = Task
    template_name = 'tasks/delete-task.html'
    success_url = reverse_lazy('list-of-taks')

