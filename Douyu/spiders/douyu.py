# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import DouyuItem
import json
import scrapy
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com','douyucdn.cn']
    baseUrl = 'https://www.douyu.com/gapi/rknc/directory/yzRec/'
    index = 1
    start_urls = [baseUrl+str(index)]

    def parse(self, response):
        if len(json.loads(response.body)['data'])==0 :
            return
        node_list = json.loads(response.body)['data']['rl']
        for node in node_list :
            item = DouyuItem()
            # 主播名
            item["anchorName"] = node['nn']
            # 粉丝人数
            item["pepleNumber"] = node['ol']
            # 主播图片链接
            item["anchorPicLink"] = node['rs1']
            # 主播签名
            item["anchorSigna"] = node['rn']
            # 粉丝评价
            if node['utag'] :
                item["pepleEvalu"] = ",".join([x['name'] for x in node['utag']])
            else :
                item["pepleEvalu"] = "主播还没有获得任何评价喔"
            yield item
        
        index +=1
        yield scrapy.Request(baseUrl+str(index),self.parse)
            