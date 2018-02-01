import pprint
import logging

import pymongo
from scrapy.statscollectors import StatsCollector

logger = logging.getLogger(__name__)


class MongoDBStatsCollector(StatsCollector):
    collection_name = 'loggers'

    def __init__(self, crawler):
        super(MongoDBStatsCollector, self).__init__(crawler)
        self.mongo_uri = crawler.settings.get('MONGO_URI')
        self.mongo_db = 'loggers'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider, reason):
        if self._dump:
            logger.info("Dumping Scrapy stats:\n" + pprint.pformat(self._stats),
                        extra={'spider': spider})
            stats_to_db = {
                'start': self._stats.get('start_time'),
                'finish': self._stats.get('finish_time'),
                'total_time': (self._stats.get('finish_time') - self._stats.get('start_time')).seconds,
                'profiles_added': self._stats.get('item_scraped_count'),
                'errors': self._stats.get('log_count/ERROR', 0),
            }
            self.db[self.collection_name].insert_one(stats_to_db)
        self._persist_stats(self._stats, spider)
