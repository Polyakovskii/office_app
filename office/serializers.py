from rest_framework import serializers
from .models import Room, Worker, WorkerInRoom


class RoomWorkerInRoomSerializer(serializers.ModelSerializer):

    worker = serializers.SlugRelatedField(slug_field='name', queryset=WorkerInRoom.objects.all())

    class Meta:
        model = WorkerInRoom
        fields = ('worker', 'date_of_beginning', 'date_of_ending')


class WorkerInRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkerInRoom
        fields = ('room', 'date_of_beginning', 'date_of_ending')


class AddWorkerInRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkerInRoom
        fields = ('worker', 'date_of_beginning', 'date_of_ending')

class ListRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('capacity', 'count_of_workers')


class RetrieveRoomSerializer(serializers.ModelSerializer):

    workers = RoomWorkerInRoomSerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"


class ListWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('id', 'name')


class RetrieveWorkerSerializer(serializers.ModelSerializer):

    history_of_work = WorkerInRoomSerializer(many=True)

    class Meta:
        model = Worker
        fields = '__all__'
