from django.contrib import admin
from .models import Task, TaskList, Attachment

admin.site.register(Task)
admin.site.register(TaskList)
admin.site.register(Attachment)
