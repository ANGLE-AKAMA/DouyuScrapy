# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
import os
import codecs
from Douyu.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline 
class DouyuPipeline(object):
    def __init__(self):
        self.f = codecs.open("douyu_pipe.json","w","utf-8")
    
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)
        self.f.write(content.join(",\n"))
        
        return item
    
    def close_spider(self,spider):
        self.f.close()
        

class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["anchorPicLink"])
    
    def item_completed(self, results, item, info):
        print("*"*20)
        imagePath = [x['path'] for ok,x in results if ok][0]
        print(imagePath)
        os.rename(IMAGES_STORE+imagePath,IMAGES_STORE+item["anchorName"]+".jpg")
        return item