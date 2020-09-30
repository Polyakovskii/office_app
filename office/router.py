from .views import RoomView, WorkerView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('rooms', RoomView)
router.register('workers', WorkerView)