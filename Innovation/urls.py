from django.conf.urls import url
from Innovation import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("innovation", views.InnovationApiViewSet)


urlpatterns = [
    path("", include(router.urls)),
   
]
