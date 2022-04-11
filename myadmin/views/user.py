# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/16 17:43
# Author   :George

from django.shortcuts import render,redirect,reverse
from myadmin.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.cache import cache_page
import logging
from django.core import mail
import traceback
import hashlib
import random

@cache_page(30)
def index(request,page_index=1):
    try:
        tail = []
        kw = request.GET.get('keyword',None)
        user = User.objects.filter(status__lt=9)
        if kw:
            user_list = user.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
            tail.append('keyword='+kw)
        else:
            user_list = user.filter()
        page = Paginator(user_list, 5)
        max_page = page.num_pages
        page_index = int(page_index)
        if page_index < 1:
            page_index = 1
        if page_index > max_page:
            page_index = max_page
        page_list = page.page_range
        user_list = page.page(int(page_index))
        # 登录用户的个人信息
        user_name = request.session.get('username')
        login_user = User.objects.get(username=user_name)
        context = {"user_list":user_list,'page_list':page_list,"cur_page":page_index,'tail':tail,"login_user":login_user}
        # mail.send_mail(
        #     subject='subject',
        #     message=str(context),
        #     from_email='yanggzhi@163.com',
        #     recipient_list=['516901569@qq.com']
        # )

        return render(request,'myadmin/user/index.html',context=context)
    except Exception as e:
        return HttpResponse(e)

def add(request):

    return render(request,'myadmin/user/add.html')


def insert(request):
    try:
        username = request.POST['username']
        nickname = request.POST['nickname']
        if not User.objects.filter(username=username).exists():

            password = request.POST['password']
            # User.objects.create(username=username,nickname=nickname,status=request.POST["status"],password=password)
            ob = User()
            ob.set_password(password)
            ob.username = username
            ob.nickname = nickname
            ob.status = request.POST["status"]
            ob.save()
            return redirect(reverse('myadmin_userindex',args=(1,)))
        else:
            print('用户名已存在！')
            return redirect(reverse('myadmin_useradd'))
    except Exception as e:
        return HttpResponse(e)


def delete(request):

    return render(request,'myadmin/user/index.html')


def do_delete(request,uid):
    try:
        ob = User.objects.filter(id=uid)
        ob.delete()
        return redirect(reverse('myadmin_userindex',args=(1,)))
    except Exception as e:
        return HttpResponse(e)

def edit(request,uid):
    try:
        ob = User.objects.get(id=uid)
        context = {'user':ob}
        return render(request, 'myadmin/user/edit.html',context=context)
    except Exception as e:
        return HttpResponse(e)
    # return HttpResponse('HELLO')

def update(request,uid):
    try:
        ob = User.objects.get(id=uid)
        nickname = request.POST['nickname']
        status = request.POST['status']
        ob.nickname = nickname
        ob.status = status
        ob.save()
        return redirect(reverse('myadmin_userindex',args=(1,)))
    except Exception as e:
        return HttpResponse(e)