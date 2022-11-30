from django.urls import path, include
from assets.views import employee_views as views
# from assets.views.employee_views import getEmployees

urlpatterns = [
    path('employees/',views.getEmployees, name="employees"),
    path('employees/<str:pk>/',views.getEmployee, name="employee"),
]
