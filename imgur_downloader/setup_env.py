import os
import logging

from download import setup_download_dir, get_links

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')

client_id = os.getenv('IMGUR_CLIENT_ID')
if not client_id:
	raise Exception("Couldn't find IMGUR_CLIENT_ID env variable")

download_dir = setup_download_dir()
links = get_links(client_id)