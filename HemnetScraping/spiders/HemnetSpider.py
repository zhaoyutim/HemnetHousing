import scrapy
import configparser
from HemnetScraping.items import HemnetscrapingItem


class HemnetSpider(scrapy.Spider):
    name = "HemnetSpider"
    config = configparser.ConfigParser()

    def start_requests(self):
        self.config.read('scrapy.cfg')
        housing_type = self.config.get('HOUSINGTYPE', 'housing_type')
        for i in range(1, 10):
            url = 'https://www.hemnet.se/bostader?location_ids%5B%5D=17744&item_types%5B%5D={}&upcoming=1&page={}'.format(housing_type, i)
            yield scrapy.Request(url, callback=self.parse)

    def address_provision(self, address):
        # address = str(response.xpath(
        #     '//*[@id="result"]/ul/li/a/div[2]/div/div[1]/div[1]/h2/text()').extract())
        address = address.replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '').strip()
        return address

    def price_provision(self, price):
        # price = str(response.xpath(
        #     '//*[@id="result"]/ul/li/a/div[2]/div/div[2]/div[1]/div[1]/text()').extract())
        price = price.replace('\\n', '').replace('\'', '').replace('[', '').replace('\\xa0', '').replace(']', '').strip()
        return price

    def area_provision(self, area):
        # area = str(response.xpath(
        #     '//*[@id="result"]/ul/li/a/div[2]/div/div[2]/div[1]/div[2]/text()').extract())
        area = area.replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '').strip()
        return area

    def parse(self, response):
        addresses = response.xpath(
            '//*[@id="result"]/ul/li/a/div[2]/div/div[1]/div[1]/h2/text()').extract()
        prices = response.xpath(
            '//*[@id="result"]/ul/li/a/div[2]/div/div[2]/div[1]/div[1]/text()').extract()
        areas = response.xpath(
            '//*[@id="result"]/ul/li/a/div[2]/div/div[2]/div[1]/div[2]/text()').extract()
        for i in range(0, len(addresses)):
            houseItem = HemnetscrapingItem()
            houseItem['address'] = self.address_provision(str(addresses[i]))
            houseItem['price'] = self.price_provision(str(prices[i]))
            houseItem['area'] = self.area_provision(str(areas[i]))
            self.log(houseItem['address'] + '~' + houseItem['price'] + '~' + houseItem['area'])
            yield houseItem