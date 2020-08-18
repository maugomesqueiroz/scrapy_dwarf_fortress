# -*- coding: utf-8 -*-
import scrapy


class CreaturesSpider(scrapy.Spider):
    name = 'Creatures'
    allowed_domains = ['dwarffortresswiki.org/index.php/DF2014:Creature']
    start_urls = ['http://dwarffortresswiki.org/index.php/DF2014:Creature/']

    def parse(self, response):
        pass
