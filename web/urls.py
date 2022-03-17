# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:12
# Author   :George

from django.contrib import admin
from django.urls import path,include
from web.views import index

urlpatterns = [
    path('',index.index,name='index'),
]
