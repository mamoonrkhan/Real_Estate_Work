def get_good_location(): #Function to call on for location purposes
    return input("Which city are you looking for? (Brampton, Mississauga, or Toronto): ").strip()

def get_num_of_filter(prompt): #Function to call on for other numeric inputs
    while True:
        try:
            return int(input(f"What is your {prompt}? (numbers only): ")) #Prompt lists all numerical inputs
        except ValueError:
            print("Please enter a valid number.")