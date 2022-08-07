from django.conf.urls import url
from Innovation import views

urlpatterns=[
    url(r'^innovation/$',views.InnovationApi)
]