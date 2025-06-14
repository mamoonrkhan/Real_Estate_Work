#Library used to read CSV file
import pandas as pd

#Filters (i.e returning helper function values)
from Filtering import (get_location, get_maxprice, get_minprice, get_maxbedrooms,
get_minbedrooms, get_maxbathrooms, get_minbathrooms, get_maxsize, get_minsize)

#File reading
df = pd.read_csv('listings.csv')

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
    #Need to add

else:
    if 'location' in filters: #Apply location filter
        location = get_location()
        #Need to add

    if 'price' in filters:    #Apply price filter
        min_price = get_minprice()
        max_price = get_maxprice()
        #Need to add

    if 'bedroom count' in filters:   #Apply bedroom count filter
        min_bed = get_minbedrooms()
        max_bed = get_maxbedrooms()
        #Need to add

    if 'bathroom count' in filters:   #Apply bathroom count filter
        min_bath = get_minbathrooms()
        max_bath = get_maxbathrooms()
        #Need to add

    if 'property size' in filters:    #Apply property size filter
        min_size = get_minsize()
        max_size = get_maxsize()
        #Need to add

    # Output final results
    if df.empty:
        print("\n Sorry, no listings match your preferences.")
        #Need to add
    else:
        print("\n Yay! Matching Listings:\n") #
        # Suggest the best match (lowest price while accounting for filters)
        #Need to add

