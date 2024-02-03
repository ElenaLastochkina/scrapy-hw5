import scrapy
import csv
 
class RankingSpider(scrapy.Spider):
    name = 'ranking_spider'
    allowed_domains = ['fifa.com']
    start_urls = ['https://www.fifa.com/fifa-world-ranking/']
 
    def parse(self, response):
        # Найдем таблицу с данными с помощью CSS селектора
        table = response.css('table.table.tbl-ranking')
 
        # Извлечем заголовки таблицы
        headers = table.css('th::text').getall()
 
        # Извлечем данные из строк таблицы
        rows = table.css('tr')
        data = []
        for row in rows:
            row_data = row.css('td::text').getall()
            data.append(row_data)
 
        # Сохраняем данные в CSV-файл
        with open('fifa_ranking_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
 
        self.log('Данные успешно сохранены в CSV-файл.')