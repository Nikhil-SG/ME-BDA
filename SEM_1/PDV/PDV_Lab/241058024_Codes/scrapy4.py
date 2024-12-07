# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:57:00 2023

@author: MAHE
"""

import scrapy
from ..items import QuotesElementsDatabase4Item

class QuoteSpider(scrapy.Spider):
    name = 'books'
    page_number = 1
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']
    
    def parse(self, response):
        
        items = QuotesElementsDatabase4Item()
        
        # 1. quotes 2. Author 3. tag
        
        all_div_quotes = response.css('ol.row')
        
        for quotes in all_div_quotes:
        
            title = quotes.css('h3 a::attr(title)').extract()
            price = quotes.css('p.price_color::text').extract()
            rating = quotes.css('p.star-rating::attr(class)').extract()
            availability_list = quotes.css('p.instock.availability::text').getall()
            availability = ''.join([text.strip() for text in availability_list if text.strip()]).strip()
            items['title'] = title
            items['price'] = price
            items['rating'] = rating
            items['availability'] = availability
            
        
            yield items
        next_page = 'https://books.toscrape.com/catalogue/page-'+str(QuoteSpider.page_number)+'.html'
    
        if QuoteSpider.page_number < 51:
            yield response.follow(next_page, callback = self.parse)
            QuoteSpider.page_number += 1    
