from django.urls import path
from cashbox import views
from cashbox.views import CashboxView, ShiftsView

urlpatterns = [
    path('cashbox/', CashboxView.as_view(), name='cashbox'),
    path('shifts/', ShiftsView.as_view(), name='shifts'),
]
