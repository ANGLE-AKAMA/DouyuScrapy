# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # 主播名
    anchorName = scrapy.Field()
    # 主播图片链接
    anchorPicLink = scrapy.Field()
    # 粉丝人数
    pepleNumber = scrapy.Field()
    # 主播签名
    anchorSigna = scrapy.Field()
    # 粉丝评价
    pepleEvalu = scrapy.Field()