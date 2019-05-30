# -*- coding: utf-8 -*-
import json

import scrapy
import time
import random


class PositionPythonSpider(scrapy.Spider):
    name = 'position_python'
    allowed_domains = ['lagou.com']

    # start_urls = ['https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false']

    start_urls = [
        'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=']

    # def start_requests(self):
    #     yield scrapy.FormRequest(url=self.start_urls[0], callback=self.parse, meta={'cookiejar': 1})

    def start_requests(self):
        for url in self.start_urls:
            for i in range(1, 3):
                data = {
                    'first': 'false',
                    'pn': str(i),
                    'kd': 'python'
                }
                yield scrapy.FormRequest(url, callback=self.parse, formdata=data, method='post', )
                time.sleep(random.random()*5)

    def parse(self, response):
        cookie = response.headers.getlist('Set-Cookie')
        print(response.text)
        print('fist time get the cookie in the backend :', cookie)

        # if data:
        #     content = data.get('content')
        #     position_res= content['positionResult']

        # content = response.xpath('div[@class="content_left"]')
        # title = content.xpath('//a[@class="position_link"]/h3/text()').extract()
        # location = content.xpath('//span[@class="add"]/text()').extract()
        # salary = content.xpath('//span[@class="money"]/text()').extract()
        # work_year = content.xpath('//div[@class="p_bot"]/div[@class="li_b_l"]/text()').extract()
        # tag = content.xpath('//div[@class="list_item_bot"]/div[@class="li_b_l"]/span/text()').extract()
        # commany_name = content.xpath('//div[@class="company_name"]/text()').extract()
        # company_comment = content.xpath('//div[@class="list_item_bot"]/div/text()').extract()

    def parse_content(self, response):
        print(response.text)
