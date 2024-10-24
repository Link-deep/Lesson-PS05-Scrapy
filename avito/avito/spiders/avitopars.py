import scrapy


class AvitoparsSpider(scrapy.Spider):
    name = "avitopars"
    allowed_domains = ["www.avito.ru"]


    custom_settings = {
        'DOWNLOAD_DELAY': 0.5
    }

    def parse(self, response):
        h3 = response.css("h3")
        print(h3)
        print(f"Status code: {response.status}")

    def start_requests(self):

        url = f"https://www.avito.ru/tyumen/kvartiry/prodam/novostroyka-ASgBAgICAkSSA8YQ5geOUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAkSSA8YQ5geOUgFAyggkgFn~WA"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-control": "max-age=0",
            "Priority": "u=0, i",
            "Sec-Ch-Ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"

        }

        yield scrapy.Request(url=url, callback=self.parse, headers=headers)


