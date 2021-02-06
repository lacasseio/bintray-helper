import sys
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class BintraySpider(scrapy.Spider):
    name = 'bintrayspider'
    link_extractor = LinkExtractor()

    def __init__(self, slug, *args, **kwargs):
        super(BintraySpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://dl.bintray.com/' + slug]

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            real_url = link.url.replace('/:', '/')
            if not real_url.endswith('/'):
                print(real_url)
            yield Request(real_url, callback=self.parse)
