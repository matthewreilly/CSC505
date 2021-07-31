# Module 3: Option 2
# Matt Reilly
# Colorado State University Global
# CSC505: Principles of Software Development
# Dr. Joseph Issa
# 8 August, 2021

# DESCRIPTION
#   This python script provides a very basic implementation of the user story
# and use case described in my Module 3 Critical Thinking Option #2 report. The
# user story and use case describe the "favorites" feature on a cellphone. This
# script walks the user through the logical steps associated with:
# 1. Adding a site to the "favorites" list
# 2. Allowing the user to edit the name of the site
# 3. Allowing the user to open the favorites list and manually add/edit/remove
#    entries.
# 4. Allow the user to open a webpage from the favorites list

#///////////////////////////////////////////////////////////////////////////////
class Favorite:
    def __init__(self):
        self.name = 'none'
        self.URL = 'none'
#///////////////////////////////////////////////////////////////////////////////
# This function is used to simulate a user browing the internet since
def choose_random_site():
    import random
    list_sites = ['csuglobal.edu','geeksforgeeks.org','fullstackpython.com']
    num = random.randint(0,2)
    site = list_sites[num]
    print('\nYou have navigated to {}'.format(site))
    return site
#///////////////////////////////////////////////////////////////////////////////
def add_to_favorites():
    print('\nStep 1: Open browser.')
    # Step 2: allow user to input a webpage or let script pick a 'random' one to
    #   simulate browsing
    site = input('Enter a webpage URL or type "random" to simulate \
browsing:\n')
    print()
    if site == 'random':
        site = choose_random_site()
    else:
        print('You have navigated to {}'.format(site))

    print('You, the user, then select the bookmark icon to add page to favorites list.\n')
    favorite_name = input('Enter a name for this bookmark: ')
    favorite = Favorite()
    favorite.name = favorite_name
    favorite.URL = site
    favorites_list.append(favorite)

    print('\n{} added to favorites list\n'.format(favorite_name))

    return
#///////////////////////////////////////////////////////////////////////////////
# Allows user to remove an entry from the favorites list
def remove_favorite():
    print('\nFAVORITES LIST:')
    for i in range(len(favorites_list)):
        print('{}. {}'.format(i+1, favorites_list[i].name))
    site = input('\nEnter the name of the site to be removed: ')
    for i in favorites_list:
        if i.name == site:
            favorites_list.remove(i)
    return
#///////////////////////////////////////////////////////////////////////////////
# Allows user to edit the name and/or URL of a favorites list entry
def edit_favorites():
    print('\nFAVORITES LIST:')
    for i in range(len(favorites_list)):
        print(favorites_list[i].name)
    print()
    site = input('\nEnter the name of the site you\'d like to edit: ')
    for i in favorites_list:
        if i.name == site:
            name_change = input('\nWould you like to change the name (yes or no)?\n')
            if name_change == 'yes':
                i.name = input('Enter new name: ')
            URL_change = input('Would you like to change the URL (yes or no)?\n')
            if URL_change == 'yes':
                i.URL = input('Enter new URL: ')
            print('\nNew Entry:')
            # print('Name: {}'.format(i.name))
            # print('URL: {}\n'.format(i.URL))
            print(f'Name: {i.name}\nURL: {i.URL}\n')
    return
#///////////////////////////////////////////////////////////////////////////////
# Allows user to open a webpage from the favorites list
def go_to_site():
    print('\nFAVORITES LIST:')
    for i in range(len(favorites_list)):
        print(favorites_list[i].name)
    print()
    site = input('Enter the name of the site you wish to go to: ')
    for i in favorites_list:
        if i.name == site:
            print('You have navigated to {}\n'.format(i.URL))
    '''need to add check for valid entry'''
    return
#///////////////////////////////////////////////////////////////////////////////
# This is the menu of options that allows users to interact with the favorites list
def use_favorites():
    print('\nFAVORITES LIST:')
    for i in range(len(favorites_list)):
        print(favorites_list[i].name)
    print()

    what_to_do = ''
    while what_to_do != '5':
        what_to_do = input('Choose an option:\n\
1. Manually add to favorites list\n\
2. Remove item from favorites list\n\
3. Edit item in favorites list\n\
4. Open item in favorites list\n\
5. Exit to main menu.\n')

        if what_to_do == '1':
            favorite = Favorite()
            favorite.name = input('Enter the bookmark\'s name: ')
            favorite.URL = input('Enter the bookmark\'s URL: ')
            favorites_list.append(favorite)
            print()
        elif what_to_do == '2':
            remove_favorite()
        elif what_to_do == '3':
            '''NEED TO COMPLETE function'''
            edit_favorites()
        elif what_to_do == '4':
            go_to_site()
        elif what_to_do == '5':
            break
        else:
            print('Invalid input.\n')

    return

#///////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    favorites_list = []
    #print_menu()
    print('This script walks you through the functional requirements of \
the "favorites" feature on a cellphone.\n')
    user_input = ''

    #   Allow user to browse the internet and add pages to favorites list as
    # they go, allow them to open the favorites list and interact with it
    # directly, and allow user to exit the program
    while user_input != '3':
        user_input = input('Choose an option:\n\
1. Add webpage to favorites list\n\
2. Access/manipulate/use favorites list\n\
3. Quit\n')
        if user_input == '1':
            add_to_favorites()
        elif user_input == '2':
            use_favorites()
        elif user_input == '3':
            break
        else:
            print('Invalid input. Please choose an option: \n')
