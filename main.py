import re

class Contact:
    def __init__(self):
        # Assign empty array
        self.contacts = []
    
    # Define display_contacts() function to display all of contacts which user added
    def display_contacts(self):
        # Check if contacts are empty
        if len(self.contacts) == 0:
            print("\nSorry, there is no contact to display!")
            return False
        
        print("Contact list:")
        # For loop that iterates over self.contacts list and prints each item
        for contact in self.contacts:
            # Access objects of array item
            print(f"   (*) Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}")
    
    # Define add_contact() function to add the contact to the list
    def add_contact(self):
        # Take input from user
        name = input("\nEnter contact name: \n")
        email = input("Enter contact email: \n")
        number = input("Enter contact number: \n")
        
        # Global variable for using the variable in all of functions
        global regex
        # Assign regular expression for check email address
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Empty check for name, email, and number field
        if not name or not email or not number:
            print("Sorry, field cannot be left blank!")
            return False
        
        # Check valid email address
        if(not re.fullmatch(regex, email)):
            print("Please enter valid email address!")
            return False
        
        # Append contact to the list array
        self.contacts.append({'name': name, 'email': email, 'number': number})
        print("\nContact added!")
    
    # Define edit_contact() function to update the contact which user added
    def edit_contact(self):
        # Check if contacts are empty
        if len(self.contacts) == 0:
            print("\nSorry, there is no contact to display!")
            return False
        
        print("List of all contacts:")
        # For loop that iterates over self.contacts list and prints each item
        # Enumerate index of the array of items
        for idx, contact in enumerate(self.contacts):
            # Access objects of array item
            print(f"   ({idx}) Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}")
        
        # Take input from user
        index = int(input("\nEnter index to update: "))
        
        # Empty check for index
        # The array of items start with 0 and 0 means false that's because check this way
        if index == 0 or index > 0:
            # Take input from user
            name = input("\nEnter contact name: \n")
            email = input("Enter contact email: \n")
            number = input("Enter contact number: \n")
            
            # Empty check for name, email, and number field
            if not name or not email or not number:
                print("Sorry, field cannot be left blank!")
                return False

            # Check valid email address
            if(not re.fullmatch(regex, email)):
                print("Please enter valid email address!")
                return False
            
            # Update contact information by array index
            self.contacts[index]['name'] = name
            self.contacts[index]['email'] = email
            self.contacts[index]['number'] = number
            
            print("\nContact updated!")
    
    # Define remove_contact() function to delete the contact which user added
    def remove_contact(self):
        # Check if contacts are empty
        if len(self.contacts) == 0:
            print("\nSorry, there is no contact to display!")
            return False
        
        print("List of all contacts:")
        # For loop that iterates over self.contacts list and prints each item
        # Enumerate index of the array of items
        for idx, contact in enumerate(self.contacts):
            # Access objects of array item
            print(f"   ({idx}) Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}")
        
        # Take input from user
        choice = int(input("\nEnter index to delete: "))
        # Remove contact from list of contacts
        self.contacts.remove(self.contacts[choice])
        
        print("\nContact removed!")
    
    # Define search_contacts() function for search item in existing contacts
    def search_contacts(self):
        # Take input from user
        name = input("\nEnter contact name: \n")
        # Filtered items by name of the contacts
        filtered_items = list(filter(lambda item: item['name'] == name, self.contacts))
        
        # Check if contacts are empty
        if len(filtered_items) == 0:
            print("\nSorry, there is no contact to display!")
            return False
        
        print("\nSearch results:")
        # For loop that iterates over self.contacts list and prints each item
        for item in filtered_items:
            # Access objects of array item
            print(f"   (*) Name: {item['name']}, Email: {item['email']}, Number: {item['number']}")

if __name__ == "__main__":
    # Create Contact() class object
    contact = Contact()
    
    # Infinite loop for get inputs from the user
    while True: 
        # Define choice_array variable as a list of strings
        choice_array = ['Contact list', 'Add contact', 'Edit contact', 'Remove contact', 'Search contacts', 'Exit application']
        
        print("\nList of all choices:")
        # For loop that iterates over choice_array list and prints each string item
        # Enumerate index of the array of items
        for idx, item in enumerate(choice_array):
            print(f"   ({idx + 1}) {item}")
        
        # Try exception for handling error
        try:
            # Take input from user
            # Convert string to number
            choice = int(input("\nEnter your choice: "))

            # If user types 1, run the display_contacts() function
            if choice == 1:
                contact.display_contacts()
            # If user types 2, run the add_contact() function
            elif choice == 2:
                contact.add_contact()
            # If user types 3, run the edit_contact() function
            elif choice == 3:
                contact.edit_contact()
            # If user types 4, run the remove_contact() function
            elif choice == 4:
                contact.remove_contact()
            # If user types 5, run the search_contacts() function
            elif choice == 5:
                contact.search_contacts()
            # If user types 6, then exit() the program
            elif choice == 6:
                exit()
        # Catch the invalid value type error
        except ValueError:
            print("\nYou typed invalid value!")
        # If anything wrong in the program
        except: 
            print("\nSomething went wrong!")