from django import forms 
from .models import LeaveRequest

class CreateLeaveRequest(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'title', 'comment', 'upload', 'leave', 'start_date', 'end_date'
        ]
    
class UpdateLeaveRequest(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'title', 'comment', 'upload', 'leave', 'start_date', 'end_date'
        ]
        