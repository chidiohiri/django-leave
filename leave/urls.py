from django.urls import path
from . import views 

urlpatterns = [
    path('create-leave-request/', views.create_leave_request, name='create-leave-request'), 
    path('update-leave-request/<int:pk>/', views.update_leave_request, name='update-leave-request'), 
    path('my-leave-requests/', views.my_leave_requests, name='my-leave-requests'), 
    path('all-leave-requests/', views.all_leave_requests, name='all-leave-requests'), 
    path('leave-request-details/<int:pk>/', views.leave_request_details, name='leave-request-details'), 
    path('delete-leave-request/<int:pk>/', views.delete_leave_request, name='delete-leave-request'), 
    path('approve-leave-request/<int:pk>/', views.approve_leave_request, name='approve-leave-request'), 
    path('reject-leave-request/<int:pk>/', views.reject_leave_request, name='reject-leave-request')
]