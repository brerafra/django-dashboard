from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('grid2/', grid2, name='grid2'),
    path('grid3/', grid3, name='grid3'),
]