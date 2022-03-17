# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:35
# Author   :George

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    return render(request,'myadmin/index/index.html')