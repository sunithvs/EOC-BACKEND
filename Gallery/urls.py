from django.conf.urls import url
from Gallery import views

urlpatterns=[
    url(r'^gallery/$',views.galleryApi)
]