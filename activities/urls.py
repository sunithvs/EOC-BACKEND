from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register("activities", views.ActivityApiViewSet)

urlpatterns = [
    path("", include(router.urls)),

]
