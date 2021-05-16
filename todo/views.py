from todo.forms.ToDoListForm import ToDoListForm, ToDoListItemForm
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import ToDoList, ToDoListItem


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'todo/index.html')
    context['form'] = form
    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'todo/login.html')


@login_required
def index(request):
    if request.user.is_authenticated:
        data = ToDoList.objects.filter(user_id=request.user.id)
        return render(request, 'todo/index.html', {'list': data})


@login_required
def create_todo_list(request):
    form = ToDoListForm()
    if request.method == 'POST':
        list = ToDoList(user=request.user)
        form = ToDoListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'todo/create_list.html', {'create_todo_list': form})


@login_required
def create_todo_list_item(request, todolist_id):
    form = ToDoListItemForm()
    if request.method == 'POST':
        todo_list = ToDoList.objects.get(id=todolist_id)
        item = ToDoListItem(todolist=todo_list)
        form = ToDoListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_list_items', todolist_id)
    return render(request, 'todo/create_list_item.html', {'create_todo_list_item': form})


@login_required
def update_todo_list(request, id):
    form = ToDoList.objects.get(id=id)
    data = ToDoListForm(instance=form)
    if request.method == 'POST':
        list = ToDoListForm(request.POST, instance=form)
        if list.is_valid():
            list.save()
            return redirect(index)

    return render(request, 'todo/update_list.html', {'update_todo_list': data})


@login_required
def update_todo_list_item(request, id):
    item = ToDoListItem.objects.get(id=id)
    form = ToDoListItemForm(instance=item)
    if request.method == 'POST':
        form = ToDoListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_list_items', item.todolist.id)
    return render(request, 'todo/update_list_item.html', {'update_todo_list_item': form})


@login_required
def delete_todo_list(request, id):
    todo_list = ToDoList.objects.get(id=id)
    todo_list.delete()
    return redirect(index)


@login_required
def delete_todo_list_item(request, id):
    todo_list_item = ToDoListItem.objects.get(id=id)
    todolist_id = todo_list_item.todolist.id
    todo_list_item.delete()
    return redirect('todo_list_items', todolist_id)


@login_required
def todo_list_items(request, todolist_id):
    todo_list_items = ToDoListItem.objects.filter(todolist_id=todolist_id)
    todo_list = ToDoList.objects.get(id=todolist_id)
    if todo_list_items.count() == 0:
        return redirect(index)
    return render(request, 'todo/index.html', {'todo_list_items': todo_list_items, 'todo_list': todo_list})


def mark_todo_list_item(request, id):
    item = ToDoListItem.objects.get(id=id)
    if item.status == ToDoListItem.ToDoListItemStatus.UNCOMPLETED:
        item.status = ToDoListItem.ToDoListItemStatus.COMPLETED
    elif item.status == ToDoListItem.ToDoListItemStatus.COMPLETED:
        item.status = ToDoListItem.ToDoListItemStatus.UNCOMPLETED
    item.save()
    return redirect('todo_list_items', item.todolist.id)

    
def detail(request, id):
    todo_list_item = ToDoListItem.objects.get(id=id)
    return render(request, 'todo/detail.html', {'todo_list_item': todo_list_item})
