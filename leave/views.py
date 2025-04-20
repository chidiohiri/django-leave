from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from . import form as fm
from .models import Leave, LeaveRequest
from .filters import LeaveRequestFilter

# create leave request
@login_required
def create_leave_request(request):
    if request.method == 'POST':
        form = fm.CreateLeaveRequest(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.save()
            messages.success(request, 'Your leave request has been created and being reviewed')
            send_mail(
                'LEAVE REQUEST SUBMITTED', 
                f'Your leave reqest has been submitted and is now being reviewed by the HR team.', 
                'noreply@email.com', 
                [var.created_by.email], 
                fail_silently=False
            )
            return redirect('my-leave-requests')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('create-leave-request')
    else:
        form = fm.CreateLeaveRequest()
        context = {'form':form}
    return render(request, 'leave/create_leave_request.html', context)

# update leave request
@login_required
def update_leave_request(request, pk):
    leave_request = LeaveRequest.objects.get(pk=pk)

    if not leave_request.status == 'Pending':
        messages.warning(request, 'You cannot update this leave request.')
        return redirect('my-leave-requests')

    if request.method == 'POST':
        form = fm.UpdateLeaveRequest(request.POST, request.FILES, instance=leave_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Leave request information updated and saved')
            return redirect('leave-request-details', leave_request.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-leave-request', leave_request.pk)
    else:
        form = fm.UpdateLeaveRequest(instance=leave_request)
        context = {'form':form}
    return render(request, 'leave/update_leave_request.html', context)

# my leave requests
@login_required
def my_leave_requests(request):
    leave_requests = LeaveRequest.objects.filter(created_by=request.user).order_by('-created_on')

     # apply filter
    leave_requests_filter = LeaveRequestFilter(request.GET, queryset=leave_requests)
    filtered_leave_requests = leave_requests_filter.qs

    # pagination
    paginator = Paginator(filtered_leave_requests, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'leave_requests':page_obj, 'filter':leave_requests_filter}

    return render(request, 'leave/my_leave_requests.html', context)

# all leave requests (for hr)
@login_required
def all_leave_requests(request):
    leave_requests = LeaveRequest.objects.all().order_by('-created_on')

    # apply filter
    leave_requests_filter = LeaveRequestFilter(request.GET, queryset=leave_requests)
    filtered_leave_requests = leave_requests_filter.qs

    # pagination
    paginator = Paginator(filtered_leave_requests, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'leave_requests':page_obj, 'filter':leave_requests_filter}
    return render(request, 'leave/all_leave_requests.html', context)

# leave request details
@login_required
def leave_request_details(request, pk):
    leave_request = LeaveRequest.objects.get(pk=pk)
    context = {'leave_request':leave_request}
    return render(request, 'leave/leave_request_details.html', context)

# delete leave request
@login_required
def delete_leave_request(request, pk):
    leave_request = LeaveRequest.objects.get(pk=pk)

    if not leave_request.status == 'Pending':
        messages.warning(request, 'You cannot delete this leave request.')
        return redirect('my-leave-requests')
    
    leave_request.delete()
    messages.success(request, 'Leave request has been deleted')
    return redirect('my-leave-requests')

# approve leave request
@login_required
def approve_leave_request(request, pk):
    leave_request = LeaveRequest.objects.get(pk=pk)

    if leave_request.created_by == request.user:
        messages.warning(request, 'You cannot approve this leave request since you requested it.')
        return redirect('leave-request-details', leave_request.pk)

    if not leave_request.status == 'Pending':
        messages.warning(request, 'You cannot approve this leave request.')
        return redirect('all-leave-requests')
    
    leave_request.status = 'Approved'
    leave_request.save()
    send_mail(
        'LEAVE REQUEST APPROVED', 
        f'Your leave reqest has been approved by the HR Team. Do enjoy your time off and refresh.', 
        'noreply@email.com', 
        [leave_request.created_by.email], 
        fail_silently=False
        )
    messages.success(request, 'Leave request has been approved by you.')
    return redirect('leave-request-details', leave_request.pk)

# reject leave request
@login_required
def reject_leave_request(request, pk):
    leave_request = LeaveRequest.objects.get(pk=pk)

    if leave_request.created_by == request.user:
        messages.warning(request, 'You cannot approve this leave request since you requested it.')
        return redirect('leave-request-details', leave_request.pk)

    if not leave_request.status == 'Pending':
        messages.warning(request, 'You cannot delete this delete request.')
        return redirect('all-leave-requests')
    
    leave_request.status = 'Rejected'
    leave_request.save()
    send_mail(
        'LEAVE REQUEST REJECTED', 
        f'Your leave reqest has been rejected by the HR Team. Please meet the HR manager for futher review.', 
        'noreply@email.com', 
        [leave_request.created_by.email], 
        fail_silently=False
        )
    messages.success(request, 'Leave request has been rejected by you.')
    return redirect('leave-request-details', leave_request.pk)
