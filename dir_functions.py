from contact import Contact
from datetime import datetime
import json
from os import name


def load_dir():
    # Loads the directory.json file into the memory, converts into a list of Contact objects, and returns the list."""
    with open("directory.json", "r") as f:
        directory = []
        for cont_dict in json.load(f):
            cont_obj = Contact(cont_dict["first_name"], cont_dict["last_name"],
                               cont_dict["phone_num"], datetime.strptime(cont_dict["dob"], "%Y-%m-%d") if cont_dict["dob"] else None, cont_dict["email"])
            directory.append(cont_obj)
    return directory


def save_dir(directory):
    # Converts the directory loaded in memory to a JSON list, and saves the list to the directory.json file
    directory_json = []
    for contact in directory:
        contact_dict = contact.__dict__
        if contact_dict["dob"]:
            contact_dict["dob"] = datetime.strftime(
                contact_dict["dob"], "%Y-%m-%d")
        directory_json.append(contact_dict)

    with open("directory.json", "w") as f:
        f.write(json.dumps(directory_json))


def create_contact():
    # Takes several inputs from the user and returns a Contact object based on the inputs.
    while not (first_name := input("Enter first name: ")):
        print("First name is compulsory!")
    while not (last_name := input("Enter last name: ")):
        print("Last name is copulsory!")
    while not (phone_num := input("Enter phone number: ")):
        print("Phone number is compulsory!")
    while True:
        try:
            dob = input("Enter date of birth (yyyy-mm-dd): ")
            if dob:
                dob = datetime.strptime(dob, "%Y-%m-%d")
            else:
                dob = None
        except ValueError:
            print("Invalid format!")
        else:
            break
    if not (email := input("Enter email address: ")):
        email = None
    return Contact(first_name, last_name, phone_num, dob, email)


def display_all(directory):
    for contact in directory:
        print(contact.full_name)


def json_sorter(file_contents):
    for i in range(1, len(file_contents)):
        curitem = (file_contents[i])
        j = i-1
        while j >= 0 and ((curitem["first_name"]+curitem["last_name"]).lower()) < ((file_contents[j]["first_name"]+file_contents[j]["last_name"]).lower()):
            file_contents[j+1] = file_contents[j]
            j -= 1
        file_contents[j+1] = curitem
    # return file_contents using Insertion Sort


def binary_search(file_contents, search_item, search_item_type):
    low = 0
    high = len(file_contents)-1
    mid = 0
    found = False
    if search_item_type == "name":
        while low <= high:
            mid = (high+low)//2
            full_name = file_contents[mid]["first_name"] + \
                file_contents[mid]["last_name"]
            full_name = full_name.lower()
            if search_item in full_name:
                print(file_contents[mid])
                found = True
            if full_name < search_item:
                low = mid + 1
            if full_name > search_item:
                high = mid - 1
    if search_item_type == "num":
        while low <= high:
            mid = (high+low)//2
            number = file_contents[mid]["phone_num"]
            if search_item in number:
                print(file_contents[mid])
                found = True
            if number < search_item:
                low = mid + 1
            if number > search_item:
                high = mid - 1
    return found


def search_by_name():
    fp = open("directory.json", "r")
    file_contents = fp.read()
    file_contents = json.loads(file_contents)
    json_sorter(file_contents)
    name_to_search = str(input("Enter name to search"))
    name_to_search = name_to_search.lower()
    found = False
    found = binary_search(file_contents, name_to_search, "name")
    if found == False:
        print("No matches")


def search_by_num():
    fp = open("directory.json", "r")
    file_contents = fp.read()
    file_contents = json.loads(file_contents)
    json_sorter(file_contents)
    num_to_search = str(input("Enter num to search"))
    found = False
    for i in file_contents:
        num = i["phone_num"]
        if num_to_search in num:
            print(i)
            found = True
    if found == False:
        print("No matches")


def delete_contact(directory, x):
    for i in directory:
        if x in (i.full_name).lower():
            print('\n', directory.index(i) + 1, ':', '\n', i, '\n')

    s = int(input('Enter contact number you want to delete: '))

    for i in directory:
        if x in (i.full_name).lower():
            directory.pop(s - 1)

    print('\n', 'Remaining contacts: ' + '\n')

    for i in directory:
        print(directory.index(i) + 1, ':', '\n', i, '\n')


def delete_all(directory):
    directory.clear()
    return directory


json_sorter(
    [
        {
            "first_name": "John",
            "last_name": "Doe",
            "phone_num": "031212392",
            "dob": "2004-09-14",
            "email": None
        },
        {
            "first_name": "Chris",
            "last_name": "Evans",
            "phone_num": "031212392",
            "dob": None,
            "email": "chris@gmail.com"
        },
        {
            "first_name": "Charles",
            "last_name": "Evans",
            "phone_num": "031212392",
            "dob": None,
            "email": "chris@gmail.com"
        },
        {
            "first_name": "Boyles",
            "last_name": "Evans",
            "phone_num": "031212392",
            "dob": None,
            "email": "chris@gmail.com"
        },
        {
            "first_name": "Christina",
            "last_name": "Thomas",
            "phone_num": "023340756332",
            "dob": "2002-02-21",
            "email": "Christinathomas@mail.com"
        }
    ]
)
