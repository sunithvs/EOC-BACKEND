"""eoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('eocAdmin/', admin.site.urls),
    url(r'^', include('news.urls')),
    url(r'^', include('Gallery.urls')),
    url(r'^', include('Innovation.urls')),
    url(r'^', include('Carousel.urls')),

]

admin.site.site_header = "EOC Admin"
admin.site.site_title = "EOC Admin Portal"
admin.site.index_title = "Equal Opportunity Cell Admin Portal"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
