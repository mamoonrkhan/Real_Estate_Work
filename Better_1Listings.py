#Library used to read CSV file
import pandas as pd

#Filters (i.e returning helper function values)
from Better_Filtering import get_num_of_filter, get_good_location

#Ranking function
from Better_Ranking import get_good_ranking


#Class to store listing details with display and dict conversion
class Property:

    #Initializing property with details
    def __init__(self, address, city, price, bedrooms, bathrooms, size): 
        self.address = address
        self.city = city
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.size = size

    #To string
    def __str__(self):
        return (f"{self.address} in {self.city.title()} — ${self.price} — "
                f"{self.bedrooms} bed / {self.bathrooms} bath / {self.size} sqft")

    #Dictionary conversion
    def to_dict(self):
        return {
            'address': self.address,
            'city': self.city,
            'price': self.price,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'size': self.size
        }

    #Price per sqft function
    def price_per_sqft(self):
        if self.size > 0:
            return round(self.price / self.size, 2)
        return 0

#Class to manage filtering, displaying, and exporting property listings
class ListingManager:

    #Initializing
    def __init__(self, property_list):
        self.listings = property_list

    #Displaying purposes
    def display(self, listings=None):
        for prop in listings or self.listings:
            print(prop)

    #Filters listings based on provided criteria dict.
    def filter(self, criteria):
        matches = []
        for prop in self.listings:
            if 'city' in criteria and prop.city.lower() != criteria['city']:
                continue
            if 'min_price' in criteria and prop.price < criteria['min_price']:
                continue
            if 'max_price' in criteria and prop.price > criteria['max_price']:
                continue
            if 'min_bedrooms' in criteria and prop.bedrooms < criteria['min_bedrooms']:
                continue
            if 'max_bedrooms' in criteria and prop.bedrooms > criteria['max_bedrooms']:
                continue
            if 'min_bathrooms' in criteria and prop.bathrooms < criteria['min_bathrooms']:
                continue
            if 'max_bathrooms' in criteria and prop.bathrooms > criteria['max_bathrooms']:
                continue
            if 'min_size' in criteria and prop.size < criteria['min_size']:
                continue
            if 'max_size' in criteria and prop.size > criteria['max_size']:
                continue
            matches.append(prop)
        return matches

    def export(self, listings, filename):
        pd.DataFrame([p.to_dict() for p in listings]).to_csv(filename, index=False)
        print(f" Listings saved to '{filename}'")


#File reading
df = pd.read_csv('listings.csv')

#Reading all properties
properties = [Property(r['address'], r['city'], r['price'], r['bedrooms'], r['bathrooms'], r['sqft']) for _, r in df.iterrows()]

#Calling on listing manager class to organize properties
manager = ListingManager(properties)

#Basic introduction
print('''Hello! Welcome to the real estate browser.
We’ll ask a few quick questions to find your dream property!''')

#Asks user for filters
filters = input("List your filters (location, price, bedroom count, bathroom count, property size) or type 'no': ").lower().split(',')
filters = [f.strip() for f in filters]

#Creating list to store
criteria = {}

#Prints all listings if user doesn't care for filtering
if 'no' in filters:
    print("\n📋 All Listings:\n")
    manager.display()
    exit()

#Goes one by one to check all filters and omit listings
if 'location' in filters:
    criteria['city'] = get_good_location().lower()
if 'price' in filters:
    criteria['min_price'] = get_num_of_filter("minimum budget")
    criteria['max_price'] = get_num_of_filter("maximum budget")
if 'bedroom count' in filters:
    criteria['min_bedrooms'] = get_num_of_filter("minimum bedrooms")
    criteria['max_bedrooms'] = get_num_of_filter("maximum bedrooms")
if 'bathroom count' in filters:
    criteria['min_bathrooms'] = get_num_of_filter("minimum bathrooms")
    criteria['max_bathrooms'] = get_num_of_filter("maximum bathrooms")
if 'property size' in filters:
    criteria['min_size'] = get_num_of_filter("minimum size (sqft)")
    criteria['max_size'] = get_num_of_filter("maximum size (sqft)")

matches = manager.filter(criteria)

#Print if no listings match
if not matches:
    print("\n Sorry, no listings match your preferences.")
    exit()

#Print matching listings
print("\nMatching Listings:\n")
manager.display(matches)

#Asks users if they would like to rank by value point
if input("\nWould you like to rank these by price, size, bedroom count, or bathroom count? (yes/no): ").strip().lower() == 'yes':
    matches = get_good_ranking(matches)

#Print final, ranked, matching listings
print("\n Final Listings:\n")
manager.display(matches)

#Export to csv after displaying listings
manager.export(matches, 'matched_listings.csv')