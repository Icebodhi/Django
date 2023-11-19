from django.shortcuts import render, redirect
from .models import Password

def create_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = Password(username=username)
        new_password.set_password(password)
        new_password.save()
        return redirect('password_list')
    return render(request, 'create_password.html')

def password_list(request):
    passwords = Password.objects.all()
    return render(request, 'password_list.html', {'passwords': passwords})