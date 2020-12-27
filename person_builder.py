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

    def __init__(self, first_name, last_name, address, phone_number, list_email, relationship):
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

        self.first_name = first_name  # creating the name variable
        self.last_name = last_name
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
        return 'Name: ' + self.first_name + ' ' + self.last_name + '\n' + 'Address: ' + self.address + '\n'\
            + 'Phone numbers: ' + str(self.phone_number) + '\n' + 'Emails: ' + str(self.email) + '\n' + \
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

            print("The " + phone_number[0] + " number type is already registered as: " + self.phone_number[
                phone_number[0]])
            print("Would you like to replace the number with: " + phone_number[1])

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
                return self.phone_number

            # if user does not want to change, do not change
            else:

                print('The phone number was not changed')
                return self.phone_number

        self.phone_number[phone_number[0]] = phone_number[1]
        return self.phone_number

    def add_list_of_phone_numbers(self, phone_list):
        """
        (self, list) --> dict
        :param phone_list: list of phone numbers with each index being a tuple
        :return: returning a dictionary of the new phone number list
        """

        # looping through all the indices of the list to add the phone numbers
        for number in phone_list:
            # running the instance method already created to add the phone numbers
            self.add_phone_number(number)

        print('New numbers are: ' + str(self.phone_number))
        # returning the dictionary of numbers
        return self.phone_number

    def add_email(self, new_email):
        """
        This instance method adds new email data into the object of type class
        :param new_email: type = tuple --> (type of email, email)
        :return: self.email
        """

        # checking if the type of email already exists in the dictionary
        # example: personal is already in the email dictionary
        # if so, ensure that the user wants to change the type of email
        if new_email[0] in self.email:

            print("The " + new_email[0] + " email type is already registered as: " + self.email[
                new_email[0]])
            print("Would you like to replace the email with: " + new_email[1])

            # creating the variable that will hold the choice type
            replace_choice = input("YES or NO: ").upper()

            # ensuring that the type of input is correct
            while replace_choice != "YES" and replace_choice != "NO":
                print('Unsupported input. Try again with Yes or No')

                # retrying the input
                replace_choice = input("YES or NO: ")

                replace_choice = replace_choice.upper()

            # if the user wants to change, then change the email
            if replace_choice == 'YES':

                print('Changing the email')
                # changing the value of the desired email to the new email
                self.email[new_email[0]] = new_email[1]
                return self.email

            # if user does not want to change, do not change
            else:

                print('The email was not changed')
                return self.email

        self.email[new_email[0]] = new_email[1]
        return self.email

    def add_multiple_emails(self, email_list):
        """
        This instance method adds a list of emails and their type to the email dictionary
        :param email_list: list of tuples
        :return: self.email --> dictionary
        """

        # looping through all the indices of the list to add the emails
        for email in email_list:
            # running the instance method already created to add the email
            self.add_email(email)

        print('New emails are: ' + str(self.email))
        return self.email


"""
Testing stuff:

juan = Person('Juan', 'Guerra', '98 Kimbark Boulevard', [('personal', '4165644604'), ('dad', '4162781221')],
              [('personal', 'juandavidguerra1@gmail.com')], 'myself')

print(str(juan))
juan.add_multiple_emails([('work', 'juan.guerra@mail.mcgill.ca'), ('personal', 'juandavidguerra2@gmail.com')])

print(str(juan))
"""