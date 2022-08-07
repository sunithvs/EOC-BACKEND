from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Gallery import views

router = DefaultRouter()

router.register("programs", views.ProgramApiViewSet)
router.register("mentor", views.MentorApiViewSet)

urlpatterns = [
    path("", include(router.urls)),
    url(r'^gallery/$', views.galleryApi)
]
