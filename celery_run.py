#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Executes an example task on a Celery worker in the background. Before this file
is executed, the worker instance has to be started. In this example a single
solution for a given task is compiled, executed and tested. While building and
testing runs in the background, this files process sleeps and waits for the
worker to finish.

Start this example task:
    ./celery_run.py
"""

import celery_tasks
import time
import os
from libConCoCt import Task, Solution

# Available tasks: leapyear greaterZero
task_directory = os.path.join('tasks', 'greaterZero')
solution_file = (os.path.join('solutions', 'greaterZero', 'user2', 'solution.c'), )
building = celery_tasks.build_and_check_task_with_solution.delay(task_directory,
                                                                 solution_file)

while not building.ready():
    print('Waiting...')
    time.sleep(0.2)

print(building.get())