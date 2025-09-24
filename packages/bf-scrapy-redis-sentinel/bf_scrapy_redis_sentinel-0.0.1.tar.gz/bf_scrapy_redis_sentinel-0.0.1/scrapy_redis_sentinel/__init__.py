# -*- coding: utf-8 -*-

__original_author__ = "Rolando Espinoza"
__author__ = "Gie"
__email__ = "593443714@qq.com"
__version__ = "2.0.0"

from pathlib import Path

from scrapy_tools.bfLog import Loguru
from scrapy_tools.inner_ip import get_inner_ip

inner_ip = get_inner_ip()

PRODUCTION_ENV_TAG = 'Linux'
# linux服务器，认为是非生产环境
if inner_ip[1] == PRODUCTION_ENV_TAG:
    nested_dir = Path('/mnt/logs/crawler')
    nested_dir.mkdir(parents=True, exist_ok=True)
    scrapy_log = Loguru(deep=2, log_file='/mnt/logs/crawler/crawler.log', local_ip=inner_ip[0], module='scrapy_crawl')
    inner_ip = inner_ip[0]
else:
    scrapy_log = Loguru(local_ip=inner_ip[0], module='scrapy_crawl')
    inner_ip = "127.0.0.1"
