Our directory will be stored as a JSON list of dictionaries, in the
directory.json file, like this:
[
    {
        "first_name": "John",
        "last_name": "Doe",
        "phone_num": "031212392",
        "dob": "2004-09-14",
        "email": null
    },
    {
        "first_name": "Chris",
        "last_name": "Evans",
        "phone_num": "031212392",
        "dob": null,
        "email": "chris@gmail.com"
    }
]

However, in the program memory, our directory will be stored as a list
of Contact objects, like this:
[
    Contact(
        "John", "Doe", "031212392", datetime(2004, 09, 14), None
    ),
    Contact(
        "Chris", "Evans", "031212392", None, "chris@gmail.com"
    )
]

Implemented the following:

- Class Contact which represents a single contact and stores the compulsory
  first name, last name, and phone number properties, and the optional date-
  of-birth, and email properties.

  - Contact.full_name returns a concatenated string of the first and last names.
  - Contact.edit updates the contact's properties by taking in keyword arguments
    for the new properties.

- Function load_dir() which parses the directory.json file and returns
  it as a list of Contact objects.

- Function save_dir(directory) which takes in the directory stored in
  memory as an argument, converts it into a JSON list of dictionaries, and
  saves it to the directory.json file.

- Function create_contact() which takes inputs from the user and creates
  and returns a Contact object based on the input.

- Function display_all() which prints the full names of all contacts in the
  directory to the console.

- Function json_sorter(file_contents) which reads the directory.json file,
  sorts it using Insertion Sort, and returns the sorted list.

- Function binary_search(file_contents, search_item, search_item_type) which
  searches for the given search_item which is of the given search_item_type.

- Function search_by_name() which prompts the user for the name to search and
  returns all found matches.

- Function search_by_num() which prompts the user for the number to search and
  returns all found matches.

- Function delete_contact() which deletes the given contact from the directory.

- Function delete_all() which removes all contacts from the directory