"""
Author: Juan David Guerra
Project: Make a directory which maps people to their addresses, email, phone number, contact photo, relationship, etc.
Kind of like contacts in the iPhone
Will do this through the use of classes
"""


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

        # assuming a phone number was input, add it to the dictionary of phone numbers
        if phone_number is not None:
            for number in phone_number:
                self.phone_number[number[0]] = number[1]

        # creating the email dictionary
        self.email = {}

        # doing the same as in the phone_number dictionary, creating the dictionary of emails
        if list_email is not None:
            for email in list_email:
                self.email[email[0]] = email[1]

        # assigning the relationship attribute
        self.relationship = relationship

    def __str__(self):
        """
        Overloading the str cast to return what I want: the info of the person
        :return: returns the information of the given person
        """
        return self.name + '\n' + 'Address: ' + self.address + '\n' + 'Phone numbers: ' \
               + str(self.phone_number) + '\n' + 'Emails: ' + str(self.email) + '\n' + \
               'Relationship: ' + self.relationship

    def add_phone_number(self, phone_number):
        """
        (list) --> String
        :param phone_number: Type list - adds a phone number to the person
        :return: the dictionary of phone numbers
        """

        # checking if the type of phone number already exists in the dictionary
        # example: personal is already in the phone number dictionary
        # if so, ensure that the user wants to change the type of number
        if phone_number[0] in self.phone_number:

            print("This number type is already registered...")
            print("Would you like to replace the number")

            # creating the variable that will hold the choice type
            replace_choice = input("YES or NO: ").upper()

            # ensuring that the type of input is correct
            while replace_choice != "YES" and replace_choice != "NO":
                print('Unsupported input. Try again with Yes or No')

                # retrying the input
                replace_choice = input("YES or NO: ")

                replace_choice = replace_choice.upper()

            # if the user wants to change, then change the phone number
            if replace_choice == 'YES':

                print('Changing the phone number')
                # changing the value of the desired number to the new number
                self.phone_number[phone_number[0]] = phone_number[1]
                print('New numbers are: ' + str(self.phone_number))
                return self.phone_number

            # if user does not want to change, do not change
            else:

                print('The phone number was not changed')
                return str(self.phone_number)

        self.phone_number[phone_number[0]] = phone_number[1]
        return self.phone_number


"""
Testing stuff:

juan = Person('Juan', '98 Kimbark Boulevard', [('personal', '4165644604'), ('dad', '4162781221')],
              [('personal', 'juandavidguerra1@gmail.com')], 'myself')

juan.add_phone_number(('personal', '4166660541'))
"""
