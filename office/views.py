from office.models import Room, Worker
from rest_framework import viewsets
from rest_framework.response import Response
from office.serializers import ListRoomSerializer, \
    RetrieveRoomSerializer, \
    ListWorkerSerializer, \
    RetrieveWorkerSerializer, \
    AddWorkerInRoomSerializer
from office.filters import RoomsFilter
from django_filters import rest_framework as filters
from rest_framework.decorators import action
# Create your views here.


class RoomView(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.UpdateModelMixin
):

    queryset = Room.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = RoomsFilter
    default_serializer_class = ListRoomSerializer
    serializer_classes = {
        'list': ListRoomSerializer,
        'create': ListRoomSerializer,
        'retrieve': RetrieveRoomSerializer,
        'update': RetrieveRoomSerializer,
        'add_worker_to_room': AddWorkerInRoomSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=True, methods=['post'])
    def add_worker_to_room(self, request, pk):
        serializer = AddWorkerInRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = Room.objects.get(pk=pk)
        message, creation_status = room.add_worker(
            serializer.validated_data['worker'],
            serializer.validated_data['date_of_beginning'],
            serializer.validated_data['date_of_ending']
        )
        return Response(data=message, status=creation_status)


class WorkerView(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.UpdateModelMixin
):

    queryset = Worker.objects.all()
    default_serializer_class = ListWorkerSerializer
    serializer_classes = {
        'list': ListWorkerSerializer,
        'create': ListWorkerSerializer,
        'retrieve': RetrieveWorkerSerializer,
        'update': ListWorkerSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
