import scrapy
# from scrapy.spider import BaseSpider as Spider
# from scrapy.crawler import CrawlerProcess
# from scrapy import Spyder

class GameSpider(scrapy.Spider):
    name = 'sgames'


    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = ['http://www.vgchartz.com/gamedb/']

    # website_pages = [str(i) for i in range(2, 1085)]
    website_pages = [str(i) for i in range(2, 100)]
    #1085
    for i in website_pages:
        url = 'http://www.vgchartz.com/games/games.php?page='
        url2 = '&results=50&name=&console=&keyword=&publisher=&genre=&order=Sales&ownership=Both&boxart=Both&banner=Both&showdeleted=&region=All&goty_year=&developer=&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&alphasort='
        start_urls.append(url + i + url2)

# http://www.vgchartz.com/games/games.php?page=1&results=50&name=&console=&keyword=&publisher=&genre=&order=Sales&ownership=Both&boxart=Both&banner=Both&showdeleted=&region=All&goty_year=&developer=&direction=&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&alphasort=
#     made="x"+i for i in raj\nge(2)
    # def start_requests(self):
    #     self.index = 0
    #     website_pages = [str(i) for i in range(2, 1085)]
    #     urls = []
    #     for i in website_pages:
    #         url = 'http://www.vgchartz.com/games/games.php?page='
    #         url2 = '&results=50&name=&console=&keyword=&publisher=&genre=&order=Sales&ownership=Both&boxart=Both&banner=Both&showdeleted=&region=All&goty_year=&developer=&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&alphasort='
    #         urls.append(url + i + url2)
    #         for url in urls:
    #             yield scrapy.Request(url=url, callback=self.parse)
        # We make a request to each url and call the parse function on the http response.



    def parse(self, response):
        # fot link in given_list
        # Extract the links to the individual festival pages
        game_links = response.xpath('//td[3]/a[1]/@href').extract()
        # game_names = response.xpath('//td[3]/a/text()').extract()
        # game_platform = response.xpath('//td[4]/img/@alt').extract()
        # publisher = response.xpath('//tr/td[5]/text()').extract()[3:]

        for i in range(len(game_links)):
            yield scrapy.Request(
            url=game_links[i],
            callback=self.parse_games,
            meta={'url': game_links[i]}
            # , 'name': game_names[i],
            # 'platform': game_platform[i]}
            # 'publisher': publisher[i]}
            )


    def parse_games(self, response):

        url = response.request.meta['url']

        name = (
        response.xpath('//*[@id="gameSplashImage"]/h1/a[1]/text()').extract()
        )

        platform = (
        response.xpath('//*[@id="gameSplashImage"]/h1/a[2]/text()').extract()
        )


        # publisher = (
        # response.xpath('//*[@id="gameGenInfoBox"]/p/a/text()[2]').extract()
        # )
        # name = response.request.meta['name']
        #
        # platform = response.request.meta['platform']


        # response.xpath('//span[@class="userscore"]').extract()

        ratings = (
        response.xpath('//*[@id="gameGenInfoBox"]/center').extract()
        )

        release_date = (
        response.xpath('//*[@id="gameGenInfoBox"]/p/a/text()').extract()[-3]
        )


        total_sales = (
        response.xpath('//*[@id="salesHistoryHeaderB"]/div[2]/b[1]').extract()[-1]
        )

        genre = (
        response.xpath('//*[@id="gameGenInfoBox"]/h2[4]/following-sibling::p').extract()[0]
        )

        critic_review = (
        response.xpath('//*[@id="gameReviewWrapper"]/span/a/text()').extract()
        )


        yield {
            'url': url,
            'name': name,
            'platform': platform,
            'critic_review': critic_review,
            # 'publisher': publisher,
            'ratings': ratings,
            'release_date': release_date,
            'total_sales': total_sales,
            'genre': genre
        }
