from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('todo/register/', views.sign_up, name='register'),
    path('/todo/logout/', views.logout, name='logout'),
    path('todolists/create', views.create_todo_list, name='create_todo_list'),
    path('todolists/<str:todolist_id>/todolistitem/create', views.create_todo_list_item, name='create_todo_list_item'),
    path('todolists/<str:id>/update', views.update_todo_list, name='update_todo_list'),
    path('todolists/<str:id>/delete', views.delete_todo_list, name='delete_todo_list'),
    path('todolists/<str:todolist_id>/items', views.todo_list_items, name='todo_list_items'),
    path('todolistitem/<str:id>/delete', views.delete_todo_list_item, name='delete_todo_list_item'),
    path('todolistitem/<str:id>/update', views.update_todo_list_item, name='update_todo_list_item'),
    path('todolistitem/<str:id>/change_status', views.mark_todo_list_item, name='mark_todo_list_item'),
    path('todolistitem/<str:id>/detail', views.detail, name='detail'),
]
