import scrapy
import configparser
from HemnetScraping.HemnetScraping.items import HemnetscrapingItem


class HemnetSpider(scrapy.Spider):
    name = "HemnetSpider"

    houseItem = HemnetscrapingItem()
    config = configparser.ConfigParser()

    def start_requests(self):
        self.config.read('scrapy.cfg')
        # housing_type = self.config.get('HOUSINGTYPE', 'housing_type')
        # urls = ['https://www.hemnet.se/bostader?location_ids%5B%5D=17744&item_types%5B%5D={}&upcoming=1'.format(housing_type), ]
        urls = ['https://www.hemnet.se/bostader?location_ids%5B%5D=17744&item_types%5B%5D=bostadsratt&upcoming=1', ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def address_provision(self, response):
        address = str(response.xpath(
            '//*[@id="result"]/ul/li[1]/a/div[2]/div/div[1]/div[1]/h2/text()').extract())
        address = address.replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '').strip()
        return address

    def price_provision(self, response):
        price = str(response.xpath(
            '//*[@id="result"]/ul/li[1]/a/div[2]/div/div[2]/div[1]/div[1]/text()').extract())
        price = price.replace('\\n', '').replace('\'', '').replace('[', '').replace('\\xa0', '').replace(']', '').strip()
        return price

    def area_provision(self, response):
        area = str(response.xpath(
            '//*[@id="result"]/ul/li[3]/a/div[2]/div/div[2]/div[1]/div[2]/text()').extract())
        area = area.replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '').strip()
        return area

    def parse(self, response):
        self.houseItem['address'] = self.address_provision(response)
        self.houseItem['price'] = self.price_provision(response)
        self.houseItem['area'] = self.area_provision(response)
        self.log(self.houseItem['address'] + ' ' + self.houseItem['price'] + ' ' + self.houseItem['area'])