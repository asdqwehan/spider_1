import scrapy
from crawler.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = [
        'http://dmoztools.net/Games/Video_Games/'
    ]

    def parse(self, response):
        '''
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        '''
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="title-and-desc"]')

        '''
        for site in sites:

            title = site.xpath('a/div[@class="site-title"]/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('div[@class="site-descr "]/text()').extract()[0]
            print(title, link, desc)
        '''
        items=[]
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div[@class="site-title"]/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract()[0]
            items.append(item)
        return items
