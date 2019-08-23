from django.urls import path
from cashier import views
from cashier.views import CashierView

urlpatterns = [
    # path('cashier_interface/', views.cashier_interface, name='cashier_interface'),
    path('cashier/', CashierView.as_view(), name='cashier_interface'),
    path('clear/', views.clear_session, name='clear_session'),
    path('add-to-card/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('save/', views.save_to_database, name='save_to_database'),
    path('employees_prepayment/', views.employees_prepayment, name='employees_prepayment'),
    path('save_log/', views.cashier_save, name='cashier_save'),
    path('report_save_of_cashier/', views.report_save_of_cashier, name='report_save_of_cashier'),
    path('log/', views.log_cash, name='log_cash'),
    # path('add-to-card/<int:id>/', views.add_to_cart_view, name='add_to_cart_view'),
    # path('change/', views.change_item_qty, name='change_item_qty'),
    # path('remove_from_cart/', views.remove_from_card_view, name='remove_from_cart'),
    # path('remove_from_card_view/<int:id>/', views.remove_from_card_view, name='remove_from_card_view'),

]
