
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('olxapp.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
]
