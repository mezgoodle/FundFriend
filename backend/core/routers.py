from rest_framework import routers

from core.auth.viewsets import RegisterViewSet
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"auth/register", RegisterViewSet, basename="register")

urlpatterns = [*router.urls]
