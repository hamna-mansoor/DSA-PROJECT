import dir_functions as df

# Load the directory from directory.json as a list of Contact objects.
directory = df.load_dir()

# Start output
print("CONTACTS DIRECTORY")

while True:
    print("==================")
    print("1. View directory")
    print("2. Create a new contact")
    print("3. Search for a contact by name")
    print("4. Search for a contact by phone number")
    print("5. Remove contact from directory")
    print("6. Delete all contacts")

    choice = input("Enter (1/2/3/4/5/6) or 'q' to quit: ")

    # Validate input
    while choice not in ["1", "2", "3", "4", "5", "6", "q"]:
        choice = input("Invalid input! Please enter (1/2/3/4/5/6) or 'q': ")

    # Save and exit program if "q" is entered
    if choice == "q":
        df.save_dir(directory)
        break

    # Print the complete directory if "1" is entered
    if choice == "1":
        df.display_all(directory)

    # Create a new contact and add it to the directory if "2" is entered
    if choice == "2":
        new_contact = df.create_contact()
        directory.append(new_contact)

    # Search for a contact by name if "3" is entered
    if choice == "3":
        df.search_by_name()

    # Search for a contact by number if "4" is entered
    if choice == "4":
        df.search_by_num()

    # Search for a contact and remove it from directory if "5" is entered
    if choice == "5":
        full__name = input(
            '\n' + 'Enter full name of contact you want to delete: ')
        df.delete_contact(directory, full__name)

    # Delete all contacts if "6" is entered
    if choice == "6":
        df.delete_all(directory)
