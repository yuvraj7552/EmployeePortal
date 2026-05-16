from django.db import models

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey('employee.User', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    start_location = models.CharField(max_length=255, blank=True, null=True)
    end_location = models.CharField(max_length=255, blank=True, null=True)
    task = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date}"