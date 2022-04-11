# !usr/bin/env python
# -*- coding:utf-8 -*-
# Time     :2022/4/10 15:58
# Author   :George

import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myobject.settings')
django.setup()

celery_app = Celery('myobject')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

