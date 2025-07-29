from django.shortcuts import render, redirect
from .models import Blog, FormEntry

def home(request):
    blogs = Blog.objects.all()[:3]  # Fetch the latest 3 blogs
    return render(request, 'index.html', {'blogs': blogs})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        FormEntry.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'index.html')
