# -*- coding: utf-8 -*-

# celery_test/celery_app/celeryconfig.py
from __future__ import absolute_import,unicode_literals
from datetime import timedelta
from celery.schedules import crontab

# Broker and Backend
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Timezone
CELERY_TIMEZONE='Asia/Shanghai'    # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'


CELERY_ACCEPT_CONTENT = ['json','pickle']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# import
# CELERY_IMPORTS = (
#     'task'
# )

# from celery_script import tasks
CELERY_IMPORTS = ['celery_script.tasks']

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_script.tasks.import_data',
         'schedule': timedelta(seconds=30),      # 每 30 秒执行一次或者引入crontab进行编写
         'args': ()                             # 任务函数参数
    },
#     'multiply-at-some-time': {
#         'task': 'celery_app.task.lession',
#         'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
# #       'args': ()                               # 任务函数参数
#     }
    'add-numbers': {
         'task': 'celery_script.tasks.add_number',
         'schedule': timedelta(seconds=10),      # 每 30 秒执行一次或者引入crontab进行编写
         'args': (90,10),                             # 任务函数参数
    },

}
