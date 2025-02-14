from django.urls import path, include
from .views import cv, cv_detail

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cv/', cv),
    path('cv/<int:pk>/', cv_detail),
]
