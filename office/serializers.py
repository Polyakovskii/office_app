from rest_framework import serializers
from .models import Room, Worker, WorkerInRoom


class WorkerInRoomSerializer(serializers.ModelSerializer):

    worker = serializers.SlugRelatedField(slug_field='name', queryset=WorkerInRoom.objects.all())

    class Meta:
        model = WorkerInRoom
        fields = ('worker', 'date_of_beginning', 'date_of_ending')


class ListRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('capacity', 'count_of_workers')


class RetrieveRoomSerializer(serializers.ModelSerializer):

    workers = WorkerInRoomSerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"
