from rest_framework import routers

from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [*router.urls]
