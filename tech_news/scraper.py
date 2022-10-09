import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"User-Agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
        time.sleep(1)
        return response.text
    except (requests.Timeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css('.entry-header h2 a::attr(href)').getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css('.next::attr(href)').get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news_info = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css('.entry-title::text').get().strip(),
        "timestamp": selector.css('.meta-date::text').get(),
        "writer": selector.css('.fn a::text').get().strip(),
        "comments_count": len(selector.css('#comments').getall()),
        "summary": "".join(selector.css(
            "div.entry-content > p:first-of-type *::text").getall()).strip(),
        "tags": selector.css('a[rel=tag]::text').getall(),
        "category": selector.css('.label::text').get()
    }
    return news_info


# Requisito 5
def get_tech_news(amount):
    baseURL = "https://blog.betrybe.com/"
    news = []

    while len(news) < amount:
        news_url = scrape_novidades(fetch(baseURL))
        for url in news_url:
            noticia_html = fetch(url)
            news_info = scrape_noticia(noticia_html)
            news.append(news_info)

            if len(news) == amount:
                break

        baseURL = scrape_next_page_link(fetch(baseURL))

    create_news(news)
    return news
