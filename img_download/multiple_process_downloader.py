import logging
import os
from functools import partial
from multiprocessing.pool import Pool
from time import time

from download import download_link, setup_download_dir, get_links

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID env variable")

    download_dir = setup_download_dir()
    links = get_links(client_id)

    ts = time()
    download = partial(download_link, download_dir)
    p = Pool(4)
    p.map(download, links)
    logging.info('Took %s seconds', time() - ts)