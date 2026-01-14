# Extração de dados de livros do site teste [toscrape](https://books.toscrape.com/)
Nessa extração utilizei somente o framework Scrapy. Os dados extraídos serão salvos em JSON.

### Criando ambiente virtual
```bash
$ python3 -m venv venv && source/venv/bin/activate
```
### Instalando dependências
```bash
$ cd ./teste/teste && pip install -r requirements
```
### Executando spider
```bash
$ scrapy crawl teste
```
