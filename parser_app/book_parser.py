import requests
from bs4 import BeautifulSoup

URL = 'https://books.toscrape.com/catalogue/page-1.html'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


# 1. Get HTML
def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


# 2. Parse data
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    book_list = []
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        image_url = URL.rsplit('/', 1)[0] + '/' + book.find('img')['src']
        book_list.append({
            'title': title,
            'price': price,
            'availability': availability,
            'image': image_url,
        })
    return book_list


# 3. Parsing function
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        return get_data(response.text)
    raise Exception('Error while parsing')
