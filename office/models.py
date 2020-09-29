from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def history_of_work(self):
        return [a for a in self.workerinroom_set.all()]

class Room(models.Model):
    capacity = models.PositiveIntegerField()

    @property
    def workers(self):
        return [a for a in self.workerinroom_set.all()]

    @property
    def count_of_workers(self):
        return self.workerinroom_set.count()

    def add_worker(self, worker, date_of_beginning, date_of_ending):
        if self.workerinroom_set.count() < self.capacity:
            return WorkerInRoom.objects.create(worker=worker, date_of_beginning=date_of_beginning, date_of_ending=date_of_ending)
        else:
            return None


class WorkerInRoom(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_of_beginning = models.DateField()
    date_of_ending = models.DateField()
