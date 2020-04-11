# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from WebScrapting.models import HousingStatus


class HemnetscrapingItem(DjangoItem):
# class HemnetscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # address = scrapy.Field()
    # price = scrapy.Field()
    # area = scrapy.Field()
    django_model = HousingStatus