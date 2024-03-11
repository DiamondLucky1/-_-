
from django.contrib import admin
from django.urls import path, include
from stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='vhod'),
]
