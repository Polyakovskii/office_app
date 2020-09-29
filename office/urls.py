from django.urls import path
from .views import RoomView, WorkerView

urlpatterns = [
    path('rooms/', RoomView.as_view({'get':'list', 'post':'create'})),
    path('rooms/<int:pk>', RoomView.as_view({'get':'retrieve', 'put':'update'})),
    path('workers/', WorkerView.as_view({'get':'list', 'post':'create'})),
    path('workers/<int:pk>', WorkerView.as_view({'get':'retrieve', 'put':'update'})),
]