# Ebay Scraping

## What the file does
The ebay-dl.py file included in this repository scrapes ebay for any search terms entered by the user. The program creates a url using the search term and then downloads the number of pages of that item entered by the user. It then outputs a .json file with a dictionary that includes extracted data on the name of the items listed, how many have been sold, their status, the price, shipping costs, and whether they have free returns. 

## How to run the file
To scrape data for the first 10 pages of ebay for your chosen search term use the command below:
```  
$ python3 ebay-dl.py 'search_term' 
```  
To choose the number of pages you want to search use the command below, where x is the number of pages:
```  
$ python3 ebay-dl.py 'search_term' --num_pages=x
``` 
To generate the three .json files included in this repository (axe.json, hammer.json, barbed wire.json) use the following commands:
```  
$ python3 ebay-dl.py 'axe' --num_pages=10
``` 
```  
$ python3 ebay-dl.py 'hammer' --num_pages=10
``` 
```  
$ python3 ebay-dl.py 'barbed wire' --num_pages=10
``` 
[Course Project](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)
