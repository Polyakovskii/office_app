from django.urls import path
from .views import RoomView, WorkerView, AddWorkerToRoomView

urlpatterns = [
    path('rooms/', RoomView.as_view({'get':'list', 'post':'create'})),
    path('rooms/<int:pk>', RoomView.as_view({'get':'retrieve', 'put':'update'})),
    path('rooms/<int:pk>/add', AddWorkerToRoomView.as_view({'post':'create'})),
    path('workers/', WorkerView.as_view({'get':'list', 'post':'create'})),
    path('workers/<int:pk>', WorkerView.as_view({'get':'retrieve', 'put':'update'})),
]
