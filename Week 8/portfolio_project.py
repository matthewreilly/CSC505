
# The customer must pass authentication before withdrawing money.
# Authentication is performed by checking a PIN.
# The PIN can be correct or not.
# Unsuccessful attempts are counted.
# If the counter exceeds a limit, then the customer is rejected.
# If the account balance is zero, then the account is closed.


#/////////////////////////////////////////////
def get_user_pin():
    actual_pin = '1234'
    failed_pin_count = 0
    is_pin_valid = False
    while failed_pin_count < 3:
        pin = input('Enter your 4-digit pin: ')
        if pin == actual_pin:
            return pin, True
            # failed_pin_count = 3 #forcing exit from loop
        else:
            failed_pin_count += 1
            print('Invalid PIN. Please try again: ')
    print('\nLogin attempt limit exceeded.\n\
Please contact customer service.\n')
    return pin, False
#//////////////////////////////////////////////////
def withdraw(current_balance):
    withdrawl_amount = int(input('Enter amount to withdraw: '))
    '''add a check that input is valid'''

    current_balance = current_balance - withdrawl_amount
    print('Remaining balance: ${}'.format(current_balance))
    return current_balance
#/////////////////////////////////////////////////
def check_balance(current_balance):
    print('Current balance is: ${}'.format(current_balance))
    return
#////////////////////////////////////////////////
def print_menu():
    menu = '\nSelect an option:\n\
w - Withdraw\n\
C - Check account balance\n\
E - Exit'
    current_balance = 100
    user_input = ''
    while user_input.lower() != 'e':
        print(menu)
        user_input = input()
        if user_input.lower() == 'w':
            current_balance = withdraw(current_balance)
        elif user_input.lower() == 'c':
            check_balance(current_balance)
        elif user_input.lower() == 'e':
            break
        else:
            print('Invalid input. Please choose an option:\n')

    return
#//////////////////////////////////////////////////
if __name__ == '__main__':
    pin, is_login_successful = get_user_pin()
    if is_login_successful == True:
        print_menu()
