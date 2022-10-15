from unicodedata import name
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import User
# Create your views here.

# 主页
def index(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('login:login'))
    return render(request, 'login/index.html')

# 登录
def login(request):
    if request.session.get('is_login', None):   # 不允许重复登录
        return redirect(reverse('login:index'))
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        # 判断账户是否已注册
        user = User.objects.get(name=username)
    # 未注册则返回提示
    except:
        messages.error(request, "用户不存在，请检查用户名！")
        return render(request, 'login/login.html')
    else:
        # 验证密码
        if password != user.password:
            messages.error(request, '密码错误！')
            return render(request, 'login/login.html')
        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
        return redirect(reverse('login:index'))

# 登出
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect(reverse('login:login'))
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect(reverse('login:login'))

# 注册
def register(request):
    # 若已经登录则直接跳转主页
    if request.session.get('is_login', None):
        return redirect(reverse('login:index'))
    if request.method == 'POST':
        register_form = request.POST
        username = register_form['username']
        password = register_form['password']
        email = register_form['email']
        same_name_user = User.objects.filter(name=username)
        if same_name_user:
            messages.error(request, '用户名已存在')
            return render(request, 'login/register.html')
        same_email_user = User.objects.filter(email=email)
        if same_email_user:
            messages.error(request, '该邮箱已被注册')
            return render(request, 'login/register.html')
        new_user = User()
        new_user.name = username
        new_user.password = password
        new_user.email = email
        new_user.save()
        messages.info(request, '注册成功！')
        return redirect(reverse('login:login'))
        
    return render(request, 'login/register.html')