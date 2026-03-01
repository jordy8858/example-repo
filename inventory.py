'''
make a program that will read from the txt file inventory.txt
inside the file will be class names shoe with the following attributes:
(country, code, product, cost, quantity)
inside the class define the following methods:
- get_cost() - returns the cost of the shoe
- get_quantity() - returns the quantity of the shoe
__str__ method - returns a string representation of the shoe
defuine the follwoing fuctions outside the class:
- read_shoes_data() - reads the data from inventory.txt and creates a list of shoe objects
- capture_shoes() - allows the user to capture data about a shoe and append it to the inventory.txt file
- view_all() - displays all the shoes in the inventory
- re_stock() - finds the shoe with the lowest quantity and asks the user if they want to restock it
- search_shoe() - allows the user to search for a shoe by its code and displays its details
- value_per_item() - calculates the total value of each shoe in the inventory (cost * quantity) and displays it
- highest_qty() - finds the shoe with the highest quantity and displays its details
create a main menu that allows the user to select one of the functions above or exit the program
'''
with open('inventory.txt', 'r+') as file: #the shoe file

    class Shoe:
        def __init__(self, country, code, product, cost, quantity):
            self.country = country
            self.code = code
            self.product = product
            self.cost = cost
            self.quantity = quantity #defined the Shoe class witht the Attributes

        def get_cost(self): #first Method to return the cost of the shoe
            return self.cost

        def get_quantity(self): #second method to return the quantity of the shoe
            return self.quantity

        def __str__(self):
            return f"Shoe({self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity})" #string representation of the shoe


def read_shoes_data(): #define the function the read the shoe data outside the class
    shoe_list = []
    try:
        with open('inventory.txt', 'r') as file:
            for line in file:
                stripped_line = line.strip() #romove any leading/trailing whitespace
                if stripped_line == "Country,Code,Product,Cost,Quantity": 
                    continue

                parts = stripped_line.split(',') #split the line into parts based on the comma delimiter
                if len(parts) != 5: #check if the line has exactly 5 parts (country, code, product, cost, quantity)
                    print(f"Warning: Skipping malformed line '{stripped_line}' (expected 5 parts, found {len(parts)}).") #kept having Errors with this upon testing the code so added this line
                    continue

                try:
                    country, code, product, cost_str, quantity_str = parts #unpack the parts into variables
                    shoe = Shoe(country, code, product, float(cost_str), int(quantity_str))
                    shoe_list.append(shoe)
                except ValueError:
                    print(f"Warning: Could not parse numeric values in line '{stripped_line}'. Skipping.")
                    continue
    except FileNotFoundError:
        print("inventory.txt not found. Starting with an empty inventory.")
    return shoe_list #return the list of shoe objects created from the data in the inventory.txt file


def capture_shoes(): #define the function to capture shoe data from the user and append it to the inventory.txt file
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: ")) #gather all the shoe data from the user
    shoe = Shoe(country, code, product, cost, quantity) #create a new shoe object with the data provided by the user
    with open('inventory.txt', 'a') as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}\n") #make sure the new shoe data is appended on a new line
    print("Shoe captured successfully!")


def view_all(): #self explanatory function to view all the shoes in the inventory
    shoe_list = read_shoes_data()
    for shoe in shoe_list:
        print(shoe)


def re_stock(): #define the function to restock the shoe with the lowest quantity
    shoe_list = read_shoes_data()
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity()) #used the min lambda function to find the shoe with the lowest quantity
    print(f"Shoe with the lowest quantity: {lowest_quantity_shoe}")
    restock = input("Do you want to restock this shoe? (yes/no): ") #ask the user if they want to restock the shoe with the lowest quantity
    if restock.lower() == 'yes':
        try:
            additional_quantity = int(input("Enter the additional quantity: ")) #ask the user for the additional quantity to restock
            if additional_quantity<=0:
                print("Quantity must be a positive number.")
                return
        except ValueError: #handle the case where the user enters a non-integer value for the additional quantity
            print("Invalid input. Please enter a positive number.")
            return
        lowest_quantity_shoe.quantity += additional_quantity
        with open('inventory.txt', 'w') as file:
            file.write("\nCountry,Code,Product,Cost,Quantity\n") 
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n") #rewrite the inventory.txt file with the updated shoe quantities after restocking
        print("Shoe restocked successfully!")


def search_shoe(): #define the function to search for a shoe by its code and display its details
    shoe_list = read_shoes_data()
    code = input("Enter the shoe code to search: ") #ask the user for the shoe code they want to search for
    for shoe in shoe_list:
        if shoe.code == code: #search through the shoe list to find a shoe with a matching code
            print(shoe)
            return
    print("Shoe not found!") 


def value_per_item(): #define the function to calculate the total value of each shoe in the inventory
    shoe_list = read_shoes_data()
    if not shoe_list:
        print("No shoes in inventory.")
        return
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity() #calculate the total value of each shoe by multiplying its cost by its quantity
        print(f"{shoe.product}: Total Value = {value}")


def highest_qty():
    shoe_list = read_shoes_data()
    if not shoe_list:
        print("No shoes in inventory.")
        return
    highest_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity()) #used the max lambda function to find the shoe with the highest quantity
    print(f"Shoe with the highest quantity: {highest_quantity_shoe}")


def main_menu(): #define the main menu function to display the menu options and handle user input
    while True:
        print("\nMain Menu:")
        print("1. View all shoes")
        print("2. Capture a shoe")
        print("3. Restock a shoe")
        print("4. Search for a shoe")
        print("5. Calculate value per item")
        print("6. Find shoe with highest quantity")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Exiting the program.") #make a way for the user to exit the program from the main menu
            break
        else:
            print("Invalid choice. Please try again.") #handle the case where the user enters an invalid menu option

main_menu()
