import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/samara/category/svet"]

    def parse(self, response):
         lights = response.css('[class*="ProductCardMain_container__"]')
         for light in lights:
             yield {
                 'name': light.css('div.ActiveProduct::text').get(),
                 'price': light.css('[class*="FullPrice_actual__"]::text').get(),
                 'url' : light.css('a').attrib['href']
             }
