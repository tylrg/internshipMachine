import requests
import article
from bs4 import BeautifulSoup

def seekingalpha(comp_n, comp_t):
    articleList = []
    
    URL = 'https://seekingalpha.com/market-news'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='latest-news-list')
    if None is results:
        exit

    comp_name = comp_n
    comp_tick = comp_t

    article_elems = results.find_all('li', class_='item')

    for article_elem in article_elems:
        if None is article_elem:
            continue

        URL = 'https://seekingalpha.com' + article_elem.find('a')['href'].strip()
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        title_elem = article_elem.find('h4')

        results = soup.find(id='bullets_ul')
        if None is results:
            continue
    
        bullet_elems = results.find_all('p', class_='bullets_li')
        relevant_article = False
        if (comp_name or comp_tick) in title_elem.text.strip():
            relevant_article = True
        else:
            for bullet_elem in bullet_elems:
                if None is bullet_elem:
                    continue
                if (comp_name or comp_tick) in bullet_elem.text.strip():
                    relevant_article = True
                    continue
        if relevant_article:
            body_builder = ''
            for bullet_elem in bullet_elems:
                if None is bullet_elem:
                    continue    
                body_builder += bullet_elem.text.strip() + ' ' 
            new_article = article.Article(title_elem.text.strip(), URL, body_builder.strip())
            articleList.append(new_article)
    
    for rev_article in articleList:
        print(rev_article, end='\n')
        print()

seekingalpha('Facebook', 'FB')
