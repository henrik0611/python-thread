import logging
from redis import Redis
from rq import Queue

from setup_env import *
from download import download_link

log = logging.getLogger(__name__)

if __name__ == '__main__':
	q = Queue(connection=Redis(host='localhost', port=6379))
	for link in links:
		q.enqueue(download_link, download_dir, link)
