from .models import Room, Worker, WorkerInRoom
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ListRoomSerializer, RetrieveRoomSerializer, ListWorkerSerializer, RetrieveWorkerSerializer, AddWorkerInRoomSerializer
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


class AddWorkerToRoomView(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin):
    queryset = WorkerInRoom.objects.all()
    serializer_class = AddWorkerInRoomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = Room.objects.get(pk=self.kwargs['pk'])
        worker = room.add_worker(serializer.validated_data['worker'],
                                 serializer.validated_data['date_of_beginning'],
                                 serializer.validated_data['date_of_ending'])
        if worker is None:
            return Response(data="The room is full")
        else:
            return Response(AddWorkerInRoomSerializer(worker).data, status=status.HTTP_201_CREATED)


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
