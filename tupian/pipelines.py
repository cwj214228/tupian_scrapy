# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import requests

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 继承ImagesPipenine类，这是图片管道
class SaveImagePipeline(object):
    def process_item(self, item, spider):
        print(item['end_url'])
        res = requests.get(item['end_url'])
        with open('d:/1PictureDown/'+item['name']+'.jpg', 'wb') as f:
            f.write(res.content)
            f.close()
        return item

