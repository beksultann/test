from django.urls import path
from counterparties.views import SupplierDetailView, SupplierUpdateView, SupplierDeleteView, SupplierView, CustomerView

urlpatterns = [
    path('supplier/', SupplierView.as_view(), name='supplier'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('supplier/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),

]
