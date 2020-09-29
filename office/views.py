from .models import Room, Worker, WorkerInRoom
from rest_framework import viewsets
from .serializers import ListRoomSerializer, RetrieveRoomSerializer, ListWorkerSerializer, RetrieveWorkerSerializer
# Create your views here.


class RoomView(viewsets.GenericViewSet,
               viewsets.mixins.ListModelMixin,
               viewsets.mixins.RetrieveModelMixin,
               viewsets.mixins.CreateModelMixin,
               viewsets.mixins.UpdateModelMixin):

    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return ListRoomSerializer
        if self.action in ('retrieve', 'update'):
            return RetrieveRoomSerializer


class WorkerView(viewsets.GenericViewSet,
                 viewsets.mixins.ListModelMixin,
                 viewsets.mixins.RetrieveModelMixin,
                 viewsets.mixins.CreateModelMixin,
                 viewsets.mixins.UpdateModelMixin):

    queryset = Worker.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'create', 'update'):
            return ListWorkerSerializer
        if self.action in 'retrieve':
            return RetrieveWorkerSerializer
