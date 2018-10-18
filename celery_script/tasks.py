# -*- coding: utf-8 -*-

# from app import celery
from __future__ import absolute_import,unicode_literals

# from __future__ import absolute_import


from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

# 定时导入
#任务名称为config文件中定义
from celery_script import celery_test_demo

@celery_test_demo.task()
def import_data():
    print "定时任务：每10秒执行一次"
    # 记录日志
    logger.info(u"导入成功")
    return 'hello world'


@celery_test_demo.task()
def add_number(a,b):
    return a+b


# a= 10
# print(a)

