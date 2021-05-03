from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def scraped():
    scraps = []
    url = "https://www.pesapal.com/personal"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    rows = soup.find_all(class_= "col-12 col-md-6 col-xl-4 offset-xl-1 order-md-2 aos-init aos-animate")
    # print(rows)
    for r in rows:
        title=r.find('h3').text
        # print(title)
        scrap={
            
        }
        scraps.append(scrap)
    return scraps

def load_scraps(request):
    scraps = scraped()
    context = {
        'scraps': scraps
    }
    return render(request, 'index.html', context )
