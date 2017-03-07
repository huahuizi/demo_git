# coding:utf-8
import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
from pymongo import MongoClient
HOST = settings["HOST"]
PORT = settings["PORT"]
DB = settings["DB"]
COLLECTION = settings["COLLECTION"]

class MongoDBPipeline(object):
    def __init__(self):
        connection = MongoClient(
            HOST,
            PORT
       )
        db = connection[DB]
        self.collection = db[COLLECTION]
        self.ids_seen = set()
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if item['url'] not in self.ids_seen:
            self.collection.insert(dict(item))
            self.ids_seen.add(item['url'])
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
