from tech_news.database import search_news
from datetime import datetime


# Requisito 6
# based on: https://www.mongodb.com/community/
# forums/t/case-insensitive-search-with-regex/120598
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_by_title = []

    for content in news:
        news_by_title.append((content['title'], content['url']))

    return news_by_title


# Requisito 7
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    news = search_news({"timestamp": {"$regex": date}})
    news_by_date = []

    for content in news:
        news_by_date.append((content["title"], content["url"]))

    return news_by_date


# Requisito 8
def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news_by_tag = []

    for content in news:
        news_by_tag.append((content['title'], content['url']))

    return news_by_tag


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
