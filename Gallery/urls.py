from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Gallery import views

router = DefaultRouter()

router.register("programs/", views.ProgramApiViewSet)

urlpatterns = [
    path("", include(router.urls)),
    url(r'^gallery/$', views.galleryApi)
]
