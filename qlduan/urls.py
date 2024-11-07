from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('dsnhanvien/', dsnhanvien),
    path('dsduan/<int:idduan>/', ctduan, name='ctduan'),
    path('suaduan/<int:idduan>/', duan),
    path('taoduan/', duan)
]