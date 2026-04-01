from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
yc_news = response.text

soup = BeautifulSoup(yc_news,"html.parser")
articles = soup.find_all(class_="titleline",name="span a")
print(articles)
article_links = []
article_texts = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name = "span",class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)






