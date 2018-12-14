import scrapy
from dbworld.items import DbworldItem

class DbworldSpider(scrapy.Spider):
    name = 'dbworld'

    allowed_domains = [
        "research.cs.wisc.edu",
        "www.cs.wisc.edu"
    ]
    start_urls = [
        "https://research.cs.wisc.edu/dbworld/browse.html"
    ]

    def parse(self, response):
        # filename = "list.html"
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        for tbody in response.xpath('/html/body/table/tbody'):
            item = DbworldItem()
            item['msg_sent'] = tbody.xpath('tr/td[1]/text()').extract()[0].strip()
            item['msg_type'] = tbody.xpath('tr/td[2]/text()').extract()[0].strip()
            item['msg_from'] = tbody.xpath('tr/td[3]/text()').extract()[0].strip()
            item['msg_subject'] = tbody.xpath('tr/td[4]/a/text()').extract()[0].strip()
            item['msg_subject_link'] = tbody.xpath('tr/td[4]/a/@href').extract()[0].strip().replace("http://www", "https://research")
            item['msg_ddl'] = tbody.xpath('tr/td[5]/text()').extract()[0].strip()
            if len(tbody.xpath('tr/td[6]/a/text()').extract()):
                item['msg_webpage_link'] = tbody.xpath('tr/td[6]/a/@href').extract()[0].strip()
            yield scrapy.Request(url=item['msg_subject_link'], callback=self.parse_subject, meta={'data':item})

    def parse_subject(self, response):
        item = response.meta['data']
        item['msg_subject_content'] = response.text
        yield item
