from django import forms
from todo.models import ToDoList, ToDoListItem


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = ['user', 'create_date']


class ToDoListItemForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Deadline'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Item Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' Description '}))

    class Meta:
        model = ToDoListItem
        exclude = ['todolist', 'create_date', 'status']
