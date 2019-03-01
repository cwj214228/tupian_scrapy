# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup

from tupian.items import TupianItem


class GettupianSpider(scrapy.Spider):
    name = 'gettupian'
    allowed_domains = ['www.guang.net/map.htm']
    start_urls = ['http://www.guang.net/map.htm']

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        start_url='http://www.guang.net/m/a/'
        data=TupianItem()
        for link in soup.find_all('a'):
            href = str(link.get('href')).split('/')[1]
            print(href)
            name = href.split('.')[0]
            end_url = start_url + name + '.jpg'
            path = 'd:/1PictureDown/'
            data['name']=name
            data['path']=path
            data['end_url']=end_url
            yield data



