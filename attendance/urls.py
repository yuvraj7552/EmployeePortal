from django.urls import path
from . import views

urlpatterns = [
    path("attendance/create/", views.AttendanceCreateView.as_view(), name='attendance-create'),
    path("attendance/list/", views.AttendanceListView.as_view(), name='attendance-list'),
]