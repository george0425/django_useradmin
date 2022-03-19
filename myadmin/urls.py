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
    path('delete/<int:uid>',user.delete,name='myadmin_userdelete'),
    path('do_delete/<int:uid>',user.do_delete,name='myadmin_dodetete'),
    path('edit/<int:uid>',user.edit,name='myadmin_useredit'),
    path('update/<int:uid>',user.update,name='myadmin_userupdate'),
    path('login',index.login,name='myadmin_login'),
    path('dologin',index.dologin,name='myadmin_dologin'),
    path('logout',index.dologout,name='myadmin_logout'),
    path('verify',index.verify,name='myadmin_verify'),
]