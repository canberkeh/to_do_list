from django.contrib import admin
from . import models


class ToDoListAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name', 'create_date']
    list_display = ['name', 'create_date']


admin.site.register(models.ToDoList, ToDoListAdmin)


class ToDoListItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name', 'create_date', 'status']
    list_display = ['name', 'create_date']


admin.site.register(models.ToDoListItem, ToDoListItemAdmin)
