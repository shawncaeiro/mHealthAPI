# Shawn Caeiro
from views import HealthView
from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^health[/]?$', HealthView.as_view(), name='health_view'),  
]