from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .forms import AttendanceForm
from .models import Attendance
    
# Create your views here.
class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendance/attendance_form.html'
    success_url = reverse_lazy('attendance-list')

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'