from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
import phonenumbers

from .models import CustomUser


def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "CN")  # CN代表中国

        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 使用手机号码进行用户认证
        print(f'username:{username},password:{password}')
        user = authenticate(request, username=username, password=password)
        print(f'user:{user}')
        if user is not None:
            login(request, user)
            return render(request,'index.html')  # 重定向到你的首页
        else:
            return HttpResponse('Invalid login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # 处理用户提交的注册信息
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        # 在这里保存用户信息到数据库，这里只是示例
        # 使用 make_password 函数对密码进行哈希处理
        hashed_password = make_password(password)
        user = CustomUser.objects.create(username=username, phone_number=phone_number, password=hashed_password)
        user.save()
        return redirect('registration_success')
    return render(request, 'register.html')


def registration_success(request):
    return render(request, 'register_success.html')