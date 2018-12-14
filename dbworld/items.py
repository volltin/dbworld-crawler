# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbworldItem(scrapy.Item):
    msg_sent = scrapy.Field()
    msg_type = scrapy.Field()
    msg_from = scrapy.Field()
    msg_subject = scrapy.Field()
    msg_subject_link = scrapy.Field()
    msg_subject_content = scrapy.Field()
    msg_ddl = scrapy.Field()
    msg_webpage_link = scrapy.Field()
