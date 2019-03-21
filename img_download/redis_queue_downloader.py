import os
import logging
from redis import Redis
from rq import Queue

from download import download_link, setup_download_dir, get_links

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
log = logging.getLogger(__name__)

if __name__ == '__main__':
	client_id = os.getenv('IMGUR_CLIENT_ID')
	if not client_id:
		raise Exception("Couldn't find IMGUR_CLIENT_ID env variable")

	download_dir = setup_download_dir()
	links = get_links(client_id)

	q = Queue(connection=Redis(host='localhost', port=6379))
	for link in links:
		q.enqueue(download_link, download_dir, link)
