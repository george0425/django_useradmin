# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:36
# Author   :George

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('欢迎进入移动端点餐界面！')