from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    task_assign_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = TaskModel
        fields = '__all__'
