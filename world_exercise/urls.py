"""
world-exercise URL Configuration

"""
from django.urls import path, include


urlpatterns = [
    path('world/', include('world.urls'))
]
