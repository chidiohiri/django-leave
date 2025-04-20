from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Leave(models.Model):
    leave_type = models.CharField(max_length=100)

    def __str__(self):
        return self.leave_type

class LeaveRequest(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=(
            ('Pending', 'Pending'), 
            ('Approved', 'Approved'), 
            ('Rejected', 'Rejected')
        ), 
        default='Pending'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    upload = models.FileField(upload_to='leave_attachments/', null=True, blank=True)

    leave = models.ForeignKey(Leave, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.created_by} - {self.title}'




