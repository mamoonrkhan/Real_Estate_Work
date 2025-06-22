#Library used to read CSV file
import pandas as pd

#Filters (i.e returning helper function values)
from Filtering import (get_location, get_maxprice, get_minprice, get_maxbedrooms,
get_minbedrooms, get_maxbathrooms, get_minbathrooms, get_maxsize, get_minsize)

from Ranking import (get_ranking)

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

criteria = {} #Holds user input/filters

#Print all properties if user does not provide filters
if 'no' in filters:
    print("\n📋 All Listings:\n")
    for listing in listings:
        print(f"{listing['address']} in {listing['city']} — ${listing['price']} — "
              f"{listing['bedrooms']} bed / {listing['bathrooms']} bath / {listing['sqft']} sqft")

else:
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
        criteria ['min_bathrooms'] = get_minbathrooms()

    if 'property size' in filters:    #Apply property size filter
        criteria ['max_size'] = get_maxsize()
        criteria ['min_size'] = get_minsize()

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

    if 'min_price' in criteria and listing ['price'] < criteria ['min_price']:
        matched = False

    #Check bedrooms
    if 'max_bedrooms' in criteria and listing['bedrooms'] > criteria['max_bedrooms']:
            matched = False
    if 'min_bedrooms' in criteria and listing['bedrooms'] < criteria['min_bedrooms']:
            matched = False

    #Check bathrooms
    if 'max_bathrooms' in criteria and listing['bathrooms'] > criteria['max_bathrooms']:
            matched = False
    if 'min_bathrooms' in criteria and listing['bathrooms'] < criteria['min_bathrooms']:
            matched = False

    #Check property size
    if 'max_size' in criteria and listing['size'] > criteria['max_size']:
            matched = False
    if 'min_size' in criteria and listing['size'] < criteria['min_size']:
            matched = False

    #Condition if there are matches
    if matched:
        matching_listings.append(listing)


# Output final results
if not matching_listings: #Simple print if there are no matching listings
    print ("Sorry, there are no listings that match your preferences.")

else:
    print("\nMatching Listings:\n") #Full print for matches using manual loop after filtering
    for listing in matching_listings:
            print(f"{listing['address']} in {listing['city'].title()} — ${listing['price']} — "
                  f"{listing['bedrooms']} bed / {listing['bathrooms']} bath / {listing['sqft']} sqft")
    
    while True: #Asks user if they would like to rank
        rank = input('''\nWould you also like to rank these listings based on a value point
                (price, size, bedroom count, bathroom count), please say yes or no: ''').strip().lower()
        if rank in ['yes', 'no']:
             break
        print ("Please state (yes/no): ")

    if rank == 'yes': #Uses helper function to properly sort the listings
        ranked_list = get_ranking(matching_listings)
    else:
        ranked_list_list = matching_listings


    # Print sorted list
    print("\n Final Listings:\n")
    for l in ranked_list:
        print(f"{l['address']} in {l['city'].title()} — ${l['price']} — "
            f"{l['bedrooms']} bed / {l['bathrooms']} bath / {l['sqft']} sqft")

    #Export to CSV file
    pd.DataFrame(ranked_list).to_csv('matched_listings.csv', index=False)
    print("Listings saved to 'matched_listings.csv'")