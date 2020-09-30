from django.contrib import admin
from office.models import Worker, Room, WorkerInRoom
# Register your models here.

admin.site.register(Worker)
admin.site.register(WorkerInRoom)
admin.site.register(Room)
