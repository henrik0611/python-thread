from functools import partial
from multiprocessing.pool import Pool
from time import time

from setup_env import *
from download import download_link

logger = logging.getLogger(__name__)

def main():
    ts = time()
    download = partial(download_link, download_dir)
    p = Pool(4)
    p.map(download, links)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()