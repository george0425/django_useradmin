# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/16 17:43
# Author   :George

from django.shortcuts import render,redirect,reverse
from myadmin.models import User
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
import hashlib
import random

def index(request,page_index=1):

    try:
        tail = []
        kw = request.GET.get('keyword',None)
        if kw:
            user_list = User.objects.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
            tail.append('keyword='+kw)
        else:
            user_list = User.objects.filter()
        page = Paginator(user_list, 5)
        max_page = page.num_pages
        page_index = int(page_index)
        if page_index < 1:
            page_index = 1
        if page_index > max_page:
            page_index = max_page
        page_list = page.page_range
        user_list = page.page(int(page_index))
        context = {"user_list":user_list,'page_list':page_list,"cur_page":page_index,'tail':tail}
        return render(request,'myadmin/user/index.html',context=context)
    except Exception as e:
        return HttpResponse(e)

def add(request):

    return render(request,'myadmin/user/add.html')


def insert(request):
    try:
        ob = User()
        username = request.POST['username']
        nickname = request.POST['nickname']
        print(username)
        print(nickname)
        ob.username = username
        ob.nickname = nickname
        n = random.randint(100000, 999999)
        password = request.POST['password'] + str(n)
        print(password)
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n
        ob.status = request.POST["status"]
        ob.save()
        return redirect(reverse('myadmin_userindex',args=(1,)))
    except Exception as e:
        return HttpResponse(e)


def delete(request):

    return render(request,'myadmin/user/index.html')


def do_delete(request):

    return render(request,'myadmin/user/index.html')

def edit(request):
    return render(request, 'myadmin/user/index.html')