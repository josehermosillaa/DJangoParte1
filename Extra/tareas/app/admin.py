from django.contrib import admin

from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'created_at')
    list_filter = ('status', 'assigned_to')
    search_fields = ('title','description')
    list_editable = ('status', 'assigned_to') #lo que podemos editar en la lista

    readonly_fields = ('created_at',)
    ordering = ('-created_at',) #descendente, si no coloco signo es ascendete
admin.site.register(Task, TaskAdmin)