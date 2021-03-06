# Scrapy settings for zhe800_baoyou project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhe800_baoyou'

SPIDER_MODULES = ['zhe800_baoyou.spiders']
NEWSPIDER_MODULE = 'zhe800_baoyou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhe800_baoyou (+http://www.yourdomain.com)'
ITEM_PIPELINES=['zhe800_baoyou.pipelines.Zhe800BaoyouPipeline']
#mongodb set
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'seckills'
MONGODB_COLLECTION = 'seckill'
MONGODB_UNIQ_KEY = 'id'
MONGODB_ITEM_ID_FIELD = '_id'
MONGODB_SAFE = True
