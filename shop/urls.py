from django.urls import path

from shop import views
from shop.views import ShopView, EmployeesView

urlpatterns = [
    path('shops/', ShopView.as_view(), name='shops'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('delete/users/<int:id>/', views.delete_users, name='delete_users'),
    path('delete/employees/<int:id>/', views.delete_employees, name='delete_employees'),
    path('delete/shop/<int:id>/', views.delete_shop, name='delete_shop'),
]
