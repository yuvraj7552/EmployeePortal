from django.db import models

# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.employee.user.username} - {self.date}"