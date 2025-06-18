#Library used to read CSV file
import pandas as pd

#Filters (i.e returning helper function values)
from Filtering import (get_location, get_maxprice, get_minprice, get_maxbedrooms,
get_minbedrooms, get_maxbathrooms, get_minbathrooms, get_maxsize, get_minsize)

#File reading
df = pd.read_csv('listings.csv')

#Converting df to a list (row dict.)
listings = df.to_dict(orient = 'records')

#Basic introduction
print ('''Hello and welcome to the real estate listing browser!
Here, we ask you a few, simple questions and we can match you with your dream property, free of charge!
Are you ready? Well, let's begin!''')

#Asking user for filters/requests or declining to do so
filters = input('''Do you have any specific requirements/preferences?
If so, please type the filter(s) you wish to set or state (no).
Filters available are: Location, Price, Bedroom Count, Bathroom Count, Property Size: ''').lower().split(',')

#Omitting unnecessary spaces
filters = [f.strip() for f in filters]

#Print all properties if user does not provide filters
if 'no' in filters:
    print("\n📋 All Listings:\n")
    for listing in listings:
        print(f"{listing['address']} in {listing['city']} — ${listing['price']} — "
              f"{listing['bedrooms']} bed / {listing['bathrooms']} bath / {listing['size']} sqft")

else:

    criteria = {} #Holds user input/filters

    if 'location' in filters: #Apply location filter
        criteria ['city'] = get_location().lower()


    if 'price' in filters:    #Apply price filter
        criteria ['max_price'] = get_maxprice()
        criteria ['min_price'] = get_minprice()
        

    if 'bedroom count' in filters:   #Apply bedroom count filter
        criteria ['max_bedrooms'] = get_maxbedrooms()
        criteria ['min_bedrooms'] = get_minbedrooms()
        

    if 'bathroom count' in filters:   #Apply bathroom count filter
        criteria ['max_bathrooms'] = get_maxbathrooms()
        criteria ['min_bathrooms'] = get_minbathrooms

    if 'property size' in filters:    #Apply property size filter
        criteria ['max_size'] = get_maxsize()
        criteria ['max_size'] = get_minsize()

#Listings will be manually filtered using this list
matching_listings = [] 

for listing in listings: #Loops through to find all matches, and omits them if they are
    matched = True #Assumes true unless shown otherwise

    #Check location
    if 'city' in criteria and listing ['city'].strip().lower() != criteria['city']:
        matched = False

    #Check price
    if 'max_price' in criteria and listing ['price'] > criteria ['max_price']:
        matched = False

    if 'min_price' in criteria and listing ['bedrooms'] < criteria ['min_price']:
        matched = False

    #Check bedrooms
    if 'max_bedrooms' in criteria and listing['bedrooms'] > criteria['max_bedrooms']:
            match = False
    if 'min_bedrooms' in criteria and listing['bedrooms'] < criteria['min_bedrooms']:
            match = False

    #Check bathrooms
    if 'max_bathrooms' in criteria and listing['bathrooms'] > criteria['max_bathrooms']:
            match = False
    if 'min_bathrooms' in criteria and listing['bathrooms'] < criteria['min_bathrooms']:
            match = False

    #Check property size
    if 'max_size' in criteria and listing['size'] > criteria['max_size']:
            match = False
    if 'min_size' in criteria and listing['size'] < criteria['min_size']:
            match = False

    #Condition if there are matches
    if matched:
        matching_listings.append(listing)


# Output final results
if not matching_listings: #Simple print if there are no matching listings
    print ("Sorry, there are no listings that match your preferences.")

else:
    print("\n Matching Listings:\n") #Full print for matches using manual loop after filtering
    for listing in matching_listings:
            print(f"{listing['address']} in {listing['city'].title()} — ${listing['price']} — "
                  f"{listing['bedrooms']} bed / {listing['bathrooms']} bath / {listing['sqft']} sqft")
