import requests
from bs4 import BeautifulSoup
import pprint


page = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select('.titleline > a')
subtext = soup.select('.subtext')


def sort_stories_by_votes(content_list):
    return sorted(content_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hacker_news = []

    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href')
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hacker_news.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hacker_news)


pprint.pprint(create_custom_hacker_news(links, subtext))
