def get_location(): #Function to call on for location purposes
    city = input ('''Which city are you looking for? (Brampton, Mississagua, or Toronto): ''').strip()
    return city

def get_maxprice(): #Function to call on for max price
    while True:
        try:
            maxbudg = int(input("What is your maximum budget? (numbers only): "))
            return maxbudg
        except ValueError:
            print ("Please enter a valid number.")

def get_minprice():  #Function to call on for min price
    while True:
        try:
            minbudg = int(input("What is your minumum budget? (numbers only): "))
            return minbudg
        except ValueError:
            print ("Please enter a valid number.")


def get_maxbedrooms():  #Function to call on for max bedrooms
    while True:
        try:
            maxbed = int(input("What is the maximum number of bedrooms you seek? (numbers only): "))
            return maxbed
        except ValueError:
            print ("Please enter a valid number.")


def get_minbedrooms():  #Function to call on for min bedrooms
    while True:
        try:
            minbed = int(input("What is the minimum number of bedrooms you seek? (numbers only): "))
            return minbed
        except ValueError:
            print ("Please enter a valid number.")


def get_maxbathrooms():  #Function to call on for max bathrooms
    while True:
        try:
            maxbath = int(input("What is the maximum number of bathrooms you seek? (numbers only): "))
            return maxbath
        except ValueError:
            print ("Please enter a valid number.")


def get_minbathrooms():  #Function to call on for min bathrooms
    while True:
        try:
            minbath = int(input("What is the minumum number of bathrooms you seek? (numbers only): "))
            return minbath
        except ValueError:
            print ("Please enter a valid number.")


def get_maxsize():   #Function to call on for max property size
    while True:
        try:
            maxsize = int(input("What is the maximum property size you seek? (numbers only): "))
            return maxsize
        except ValueError:
            print ("Please enter a valid number.")

def get_minsize():    #Function to call on for min property size
    while True:
        try:
            minsize = int(input("What is the minimum property size you seek? (numbers only): "))
            return minsize
        except ValueError:
            print ("Please enter a valid number.")
            