
from datetime import datetime


class Contact:
    """A class to store properties for a single contact."""

    def __init__(self, first_name, last_name, phone_num, dob: datetime = None, email=None):
        """Initialize properties."""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.dob = dob
        self.email = email

    @property
    def full_name(self):
        """Get the full name of the contact, from first and last names."""
        return f"{self.first_name} {self.last_name}"

    def edit(self, first_name=None, last_name=None, phone_num=None, dob: datetime = None, email=None):
        """Update contact properties."""
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone_num:
            self.phone_num = phone_num
        if dob:
            self.dob = dob
        if email:
            self.email = email

    def __str__(self):
        """Return a multiline string with info about the contact."""
        return f"Name: {self.full_name}\nPhone Number: {self.phone_num}\nDOB: {self.dob}\nEmail Address: {self.email}"

    def __repr__(self):
        """Return a class instance representation of the contact."""
        return f"Contact('{self.first_name}', '{self.last_name}', '{self.phone_num}', '{self.dob}', '{self.email}')"
