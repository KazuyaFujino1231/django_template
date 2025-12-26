from django.urls import path

from .views import EchoView, HealthCheckView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='api-health'),
    path('echo/', EchoView.as_view(), name='api-echo'),
]
