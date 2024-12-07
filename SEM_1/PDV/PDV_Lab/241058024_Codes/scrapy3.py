import scrapy

class WhiskySpider(scrapy.Spider):
    name = 'whisky_spider'
    start_urls = ['https://www.gotoliquorstore.com/st/spirits/bourbon-whiskey/418']  # Replace with the actual URL you want to scrape

    def parse(self, response):
        # Select each product box
        products = response.css("li.item product product-item")

        for product in products:
            # Extract product name
            name = product.css("div.product details product-item-details h3 a::text").get()
            
            # Extract product description
            description = product.css("span.price::text").get()

            # Extract bottle size
            #size = product.css("span.qty::text").get()

            # Yield the extracted data
            yield {
                'name': name,
                'description': description,
                #'size': size
            }
