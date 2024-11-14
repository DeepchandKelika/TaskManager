from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task, GoogleOAuthKeys
from .forms import TaskForm, GoogleOAuthKeysForm, UserInvitationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserInviteForm
from django.contrib import messages
from django.urls import reverse



def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@staff_member_required
def manage_google_keys(request):
    keys = GoogleOAuthKeys.objects.all()
    if request.method == 'POST':
        form = GoogleOAuthKeysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_google_keys')
    else:
        form = GoogleOAuthKeysForm()
    return render(request, 'tasks/manage_google_keys.html', {'form': form, 'keys': keys})

@staff_member_required
def invite_user(request):
    if request.method == 'POST':
        form = UserInvitationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # send an invitation email 
            send_mail(
                'Invitation to join Task Management App',
                'You are invited to join the Task Management App. Please click the link to register.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return redirect('invite_user')
    else:
        form = UserInvitationForm()
    return render(request, 'tasks/invite_user.html', {'form': form})

@staff_member_required
def invite_user_view(request):
    if not request.user.is_staff:
        return redirect('home')  

    if request.method == 'POST':
        form = UserInviteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            registration_link = request.build_absolute_uri(reverse('account_signup'))  # Example URL

            # Send an invitation email
            send_mail(
                'Invitation to Join Task Manager',
                f'You have been invited to join the Task Manager app. Please register using the following link: {registration_link}',
                'noreply@yourapp.com',  # Update this with your actual sender email
                [email],
                fail_silently=False,
            )
            messages.success(request,

 f'Invitation sent to {email}.')
            return redirect('admin:index')
    else:
        form = UserInviteForm()

    return render(request, 'admin/invite_user.html', {'form': form})

