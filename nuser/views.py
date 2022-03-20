from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, post, dailypost, viptest
from django.contrib.auth.models import auth


@login_required(login_url='login')
def vip_staff(request):
    if request.user.is_staff:
        if request.method == 'POST':
            body = request.POST['body']
            postt = post.objects.create(body=body)
            postt.save()
            messages.info(request, 'POSTED')
            return redirect('vip_staff')
        else:
            return render(request, 'vip_staff.html')
    else:
        return redirect('logout')




@login_required(login_url='login')
def daily_staff(request):
    if request.user.is_staff:
        if request.method == 'POST':
            body = request.POST['body']
            post = dailypost.objects.create(body=body)
            post.save()
            messages.info(request, 'POSTED')
            return redirect('daily_staff')
        else:
            return render(request, 'daily_staff.html')
    else:
        return redirect('logout')


@login_required(login_url='login')
def test_staff(request):
    if request.user.is_staff:
        if request.method == 'POST':
            body = request.POST['body']
            post = viptest.objects.create(body=body)
            post.save()
            messages.info(request, 'POSTED')
            return redirect('test_staff')
        else:
            return render(request, 'test_staff.html')
    else:
        return redirect('logout')



def home(request):
    dailyposts = dailypost.objects.all().order_by('-date',)
    viptests = viptest.objects.all().order_by('-date',)
    context = {'dailyposts':dailyposts, 'viptests':viptests}
    return render(request, 'home.html', context)



def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def staff(request):
    if request.user.is_staff:
        return render (request, 'staff.html')
    else:
        return redirect('logout')


def contact(request):
    return render (request, 'contact.html')


def about_us(request):
    return render (request, 'about_us.html')

@login_required(login_url='login')
def plan_c(request):
    return render (request, 'plan_c.html')


@login_required(login_url='login')
def plan_b(request):
    return render (request, 'plan_b.html')


@login_required(login_url='login')
def plan_a(request):
    return render (request, 'plan_a.html')


@login_required(login_url='login')
def vip(request):
    if request.user.is_vip or request.user.is_staff:
        posts = post.objects.all().order_by('-date',)
        return render (request, 'vip.html', {'posts': posts})
    else:
        return redirect('pvip')

@login_required(login_url='login')
def pvip(request):
    return render (request, 'pvip.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_vip:
            auth.login(request, user)
            return redirect('/')
        elif user is not None and user.is_staff:
            auth.login(request, user)
            return redirect('staff')
        elif user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'INVALID LOGIN DETAILS')
            return redirect('login')
    else:
        return render (request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        email2 = request.POST['email2']
        password = request.POST['password']
        passpowrd2 = request.POST['password2']

        if password == passpowrd2:
            if email == email2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'EMAIL ALREADY EXIST')
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'USERNAME ALREADY EXIST')
                    return redirect ('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
                    user.save()
                    messages.info(request, 'SUCCESS PLEASE LOGIN')
                    return redirect('login')
            else:
                messages.info(request, 'EMAIL DOES NOT MATCH')
                return redirect('register')
        else:
            messages.info(request, 'PASSWORD DOES NOT MATCH')
            return redirect('register')
    else:
        return render (request, 'register.html')