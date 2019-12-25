import scrapy
import json
from scrapyProject.items import ScrapyprojectItem


class STencentSpider(scrapy.Spider):
    name = 's_tencent'
    allowed_domains = ['careers.tencent.com']
    start_urls = []
    for page in range(1, 70):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex=%s&pageSize=10' % page
        start_urls.append(url)

    def parse(self, response):
        # 读response的页面信息
        content = response.body.decode('utf-8')
        # json字符串转换为python格式
        data = json.loads(content)
        job_list = data['Data']['Posts']
        for job in job_list:
            # 每条职位都需要放入单独的ScrapyprojectItem类中
            item = ScrapyprojectItem()
            name = job['RecruitPostName']  # 工作名称
            country = job['CountryName']  # 工作国家
            duty = job['Responsibility']  # 工作职责
            # 使用数据模型存数据的时候，不要用.语法
            item['name'] = name
            item['duty'] = duty
            item['country'] = country

            yield item  # 生成一条数据就挂起，传给pipeline

            # next_page = response.css('li.next a::attr(href)').extract_first()  # css选择器提取下一页链接
            # if next_page is not None:  # 判断是否存在下一页
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页

            # info=name+country+duty+'\n'  # 本地文件测试
            # info = {
            #     "name": name,
            #     "country": country,
            #     "duty": duty,
            # }
            # with open('job.txt', 'a', encoding='utf-8') as fp:
            #     fp.write(str(info)+'\n')
