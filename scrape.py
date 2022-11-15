from bs4 import BeautifulSoup
import requests
from csv import writer

#remax website with rela estate data
url = "https://www.remax.ca/on/ontario-real-estate?pageNumber=1"

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')


#finding a list of all listing cards to iterate through
lists = soup.find_all('div',class_="listing-card_root__UG576 search-gallery_galleryCardRoot__7HbLb")


#writes to a csv file to be created in the same folder
with open('RealsEstateinfo.csv','w', encoding='utf8', newline= '') as f:

    thewriter = writer(f)

    header = ['title', 'address', 'mls', 'bed']

    thewriter.writerow(header)


    # for each listing we are finding the price address mls number and bedrooms for each house and creating a column for each
    for listing in lists:

        price = listing.find('h2',class_="listing-card_price__sL9TT").text
            
        addy = listing.find('div', class_="listing-address_root__PP_Ky listing-card_address___bLLz").text

        mls = listing.find('div',class_="listing-card_mlsNumber__6KRDy").text

        bed = listing.find_all('span',class_="property-details_detailSpan__E4NRz listing-card_propertyDetail__3OOL0")
        
        for beds in bed:
            
            rrr = beds.find('span',class_="").text
            
            data = [price, addy, mls, rrr]

            thewriter.writerow(data)
            
            
            
        
        
     
        
    
     #one struggle for this side project was fidning the bed and baths value as there is no fucntionality to get tags with no class
    
    

