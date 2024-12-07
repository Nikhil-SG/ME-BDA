import scrapy

class msis(scrapy.Spider):
    name='msisfaculty'
    start_urls=['https://www.manipal.edu/sois/department-faculty.html']

    def parse(self,response):
     print(response)
     for faculty in response.css('a.members-wp'):
        yield{
            'name':faculty.css('h4::text').get(),
            'Designation':faculty.css('p::text')[0].get(),
            'Email':faculty.css('p::text')[1].get()
        }
        