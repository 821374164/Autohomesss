# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 品牌
    name = scrapy.Field()
    # 车型
    carModel = scrapy.Field()
    # 结构
    structure = scrapy.Field()
    # 发动机
    engine = scrapy.Field()
    # 报价
    price = scrapy.Field()
    # 变速箱
    transmissionCase = scrapy.Field()