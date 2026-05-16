# from django.utils import timezone
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, ListView, UpdateView
# # from employee.models import Employee
# from .forms import AttendanceCheckInForm, AttendanceCheckOutForm
# # from .models import Attendance
    
# # Create your views here.
# class AttendanceCheckInView(CreateView):
#     model = Attendance
#     form_class = AttendanceCheckInForm
#     template_name = 'attendance/attendance_form.html'
#     success_url = reverse_lazy('attendance-checkout')

#     def form_valid(self, form):
#         employee = Employee.objects.get(user=self.request.user)
#         form.instance.employee = employee
#         form.instance.date = timezone.now().date()
#         form.instance.start_time = timezone.now().time()
#         form.instance.end_time = None
#         form.instance.start_location = "Delhi"
#         form.instance.end_location = None
#         return super().form_valid(form)

# class AttendanceCheckoutView(UpdateView):
#     model = Attendance
#     form_class = AttendanceCheckOutForm
#     template_name = 'attendance/attendance_form.html'
#     success_url = reverse_lazy('attendance-list')

# def form_valid(self, form):
#     employee = Employee.objects.get(user=self.request.user)
#     form.instance.employee = employee
#     form.instance.date = timezone.now().date()
#     form.instance.start_time = timezone.now().time()
#     form.instance.start_location = "Delhi"
#     response = super().form_valid(form)
#     return redirect('attendance-checkout', pk=self.object.pk)

# class AttendanceListView(ListView):
#     model = Attendance
#     template_name = 'attendance/attendance_list.html'