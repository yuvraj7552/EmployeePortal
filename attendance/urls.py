from django.urls import path
from . import views

urlpatterns = [
    path("attendance/checkin/", views.AttendanceCheckInView.as_view(), name='attendance-create'),
    path("attendance/checkout/<int:pk>/", views.AttendanceCheckoutView.as_view(), name='attendance-checkout'),
    path("attendance/list/", views.AttendanceListView.as_view(), name='attendance-list'),
]