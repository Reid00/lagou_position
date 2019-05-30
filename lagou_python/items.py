# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouPythonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    job_title = scrapy.Field()
    job_city = scrapy.Field()
    job_company = scrapy.Field()
    job_company_label_list = scrapy.Field()
    job_address = scrapy.Field()
    job_education = scrapy.Field()
    job_first_type = scrapy.Field()
    job_salary = scrapy.Field()
    job_work_year = scrapy.Field()
