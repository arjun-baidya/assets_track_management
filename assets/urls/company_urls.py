from django.urls import path, include
from assets.views import company_views as views

urlpatterns = [
    path('companies/',views.companyGetPost, name="company"),
    path('companies/<str:pk>/',views.companyGetUpdateDelete, name="company"),
    path('check/<str:pk>/',views.checkAssetReturn, name="check"),
]
