import requests


NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"
NEWSAPI_KEY = "8866a102f5b64d809193265f2956ee38"

keywords = ""

def check_title():
    keywords = input("Enter keywords: ")

    news_parameters = {
        "apiKey": NEWSAPI_KEY,
        "qInTitle": keywords,
        "Language": "zh"
    }

    respond = requests.get(NEWSAPI_ENDPOINT, params=news_parameters)
    articles = respond.json()["articles"]

    print(articles)

    title_list = [article["title"] for article in articles]
    for title in title_list[:5]:
        print(title)



    if keywords == "exit":
        exit()


# while keywords == "":
check_title()

