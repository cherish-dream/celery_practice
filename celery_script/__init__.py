#-*- coding: utf-8 -*-
from __future__ import absolute_import
# from flask import Blueprint
# celery_run = Blueprint('celery_run',__name__)
# from . import tasks

# from flask_celery import Celery
#启动的时候必须是会指向到这个实例对象的
from celery import Celery

celery_test_demo = Celery('celery_script')

from celery_script import celeryconfig
celery_test_demo.config_from_object(celeryconfig) #导入配置


if __name__ == '__main__':
    celery_test_demo.start()