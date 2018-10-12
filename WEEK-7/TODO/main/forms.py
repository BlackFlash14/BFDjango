from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_owner', 'task_due_on', 'task_done')
        widgets = {
            'task_due_on': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }