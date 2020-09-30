from django.db import models
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def history_of_work(self):
        return list(self.workerinroom_set.all())


class Room(models.Model):
    capacity = models.PositiveIntegerField()

    @property
    def workers_now(self):
        return list(self.workerinroom_set.filter(date_of_ending__gte=datetime.date.today()))

    @property
    def count_of_workers(self):
        return self.workerinroom_set.filter(date_of_ending__gte=datetime.date.today()).count()

    def add_worker(self, worker, date_of_beginning, date_of_ending):
        if WorkerInRoom.objects.filter(date_of_ending__gte=date_of_beginning, date_of_beginning__lte=date_of_beginning).count() < self.capacity:
            if worker.workerinroom_set.filter(models.Q(date_of_ending__gte=date_of_beginning, date_of_beginning__lte=date_of_beginning)|
                                              models.Q(date_of_ending__lte=date_of_ending, date_of_beginning__gte=date_of_beginning)|
                                              models.Q(date_of_ending__gte=date_of_ending, date_of_beginning__lte=date_of_ending)
                                              ).count() == 0:
                WorkerInRoom.objects.create(room=self,
                                            worker=worker,
                                            date_of_beginning=date_of_beginning,
                                            date_of_ending=date_of_ending)
                return "Successfully created", status.HTTP_201_CREATED
            else:
                return 'Person works somewhere else in this period', status.HTTP_400_BAD_REQUEST
        else:
            return "No free places", status.HTTP_400_BAD_REQUEST


class WorkerInRoom(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_of_beginning = models.DateField()
    date_of_ending = models.DateField()
