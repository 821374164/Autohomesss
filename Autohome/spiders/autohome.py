import scrapy
import time
from ..items import AutohomeItem

class Login1Spider(scrapy.Spider):
    name = 'Autohome'
    allowed_domains = ['account.autohome.com.cn']

    def start_requests(self):
        url = "https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html"
        str_cookie = "__ah_uuid=B50262C4-5193-470A-BCEF-30C78064CDBE; fvlid=1536726819438LbAg30ru8E; sessionid=5AFE0FC7-FBCD-48D9-B717-FFB5B52D93C7%7C%7C2018-09-12+12%3A33%3A40.657%7C%7Cwww.baidu.com; sessionuid=5AFE0FC7-FBCD-48D9-B717-FFB5B52D93C7%7C%7C2018-09-12+12%3A33%3A40.657%7C%7Cwww.baidu.com; cookieCityId=110100; sessionip=219.142.86.70; area=110106; ahpau=1; __utma=1.2022982449.1536726834.1536737783.1541423090.4; __utmz=1.1541423090.4.4.utmcsr=autohome.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/beijing/; pcpopclub=f42a275167434c2790c1b9c5dd350c8404d2497e; clubUserShow=80890238|403|2|atx4p5qso|0|0|0||2018-11-05 21:58:10|0; autouserid=80890238; sessionuserid=80890238; sessionlogin=485288bd5eff4b9a9e44b078f299935304d2497e; ahpvno=25; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1541426823,1541487456; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1541487456; ref=www.baidu.com%7C0%7C0%7C0%7C2018-11-06+14%3A57%3A40.555%7C2018-09-12+12%3A33%3A40.657; ahrlid=1541487455380OdhXchu4hJ-1541489880470"
        cookies = {}

        print("ssssssssssssssssssssss")
        for t in str_cookie.split(";"):
            key, value = t.split("=", 1)
            cookies[key] = value
        yield scrapy.FormRequest(url, cookies=cookies, callback=self.parse)


    def parse(self,response):

        name = response.xpath('//div[@class="list-cont-main"]/div[1]/a[1]/text()').extract()
        carModel = response.xpath('//div[@class="list-cont-main"]/div[2]/div[1]/ul/li[1]/span/text()').extract()
        structure = response.xpath('//div[@class="list-cont-main"]/div[2]/div[1]/ul/li[2]/a/text()').extract()
        engine = response.xpath('//div[@class="list-cont-main"]/div[2]/div[1]/ul/li[3]/span/a/text()').extract()
        price = response.xpath('//div[@class="list-cont-main"]/div[2]/div[2]/div[1]/span/span/text()').extract()
        transmissionCase = response.xpath('//div[@class="list-cont-main"]/div[2]/div[1]/ul/li[4]/a/text()').extract()
        autohome = AutohomeItem()
        autohome['name'] = name
        autohome['carModel'] = carModel
        autohome['structure'] = structure
        autohome['engine'] = engine
        autohome['price'] = price
        autohome['transmissionCase'] = transmissionCase
        print(autohome)
        yield autohome




