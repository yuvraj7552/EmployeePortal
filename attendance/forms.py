from .models import Attendance
from django import forms

class AttendanceCheckInForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['user', 'date', 'start_time', 'start_location']
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'