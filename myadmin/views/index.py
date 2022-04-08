# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:35
# Author   :George

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from myadmin.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as Dlogin
from PIL import Image,ImageDraw,ImageFont
from django.views.decorators.cache import cache_page
import hashlib
import random

# Create your views here.
@cache_page(15)
def index(request):
    # print(request.COOKIES.get('username'))
    if request.method == 'GET':
        if request.session.get('username'):

            return render(request, 'myadmin/index/index.html')

        elif request.COOKIES.get('username'):
            request.session['username'] = request.COOKIES.get('username')
            # return render(request, 'myadmin/index/index.html')
            return redirect(reverse('myadmin_login'))
    return redirect(reverse('myadmin_login'))

def login(request):
    if request.method == 'GET':
        if request.session.get('username'):
            return redirect(reverse('myadmin_index'))
        else:
            return render(request, 'myadmin/index/login.html')
    else:
        return render(request,'myadmin/index/login.html')

def dologin(request):
    if request.method == 'GET':
        return redirect(reverse('myadmin_login'))

    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info': '验证码错误！'}
        return render(request, "myadmin/index/login.html", context=context)
    try:
        username = request.POST['username']
        password = request.POST['password']
        if not username:
            context = {'info': '用户名为空！'}
            return render(request, "myadmin/index/login.html", context=context)
        user = authenticate(username=username,password=password)
        if user:
            ret = redirect(reverse('myadmin_index'))

            Dlogin(request,user)
            request.session['username'] = user.username
            ret.set_cookie(key='username', value=username, max_age=7200)
            return ret

        context = {"info":'用户名或密码错误'}
        return render(request, 'myadmin/index/login.html', context=context)
    except Exception as e:

        context = {"info": e}
        return render(request,'myadmin/index/login.html',context=context)


def dologout(request):
    logout(request)
    print(request.COOKIES.get('username'))
    return redirect(reverse('myadmin_login'))

def verify(request):
    bgcolor = (242,164,247)
    width = 100
    height = 25
    im = Image.new(mode='RGB',size=(width,height),color=bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
        # 定义验证码的备选值
        # str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/arial.ttf', 21)
    # font = ImageFont.load_default().font
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')