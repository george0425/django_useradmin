# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/15 13:12
# Author   :George

from django.urls import path
from myadmin.views import index,user

urlpatterns = [
    path('',index.index,name='myadmin_index'),
    path('index/<int:page_index>',user.index,name='myadmin_userindex'),
    path('add',user.add,name='myadmin_useradd'),
    path('insert',user.insert,name='myadmin_userinsert'),
    path('delete',user.delete,name='myadmin_userdelete'),
    path('do_delete',user.do_delete,name='myadmin_dodetete'),
    path('edit',user.edit,name='myadmin_useredit'),

]