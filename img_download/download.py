import json
import logging
import os
import requests
import pathlib2
from urllib import urlopen

log = logging.getLogger(__name__)
types = {'image/jpeg', 'image/png'}

def get_links(client_id):
	LIMIT = 10
	headers = {'Authorization': 'Client-ID {}'.format(client_id)}
	resp = requests.request('GET', 'https://api.imgur.com/3/gallery/random/random/', headers=headers)
	data = resp.json()
	return [item['link'] for item in data['data'] if item.get('type') in types][:LIMIT]

def download_link(dir, link):
	download_path = dir / os.path.basename(link)
	image = urlopen(link)
	f = download_path.open('wb')
	f.write(image.read())
	log.info('Donwloaded %s', link)

def setup_download_dir():
	download_dir = pathlib2.Path('images')
	if not download_dir.exists():
		download_dir.mkdir()
	return download_dir

