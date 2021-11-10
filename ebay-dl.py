import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_itemssold(text):
    '''
    Takes string input an returns numver items sold
    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_shipping(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if numbers:
        return int(numbers)
    else:
        return 0

def parse_itemsprice(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if numbers:
        return int(numbers)
    else:
        return 0

        

#code after within the if statement doesnt run when doctest is being run
if __name__ == '__main__':

    #get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON') #this initialises it, telling python you will get information from the command line
    parser.add_argument('search_term') 
    parser.add_argument('--num_pages', default = 10) 
    args = parser.parse_args()
    print('args.search_term =', args.search_term)

    #list of all items found in all ebay webpages run through
    items = []

    #loop over the ebay webpages
    for page_number in range(1,int(args.num_pages)+1):
        #build the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + args.search_term + '&_sacat=0&_pgn=' + str(page_number) 
        print('url =', url)

        #dowload the html
        r = requests.get(url)
        status = r.status_code
        print('status', status)
        html = r.text

        #process the html
        soup = BeautifulSoup(html, 'html.parser')
        
        #loop over the items in the pagee
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:

            #extract the name
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            #extract the freereturns
            freereturns = False
            tag_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tag_freereturns:
                freereturns = True

            #extract itemssold
            itemssold = None
            tags_itemssold = tag_item.select('.s-item__hotness, .s-item__additionalItemHotness')
            for tag in tags_itemssold:
                itemssold = parse_itemssold(tag.text)
                

            #extract the status
            status = None
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text

            #extract the shipping
            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)

            #extract the price
            itemsprice = None
            tags_itemsprice = tag_item.select('.s-item__price')
            for tag in tags_itemsprice:
                itemsprice = parse_itemsprice(tag.text)
                
            item = {
                'name' : name,
                'free_returns' : freereturns,
                'itemssold' : itemssold,
                'status' : status,
                'shipping' : shipping,
                'price' : itemsprice
            }  
            items.append(item)   

    #write the json to a file
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))
