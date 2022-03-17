# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:12
# Author   :George

from django.urls import path
from mobile.views import index

urlpatterns = [
    path('',index.index,name='mobile_index'),
]
