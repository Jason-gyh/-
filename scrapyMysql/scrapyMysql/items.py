import scrapy

class ScrapymysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()  # 标签字段
    cont = scrapy.Field()  # 名言内容
    pass
