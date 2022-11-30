from django.urls import path, include
from assets.views import distribution_views as views

urlpatterns = [
    path('distributions/',views.distributionsGetPost, name="distributions"),
    path('distributions/<str:pk>/',views.distributionGetUpdateDelete, name="distribution"),
]
