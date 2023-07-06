from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import UserDetails, Contact


def HomePage(request):
    return render(request,'home.html')



def SignUpPage(request):
    global name, email, phone, country, password
    # form = UserForm()
    if request.method == 'POST':
        # form = UserForm(data=request.POST)
        # print(form)
        # if form.is_valid():
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('country')
        password = request.POST.get('password')
        terms = request.POST.get('terms')
        print(terms)
        if User.objects.filter(email=email).exists():
            messages.warning(request, "User Already Exists!")
            return render(request, "signup.html")
        else:
            nw_user = User.objects.create_user(phone=phone, password=password, email=email, first_name=first_name,
                                               last_name=last_name,country=country)
            nw_user.is_active = True
            user_details = UserDetails(user=nw_user, accept_terms=terms)
            user_details.save()
            messages.success(request, "User created successfully. Please login in.")
            return render(request, "login.html")

    return render(request, "signup.html")



def LoginPage(request):
    return render (request, 'login.html')

