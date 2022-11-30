from django.urls import path, include
from assets.views import assets_views as views

urlpatterns = [
    path('assets/',views.assetsGetPost, name="assets"),
    path('assets/<str:pk>/',views.assetGetUpdateDelete, name="asset"),
]
