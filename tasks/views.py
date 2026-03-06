from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Task
from .forms import RegisterForm, LoginForm, TaskForm


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name or user.username}! Your account has been created.')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'tasks/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    
    # Filter
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    category_filter = request.GET.get('category', '')
    search_query = request.GET.get('search', '')

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    if category_filter:
        tasks = tasks.filter(category=category_filter)
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    total = Task.objects.filter(user=request.user).count()
    completed = Task.objects.filter(user=request.user, status='completed').count()
    pending = Task.objects.filter(user=request.user, status='pending').count()
    high_priority = Task.objects.filter(user=request.user, status='pending', priority='high').count()

    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form,
        'total': total,
        'completed': completed,
        'pending': pending,
        'high_priority': high_priority,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'category_filter': category_filter,
        'search_query': search_query,
    }
    return render(request, 'tasks/dashboard.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, f'Task "{task.title}" added successfully!')
        else:
            messages.error(request, 'Please fix the errors below.')
    return redirect('dashboard')


@login_required
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'completed'
    task.save()
    messages.success(request, f'Task "{task.title}" marked as completed!')
    return redirect('dashboard')


@login_required
def mark_pending(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'pending'
    task.save()
    messages.info(request, f'Task "{task.title}" marked as pending.')
    return redirect('dashboard')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    title = task.title
    task.delete()
    messages.success(request, f'Task "{title}" deleted successfully.')
    return redirect('dashboard')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
