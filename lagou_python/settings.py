# -*- coding: utf-8 -*-

# Scrapy settings for lagou_python project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou_python'

SPIDER_MODULES = ['lagou_python.spiders']
NEWSPIDER_MODULE = 'lagou_python.spiders'

from fake_useragent import UserAgent

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lagou_python (+http://www.yourdomain.com)'
ua = UserAgent()
USER_AGENT = ua.random

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': USER_AGENT,
    'Refer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'Origin': 'https://www.lagou.com',
    'Cookie': 'JSESSIONID=ABAAABAAAGGABCBBA2AE96704533C8D151298E103C193F9; user_trace_token=20190520145716-173bbc9d-8c8e-4ab1-8d5b-90eafaee2d08; _ga=GA1.2.263002638.1558335439; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558335440; LGUID=20190520145719-82be4414-7acc-11e9-a433-525400f775ce; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=5687ed1c9a5b6ec21e996786e690e16e; _gid=GA1.2.1570025175.1559031925; X_HTTP_TOKEN=91bd26a7a3b5b43809321195517864ff1b3414ede9; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1559112391; LGRID=20190529144630-7dcb09b8-81dd-11e9-a165-5254005c3644; SEARCH_ID=acdb1cedc5c44cc6900aa1368fac0991'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lagou_python.middlewares.LagouPythonSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     # 'lagou_python.middlewares.LagouPythonDownloaderMiddleware': None,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'lagou_python.middlewares.RandomUserAgentMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lagou_python.pipelines.LagouPythonPipeline': 300,
    'lagou_python.pipelines.MongoPipeline': 450,

}
MONGO_CLIENT = 'mongodb://localhost:27017'
MONGO_DB = 'lagou_job_python'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
