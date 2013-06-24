import os
import redis
from rq import Worker, Queue, Connection
from ioos_service_monitor import redis_connection

listen = ['stats']

with Connection(redis_connection):
    worker = Worker(map(Queue, listen))
    worker.work()

