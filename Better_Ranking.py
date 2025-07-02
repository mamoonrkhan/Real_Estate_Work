def get_good_ranking(listings): #Helper function to sort list
    key_map = { #Dictionary to map input to actual data keys
        'price': 'price',
        'size': 'size',
        'bedroom count': 'bedrooms',
        'bathroom count': 'bathrooms'
    }

    while True: #Asks user which ranking value to use
        rank_by = input("Rank by (price, size, bedroom count, bathroom count): ").strip().lower()
        if rank_by in key_map:
            break
        print("Please enter a valid ranking option.")

    #Asks user if they would like to sort in ascending/descending order
    while True:
        order = input("Sort in ascending or descending order? (ascending/descending): ").strip().lower()
        if order in ['ascending', 'descending']:
            break
        print("Please enter 'ascending' or 'descending'.")

    reverse = (order == 'descending')  # Determine sort direction
    attr = key_map[rank_by]

    #Sort the listings based on value and return to main file
    return sorted(listings, key=lambda x: getattr(x, attr), reverse=reverse)