# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/3/17 18:01
# Author   :George

from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        url_list = [reverse('myadmin_login'),
                    reverse('myadmin_dologin'),reverse('myadmin_logout'),
                    reverse('myadmin_verify')]
        if re.match(r"^/myadmin",path) and (path not in url_list):
            if "adminuser" not in request.session:
                return redirect(reverse('myadmin_login'))
        response = self.get_response(request)
        return response