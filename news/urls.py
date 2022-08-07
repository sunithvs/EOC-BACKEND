from django.conf.urls import url
from news import views

urlpatterns =[
    url(r'^event/$',views.newsApi),
    url(r'^event/([0-9]+)$',views.newsApi)
]