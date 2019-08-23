from django.urls import path
from report.views import ReportView

urlpatterns = [
    path('report/', ReportView.as_view(), name='report'),

]
