from django.urls import path
from .views import RoomView

urlpatterns = [
    path('rooms/', RoomView.as_view({'get':'list', 'post':'create'})),
    path('rooms/<int:pk>', RoomView.as_view({'get':'retrieve', 'put':'update'})),
]