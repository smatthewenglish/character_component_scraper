# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CharacterComponentScraperItem(Item):
	amalgamated_info = Field()    
	delimiter = Field()
	the_strokes = Field()

    