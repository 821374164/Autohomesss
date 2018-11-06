# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import dumps

class AutohomePipeline(object):
    def __init__(self):
        self.filename = open('车辆信息.txt','a',encoding='utf-8')

    def process_item(self, item, spider):

        # self.filename.write(dumps(dict(item),ensure_ascii=False))
        jsontext = dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(str(jsontext))
        return item
    def close_spider(self, spider):
        self.filename.close()

