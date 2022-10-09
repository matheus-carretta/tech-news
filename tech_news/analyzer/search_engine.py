from tech_news.database import search_news


# Requisito 6
# based on: https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    news_by_title = []

    for content in news:
        news_by_title.append((content['title'], content['url']))

    return news_by_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
