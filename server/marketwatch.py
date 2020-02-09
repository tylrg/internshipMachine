import requests
import article
from bs4 import BeautifulSoup

def marketwatch(comp_n, comp_t):
    articleList = []
    
    URL = 'https://www.marketwatch.com/trading-deck/stories'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('ol', class_='headlines block')
    if None is results:
        exit

    comp_name = comp_n
    comp_tick = comp_t

    article_elems = results.find_all('li')

    for article_elem in article_elems:
        if None is article_elem:
            continue

        URL = 'https://www.marketwatch.com' + article_elem.find('a')['href'].strip()
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        title_elem = article_elem.find('a', class_='bighead')

        results = soup.find(id='article-body')
        if None is results:
            continue
    
        para_elems = results.find_all('p')
        relevant_article = False
        if (comp_name or comp_tick) in title_elem.text.strip():
            relevant_article = True
        else:
            for para_elem in para_elems:
                if None is para_elem:
                    continue
                if (comp_name or comp_tick) in para_elem.text.strip():
                    relevant_article = True
                    continue
        if relevant_article:
            body_builder = ''
            for para_elem in para_elems:
                if None is para_elem:
                    continue
                body_builder += para_elem.text.strip() + ' '
            body_builder = ' '.join(body_builder.split())
            new_article = article.Article(title_elem.text.strip(), URL, body_builder.strip())
            articleList.append(new_article)
    
    for rev_article in articleList:
        print(rev_article, end='\n')
        print()

marketwatch('Facebook', 'FB')