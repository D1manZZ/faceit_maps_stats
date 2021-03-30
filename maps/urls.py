from django.urls import path
from .views import *

urlpatterns = [
    path('', SetLink.as_view(), name='set_link'),
    path('view_maps/', ViewMaps.as_view(), name='view_maps')
]
