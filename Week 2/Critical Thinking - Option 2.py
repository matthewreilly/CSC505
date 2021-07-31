# Module 2: Option 1
# Matt Reilly
# Colorado State University Global
# CSC505: Principles of Software Development
# Dr. Joseph Issa
# 1 August, 2021

# DESCRIPTION
#   Assigmnet instructions: "Draft a communication diagram for stakeholders
# that prompts a usr to input their [requirements] specifications and returns
# the object of their input."
#
# This is the pythonic implementation of the system/UML diagram described above.
# This python script allows users to add requirements to a requirements database 
# and allows the user to output the contents of the database.

class req_database:
    def __init__(self):
        self.name = 'none'
        self.items = []

    # Adds requirement to the database
    def add_req(self, ReqToAdd):
        self.items.append(ReqToAdd)
        return

    # Checks whether the ID of the submitted requirement is already in the DB
    def check_duplicate_reqs(self, ReqToCheck):
        is_duplicate = False
        if len(self.items) == 0:
            pass
        else:
            for i in range(len(self.items)):
                if self.items[i].ID == ReqToCheck.ID:
                    is_duplicate = True
        return is_duplicate

    # Outputs the requirements database
    def print_database(self):
        print('You entered the following requirements:\n')
        for i in range(len(req_database.items)):
            print('Requirement ID: {}'.format(req_database.items[i].ID))
            print('Stakeholder: {}'.format(req_database.items[i].stakeholder))
            print('Priority: {}'.format(req_database.items[i].priority))
            print('Description: {}\n'.format(req_database.items[i].description))
        return
#//////////////////////////////////////////////////////////////////////
# The class from which the requirement objects will be created
class Requirement:
    def __init__(self):
        self.ID = 'none'
        self.stakeholder = 'none'
        self.priority = 0
        self.description = 'none'

#///////////////////////////////////////////////////////////////////////
def print_menu(req_database):
# Displays menu of options. Allows user to add requirements to the database and
# output the requirements database
    menu = '\nMENU\n \
a - Add Requirement\n \
o - Output Requirements\n \
q - Quit\n'

    user_input = ''
    while user_input.lower() != 'q':
        print(menu)
        user_input = input('Choose an option: ')
        print()
        if user_input.lower() == 'a':
            new_req = create_new_requirement()
            # req_database.add_req(new_req)
            is_duplicate = req_database.check_duplicate_reqs(new_req)
            if is_duplicate == False:
                req_database.add_req(new_req)
            else:
                print('This requirement has already been submitted.\n')
        elif user_input.lower() == 'o':
            req_database.print_database()
        elif user_input.lower() == 'q':
            break
        else:
            print('Invalid input. Pleas choose an option:\n')

    return

#///////////////////////////////////////////////////////////////////////
# Allows user to create a new requirement
def create_new_requirement():
    new_requirement = Requirement()
    new_requirement.ID = input('Enter the requirement\'s ID: ')
    new_requirement.stakeholder = input('Enter your organization: ')
    new_requirement.priority = input('Enter a requirement priority from 1-5.\n \
    (1 being the highest): ')
    new_requirement.description = input('Enter the requirement\'s description: ')

    return new_requirement
#///////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    req_database = req_database()
    req_database.name = 'CSC505 Requirement Database'
    print_menu(req_database)
