from rest_framework.routers import DefaultRouter

from django.urls import path, include

from user_account.views import RegisterView, UserViewSet

router = DefaultRouter()

router.register("user", UserViewSet, basename="user"),


urlpatterns = [path("", include(router.urls)),
               path("sign_up/", RegisterView.as_view())]

app_name = "user_account"
