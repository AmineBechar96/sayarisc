import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime

class OuedknissSpider(CrawlSpider):
    name = 'ouedkniss'
    allowed_domains = ['www.ouedkniss.com']
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url='https://www.ouedkniss.com/annonces/index.php?c=automobiles&prix=1&prix_min=50&prix_max=1000&trier=1000&p=150',headers={'User-Agent':self.user_agent})


    rules = (
          Rule(LinkExtractor(restrict_xpaths=('//li[@class="annonce_titre"]/a')), callback='parse_item', follow=False,process_request="set_user_agent"),
             Rule(LinkExtractor(restrict_xpaths=('(//div[@id="divPages"]/a)[1]')),process_request="set_user_agent")
         )


    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_item(self, response):
        
        yield {

                'id':response.xpath('//span[@itemprop="productID"]/text()').get(),
                'model':response.xpath('//h1/text()').get(),
                'brand':response.xpath('//h1/text()').get(),
                'notes':response.xpath('//h1/text()').get(),
                'proDate':response.xpath('//h1/text()').get(),
                'type' : response.xpath('//p[@id="Catégorie"]/span/text()').get(),
                'energie' : response.xpath('//p[@id="Energie"]/span/text()').get(),
                'kilometrage' : response.xpath('//p[@id="Kilométrage"]/span/text()').get(),
                'price':response.xpath('//p[@id="Prix"]/span/text()').get(),
                'moteur' : response.xpath('//p[@id="Moteur"]/span/text()').get(),
                'transmission' : response.xpath('//p[@id="Transmission"]/span/text()').get(),
                'couleur' : response.xpath('//p[@id="Couleur"]/span/text()').get(),
                'papiers' : response.xpath('//p[@id="Papiers"]/span/text()').get(),
                'url':response.url,
                'date_annonce':response.xpath('(//div/p[@id="Catégorie"]/preceding-sibling::p)[last()]/span[@class="description_span"]/text()').get(),
                'location':response.xpath('//p[@class="Adresse"]/text()').get(),
                'adDate':datetime.strftime(datetime.today(),'%Y-%m-%d')}