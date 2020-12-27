"""
Author: Juan David Guerra
Project: Make a directory which maps people to their addresses, email, phone number, contact photo, relationship, etc.
Kind of like contacts in the iPhone
Will do this through the use of classes
"""

import doctest


class Person:
    """
    This class will create an object that will store the person's information
    This will include the address, phone number(s), email(s), relationship to that person, and more
    """

    def __init__(self, name, address, phone_number, list_email, relationship):
        """
        All base forms of the entries should be strings
        :param address: will be the address of the person. Type string
        :param phone_number: Will be the phone numbers
        of the person. input should be a list of tuples The first index of the tuple should be the type of number as
        a string (work, home, etc.) and second should be the number
        :param list_email: emails of the person: input should be a list of tuples where the type of email is first index
        and second index of tuple is the actual email
        :param relationship: Type string: relationship to that person
        """

        self.name = name  # creating the name variable
        self.address = address  # assigning the address attribute
        self.phone_number = {}  # creating the dictionary that will map phone numbers to their use (work, personal,
        # etc.)

        if phone_number is not None:
            for number in phone_number:
                self.phone_number[number[0]] = number[1]

        self.email = {}

        if list_email is not None:
            for email in list_email:
                self.email[email[0]] = email[1]

        self.relationship = relationship

    def __str__(self):
        return


