from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def scraped():
    scraps = []
    url = "[url here]"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    rows = soup.find_all(class_= "")
    # print(rows)
    for r in rows:
        title=r.find('h3').text
        # print(title)
        scrap={
            'title': title,
        }
        scraps.append(scrap)
    return scraps

def load_scraps(request):
    scraps = scraped()
    context = {
        'scraps': scraps,
    }
    return render(request, 'index.html', context)
