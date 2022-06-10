# creating our spider
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # allows us to make GET/POST request to a particular url
    def start_requests(self):
        # here we give the list of urls from which we want to scrape the data
        urls = [
            'http://quotes.toscrape.com/page/1/'
            # 'http://quotes.toscrape.com/page/2/',
            # 'http://quotes.toscrape.com/page/3/'
        ]
        # generator function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # we make a request on this url and when the response comes, we need to parse that response

    # parse method knows what to do with the particular response
    def parse(self, response):
        # we need to see from which page the response is coming / we made the GET request
        page = response.url.split("/")[-2]
        # saving the response in HTML file
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')

        # PARSED RESPONSE FROM THE FIRST PAGE
        # parse the response (all the quotes in a page) and save it in a JSON format
        for q in response.css("div.quote"):
            # text, author and tag for each quote
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()

             # yield this in the form of a dictionary
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }
        
        # check if there is a next page or not
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)