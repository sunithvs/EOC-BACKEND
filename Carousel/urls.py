from django.conf.urls import url
from Carousel import views

urlpatterns=[
    url(r'^carousel/$',views.CarouselApi)
]