# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import Item
import pandas as pd
import os

class LagouPythonPipeline(object):
    def process_item(self, item, spider):
        df = pd.DataFrame({
            'book name': [item['name']],
            'book upc': [item['upc']],
            'book price': [item['price']],
            'book stock': [item['stock']],
            'book rating': [item['rating']],
            'book review': [item['review']],
        })

        if not os.path.exists('book.csv'):
            df.to_csv('book.csv', index=None, header=True, mode='a')
        else:
            df.to_csv('book.csv', index=None, header=None, mode='a')
        return item


class MongoPipeline(object):
    #  将数据存入MongoDB数据库中
    @classmethod
    def from_crawler(cls, crawler):
        # 类方法，读取settings.py中的配置，根据配置创建MongoPipeline对象
        cls.MONGO_CLIENT = crawler.settings.get('MONGO_CLIENT', 'mongodb://localhost:27017/')
        cls.MONGO_DB = crawler.settings.get('MONGO_DB', 'lagou_job_python')
        return cls()

    def open_spider(self, spider):
        # 创建MongoDB连接，指明连接的数据库和集合
        self.client = pymongo.MongoClient(self.MONGO_CLIENT)
        self.db = self.client[self.MONGO_DB]
        self.collection = self.db[spider.name]  # 集合名为spider.name

    def close_spider(self, spider):
        # 数据处理完后，关闭MongoDB连接
        self.client.close()

    def process_item(self, item, spider):
        # 将数据存入MongoDB集合中
        if isinstance(item, Item):  # 传入的item为Item类型，先转换为dict类型再存入MongoDB
            db_item = dict(item)
        else:
            db_item = item
        self.collection.insert_one(db_item)
        return item
