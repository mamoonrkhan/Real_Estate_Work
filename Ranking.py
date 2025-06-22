def get_ranking(matching_listings): #Helper function to sort list
    while True: #Asks user which ranking value to use
        which_rank = input("Rank by (price, size, bedroom count, bathroom count): ").strip().lower()

        rank_key_map = { #Dictionary to map input to actual data keys
            'price': 'price',
            'size': 'size',
            'bedroom count': 'bedrooms',
            'bathroom count': 'bathrooms'
        }

        if which_rank in rank_key_map:
            break
        
        print("Please enter a valid ranking value.")

    while True: #Asks user if they would like to sort in ascending/descending order
        order = input("Sort from lowest to highest? (yes/no): ").strip().lower()
        if order in ['yes', 'no']:
            break
        print("Please state (yes/no): ")

    # Determine sort direction
    reverse = False if order == 'yes' else True
    
    #Get the actual key from the map
    rank_key = rank_key_map[which_rank]

    #Sort the listings based on value and return to main file
    sorted_list = sorted(matching_listings, key=lambda x: x[rank_key], reverse=reverse)
    return sorted_list