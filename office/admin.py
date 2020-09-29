from django.contrib import admin
from .models import Worker, Room, WorkerInRoom
# Register your models here.

admin.site.register(Worker)
admin.site.register(WorkerInRoom)
admin.site.register(Room)
