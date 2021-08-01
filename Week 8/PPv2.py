
# The customer must pass authentication before withdrawing money.
# Authentication is performed by checking a PIN.
# The PIN can be correct or not.
# Unsuccessful attempts are counted.
# If the counter exceeds a limit, then the customer is rejected.
# If the account balance is zero, then the account is closed.

#/////////////////////////////////////////////

class account:
    def __init__(self):
        self.PIN = '1234'
        self.is_open = True
        self.balance = 100

    def validate_PIN(self):
        # Allows user 3 attempts to enter the correct PIN. 
        failed_pin_count = 0
        while failed_pin_count < 3:
            pin = input('Enter your 4-digit pin: ')
            if pin == self.PIN:
                return True
            else: 
                failed_pin_count += 1
                print('Invalid PIN. Please try again: ')
        print('\nLogin attemt limit exceeded.\n\
    Please contact customer service.\n')
        return False


    def withdraw(self):
        if self.is_open == False:
            print('Your account has been closed.\n')
            return

        # Ensures user enters an integer
        while True:        
            withdrawal_amount = input('Enter the amount to withdraw: ')
            try:
                withdrawal_amount = int(withdrawal_amount)
            except ValueError:
                print('Invalid input. Please try again.\n')
                continue
            break
        
        # If remaining balance will be positive, withraw money
        if self.balance - withdrawal_amount > 0:
            self.balance = self.balance - withdrawal_amount
            print(f'You withdrew ${withdrawal_amount}.')
            print(f'Your remaining balance is: ${self.balance}')
        # If remaining balance will be negative, inform user of insufficient funds
        elif self.balance - withdrawal_amount < 0:
            print('Insufficient funds.') 
            print(f'Your balance is ${self.balance}\n')
        # If remaining balance will be $0, inform user. Allow user to select whether to proceed
        # Reaching a $0 balance results in acccount closure.
        else: 
            print(f'\nWithdrawing ${withdrawal_amount} will bring your balance to $0.')
            print(f'If your balance reaches $0, your account will be closed.')
            user_input = input('Would you like to proceed? Type yes or no.\n')
            if user_input == 'yes':
                self.balance = self.balance - withdrawal_amount
                self.is_open = False
                print(f'Your remaining balance is: ${self.balance}\n')
                print('Your account has been closed.\n')
        return 

    def check_balance(self):
        if self.is_open == True:
            print(f'Current balance: ${self.balance}\n')
        else:
            print('Your account balanced reached $0 and has been closed.\n')
        return
#////////////////////////////////////////////////
def print_menu():
    menu = '\nSelect an option:\n\
w - Withdraw\n\
C - Check account balance\n\
E - Exit'

    user_input = ''
    while user_input.lower() != 'e':
        print(menu)
        user_input = input()
        if user_input.lower() == 'w':
            checking_acct.withdraw()
        elif user_input.lower() == 'c':
            checking_acct.check_balance()
        elif user_input.lower() == 'e':
            break
        else:
            print('Invalid input. Please choose an option:\n')

    return
#//////////////////////////////////////////////////
if __name__ == '__main__':
    checking_acct = account()
    login_success = checking_acct.validate_PIN()
    if login_success == True:
        print_menu()