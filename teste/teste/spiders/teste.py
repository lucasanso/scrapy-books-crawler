import scrapy

class Crawlerzudo(scrapy.Spider):
    name = "teste"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    # Não é possível alterar esse método parse, pois é o primeiro método (depois do __init__) que o spider busca
    def parse(self, response):
        link_item = response.css("h3 a::attr(href)").getall()

        for link in link_item:
            yield response.follow(link, callback=self.parse_livros)

        proxima_pagina = response.css(".next a::attr(href)").get()

        if proxima_pagina:
            yield response.follow(proxima_pagina, callback=self.parse)


    def parse_livros(self, response):
        item = {} 

        item["nome"] = response.css("h1::text").get()
        item["preco"] = response.css(".price_color::text").get()
        item["descricao"] = response.css("#product_description + p::text").get()

        yield item