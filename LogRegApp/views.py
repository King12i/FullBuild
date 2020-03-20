from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

# Create your views here.
def logreg(request):
    return render(request, "logreg.html")

def register(request):
    errors = User.objects.reg_val(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw
            )
        request.session['user_id'] = new_user.id
        return redirect('/dashboard/books')

def login(request):
    user = User.objects.filter(email=request.POST['email'])

    if user:    
        logged_user = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/dashboard/books')
    
    messages.error(request, "Invalid email/password", extra_tags="login")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')