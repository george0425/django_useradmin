# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:35
# Author   :George

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from myadmin.models import User
import hashlib


# Create your views here.

def index(request):
    user_name = request.session['adminuser']
    login_user = User.objects.get(username=user_name)
    print(login_user.status)
    context = {"login_user":login_user}
    return render(request,'myadmin/index/index.html',context=context)

def login(request):
    return render(request,'myadmin/index/login.html')

def dologin(request):
    username = request.POST['username']
    md5 = hashlib.md5()
    user = User.objects.get(username=username)
    num = user.password_salt
    password = request.POST['password'] + str(num)
    md5.update(password.encode('utf-8'))
    print(password)
    if user.password_hash == md5.hexdigest():
        request.session['adminuser']=user.username
        return redirect(reverse('myadmin_index'))


def logout(request):
    del request.session['adminuser']
    return redirect(reverse('myadmin_login'))