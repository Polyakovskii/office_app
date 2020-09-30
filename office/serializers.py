from rest_framework import serializers
from .models import Room, Worker, WorkerInRoom


class RoomWorkerInRoomSerializer(serializers.ModelSerializer):

    worker = serializers.SlugRelatedField(slug_field='name', read_only=True)

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

    def validate(self, data):
        if data['date_of_beginning'] > data['date_of_ending']:
            raise serializers.ValidationError("Date of ending can't be later then date of beginning")
        return data


class ListRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'capacity', 'count_of_workers_now')


class RetrieveRoomSerializer(serializers.ModelSerializer):

    workers_now = RoomWorkerInRoomSerializer(many=True)
    workers_for_all_time = RoomWorkerInRoomSerializer(many=True)

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
