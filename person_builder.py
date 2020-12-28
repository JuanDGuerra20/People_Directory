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
        return 'Name: ' + self.first_name + ' ' + self.last_name + '\n' + 'Address: ' + self.address + '\n' \
               + 'Phone numbers: ' + str(self.phone_number) + '\n' + 'Emails: ' + str(self.email) + '\n' + \
               'Relationship: ' + self.relationship

    def add_phone_number(self, phone_number):
        """
        (tuple) --> String
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

    def change_address(self, new_address):
        """
        This instance method changes the address
        :param new_address: string that is the new person's address
        :return: the new address
        """

        self.address = new_address

        return self.address


juan = Person('JUAN', 'GUERRA', '98 Kimbark Boulevard', [('personal', '4165644604')],
              [('personal', 'juandavidguerra1@gmail.com')], 'myself')

print(str(juan))
something = [juan]
another = ['work', '4162781221']
something[0].add_phone_number((another[0], another[1]))
print(str(juan))

terminate = False
list_of_contacts = []
print('Welcome to the contacts directory! \n')

while not terminate:

    print('Options are:')
    print('1: Add a new contact')
    print('2: Modify a contact')
    print('3: Terminate program')

    option = input('Select one of the options (1,2 or 3): ')

    while option not in ['1', '2', '3']:
        print('Incorrect input type. Please choose 1, 2, or 3')
        print('Options are:')
        print('1: Add a new contact')
        print('2: Modify a contact')
        print('3: Terminate program')

        option = input('Select one of the options (1,2 or 3): ')

    option = int(option)

    # user wants to add a contact
    if option == 1:

        # taking in the simple information
        input_first_name = input('Please enter the first name of the contact: ').upper()
        input_last_name = input('Please enter the last name of the contact: ').upper()
        input_address = input('Please enter the full address of the contact: ')

        # following is for the phone numbers
        print('Please enter the type of phone number (personal, etc.) followed by a comma then number')
        input_phone = input('In this format - personal,5555555555: ').upper()

        # creating the list that will hold the numbers
        list_of_numbers = []

        # splitting the input at the comma
        input_phone = input_phone.split(',')
        # adding the phone number and type into the list of numbers
        list_of_numbers.append((input_phone[0], input_phone[1]))

        # asking the user if they want to add more numbers
        print('Would you like to add another number?')
        more_phones = input('YES or NO: ').upper()

        # making sure the input is correct
        while more_phones != 'YES' and more_phones != 'NO':
            more_phones = input('Incorrect input. Please type YES or NO').upper()

        # if the user wants to add more numbers
        while more_phones == 'YES':
            # same as above, taking the number and putting it into a tuple and appending
            print('Please enter the type of phone number (personal, etc.) followed by a comma then number')
            input_phone = input('In this format - personal,5555555555 ').upper()

            input_phone.split(',')
            list_of_numbers.append((input_phone[0], input_phone[1]))

            print('Would you like to add another number?')
            more_phones = input('YES or NO: ')
            more_phones = more_phones.upper()

            # checking for the correct type of input
            while more_phones != 'YES' and more_phones != 'NO':
                more_phones = input('Incorrect input. Please type YES or NO').upper()

        # doing the same as the phone number but with emails (input should be same type)
        print('Please enter the type of email (personal, etc.) followed by a comma then the email')
        input_email = input('In this format - personal,johndoe@gmail.com: ').upper()

        list_of_emails = []

        input_email = input_email.split(',')
        list_of_emails.append((input_email[0], input_email[1].lower()))

        print('Would you like to add another email?')
        more_emails = input('YES or NO: ')
        more_emails = more_emails.upper()

        while more_emails != 'YES' and more_emails != 'NO':
            more_emails = input('Incorrect input. Please type YES or NO').upper()

        while more_emails == 'YES':
            print('Please enter the type of email (personal, etc.) followed by a comma then the email')
            input_email = input('In this format - personal,johndoe@gmail.com: ').upper()

            list_of_emails = []

            input_email.split(',')
            list_of_emails.append((input_email[0], input_email[1].lower()))

            print('Would you like to add another email?')
            more_emails = input('YES or NO: ').upper()

            while more_emails != 'YES' and more_emails != 'NO':
                more_emails = input('Incorrect input. Please type YES or NO').upper()

        # Taking the relationship to the user
        input_relationship = input('Please input your relationship to this person: ')

        # creating the contact and storing it in a variable with the first name of the contact
        input_first_name = Person(input_first_name, input_last_name, input_address, list_of_numbers,
                                  list_of_emails, input_relationship)

        # adding the contact to the list of contacts
        list_of_contacts.append(input_first_name)

    # if the user chooses option 2, allow them to modify a person
    elif option == 2:
        if list_of_contacts == []:
            print('There are no contacts to modify. Please choose options 1 or 3')
        else:

            print('Which contact would you like to modify?')
            counter = 0
            for contact in list_of_contacts:
                print(str(counter) + ': ' + contact.first_name + ' ' + contact.last_name)
                counter += 1

            # This will be the index of the contact in the contact list
            modify_contact = input('Please enter the number of the contact you wish to modify: ')

            while not modify_contact.isdigit() and int(modify_contact) > counter:
                print('Unsupported number. Please try again')
                modify_contact = input('Please enter the number of the contact you wish to modify: ')

            modify_contact = int(modify_contact)

            print('What would you like to do? The options are:')
            print('1: Add a phone number')
            print('2: Add multiple phone numbers')
            print('3: Add an email')
            print('4: Add multiple emails')
            print('5: Change the address')
            print('6: Change the relationship to the contact')

            modify_choice = input('Which option would you like? ')

            while not modify_choice.isdigit() and int(modify_choice) > 6:
                print('Unsupported option. Please try again')
                modify_choice = input('Which option would you like? ')

            modify_choice = int(modify_choice)

            if modify_choice == 1:
                print('Please enter the type of phone number (personal, etc.) followed by a comma then number')
                new_phone = input('In this format - personal,5555555555: ').upper()

                new_phone = new_phone.split(',')
                list_of_contacts[modify_contact].add_phone_number((new_phone[0], new_phone[1]))

                print('Here is the new contact:')
                print(str(list_of_contacts[modify_contact]))

            elif modify_choice == 2:
                # following is for the phone numbers
                print('Please enter the type of phone number (personal, etc.) followed by a comma then number')
                input_phone = input('In this format - personal,5555555555: ').upper()

                # creating the list that will hold the numbers
                list_of_numbers = []

                # splitting the input at the comma
                input_phone = input_phone.split(',')
                # adding the phone number and type into the list of numbers
                list_of_numbers.append((input_phone[0], input_phone[1]))

                # asking the user if they want to add more numbers
                print('Would you like to add another number?')
                more_phones = input('YES or NO: ').upper()

                # making sure the input is correct
                while more_phones != 'YES' and more_phones != 'NO':
                    more_phones = input('Incorrect input. Please type YES or NO').upper()

                # if the user wants to add more numbers
                while more_phones == 'YES':
                    # same as above, taking the number and putting it into a tuple and appending
                    print('Please enter the type of phone number (personal, etc.) followed by a comma then number')
                    input_phone = input('In this format - personal,5555555555 ').upper()

                    input_phone.split(',')
                    list_of_numbers.append((input_phone[0], input_phone[1]))

                    print('Would you like to add another number?')
                    more_phones = input('YES or NO: ')
                    more_phones = more_phones.upper()

                    # checking for the correct type of input
                    while more_phones != 'YES' and more_phones != 'NO':
                        more_phones = input('Incorrect input. Please type YES or NO').upper()

                # adding the list of phone numbers to the contact
                list_of_contacts[modify_contact].add_list_of_phone_numbers(list_of_numbers)

                print('Here is the new contact:')
                print(str(list_of_contacts[modify_contact]))

            elif modify_choice == 3:
                print('keep going')

    # if the user chooses option 3, terminate the program in a polite manner :)
    elif option == 3:
        print('Thank you for using the contacts directory!')
        print('Have a nice day!')
        terminate = True
