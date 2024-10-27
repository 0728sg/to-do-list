from django import forms
from .models import Task
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import TaskForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')
