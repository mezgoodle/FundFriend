from rest_framework import routers

from core.auth.viewsets import LoginViewSet, RefreshViewSet, RegisterViewSet
from core.bank.viewsets import BankViewSet
from core.document.viewsets import DocumentViewSet
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"banks", BankViewSet, basename="bank")
router.register(r"documents", DocumentViewSet, basename="document")
router.register(r"auth/register", RegisterViewSet, basename="register")
router.register(r"auth/login", LoginViewSet, basename="login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

urlpatterns = [*router.urls]
