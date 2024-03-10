
from django.contrib import admin
from django.urls import path
from stock.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='vhod'),
]
