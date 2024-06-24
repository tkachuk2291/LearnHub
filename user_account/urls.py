from rest_framework.routers import DefaultRouter

from django.urls import path, include

from user_account.views import RegisterView, UserWineViewSet

router = DefaultRouter()

router.register("user", UserWineViewSet, basename="user"),

urlpatterns = [path("", include(router.urls)),
               path("register/", RegisterView.as_view())]

app_name = "user_account"
