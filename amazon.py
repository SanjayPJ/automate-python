import requests, bs4, re, pprint

product_link = "https://www.amazon.in/NESROR-Brown-Analog-Watch-FX-480/dp/B07QGQD539/ref=sr_1_1_sspa?keywords=watches+for+men&qid=1563776847&s=gateway&sr=8-1-spons&psc=1"
res = requests.get(product_link);
links = re.findall(r'\/(?:dp)\/(?:product\/)?(\w{10})', res.text)

product_details = {}
for link in links:
    product_link = "https://www.amazon.in/dp/" + link
    res = requests.get(product_link);
    print(res.status_code)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#productTitle')
    try:
        product_title = elem[0].text.strip()
        elem = soup.select('#priceblock_ourprice')
        product_price = elem[0].text.strip()
        product_details[product_title] = product_price
    except:
        print('Soething went wrong!!!!')
pprint.pprint(product_details)
    
    
