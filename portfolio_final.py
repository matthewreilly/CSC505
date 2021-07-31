# CSC 500, Module 8: Portfolio Project (final version) - Option #1
# Created by Matt Reilly. 19 Jan 2021 (last updated 25 Feb 2021)

# References:
# Lysecky, et al. (2019). CSC500: principles of programming. zyBooks.
#   https://learn.zybooks.com/zybook/CSC500zyBookInteractiveText2020

#//////////////////////////////////////////////////////////////////////////////
# Create a new object class that will be used for all retail items in this program
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, \
self.item_price, self.item_price * self.item_quantity))
        return
#//////////////////////////////////////////////////////////////////////////////
# Create object class that will be used for the "shopping cart" in this program
class ShoppingCart:
    def __init__(self, name='None', date = "January 1, 2020"):
        self.customer_name = name
        self.date = date
        self.cart_items = []

    def add_items(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        return

    # Chekcs if item is in cart. If not, outputs error message. Removes item if
    #   item was already in the cart.
    def remove_items(self, ItemToRemove):
        for i in range(len(self.cart_items)):
            if ItemToRemove == self.cart_items[i].item_name:
                del self.cart_items[i]
                print('{} was removed from cart.\n'.format(ItemToRemove))
                return
        # If item is not found in cart, tell user, then return to main menu.
        print('Item not found in cart.\n')
        return

    '''add price and quantity valid entry checks'''
    # If item is already in cart, this function allows the user to modify an
    #   item's price, quantity, or description.
    def modify_item(self, ItemToModify):
        item_in_cart = False
        for i in range(len(self.cart_items)):
            if ItemToModify == self.cart_items[i].item_name:
                item_loc = i
                item_in_cart = True
        if item_in_cart == False:
            print('Item not found in cart.\n')
            return
        else: # Item IS in the cart

            # Prompt user for what they want to modify (price, quantity, or
            #   description). Re-prompt if input is invalid. Continue prompting
            #   until user enters 'r' to return to the main menu.
            user_choice = ''
            while user_choice != 'r':
                print('\nWhat would you like to modify?')
                print('p - Price\nq - Item Quantity\nd - Item Description\n\
r - Return to Main Menu')
                user_choice = input('Choose an option:\n')

                # Change item quantity
                if user_choice == 'q':
                    print('\nCurrent quantity: {}'\
                    .format(self.cart_items[item_loc].item_quantity))
                    while True:
                        try:
                            new_quant = int(input('Enter the new quantity:\n'))
                        except ValueError:
                            print('Invalid quantity. Please try again.\n')
                            continue
                        self.cart_items[item_loc].item_quantity = new_quant
                        break

                # Change item price
                elif user_choice == 'p':
                    print('\nCurrent price: {:.2f}'\
                    .format(self.cart_items[item_loc].item_price))

                    while True:
                        item_price = input('Enter the item\'s price:\n').replace('$','')
                        try:
                            new_price = float(item_price)
                        except ValueError:
                            print('Invalid price. Please try again.\n')
                            continue
                        self.cart_items[item_loc].item_price = new_price
                        break

                # Change item description
                elif user_choice == 'd':
                    print('\nCurrent description: {}'\
                    .format(self.cart_items[item_loc].item_description))
                    new_description = input('Enter new description:\n')
                    self.cart_items[item_loc].item_description = new_description

                # Return to main menu if user enters 'r'
                elif user_choice == 'r':
                    break

                else: # Invalid entry
                    print('Invalid input\n')
        return

    def get_num_items_in_cart(self):
        total_items = 0
        for i in range(len(cart1.cart_items)):
            total_items += cart1.cart_items[i].item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cart_cost = 0
        for i in range(len(cart1.cart_items)):
            total_cart_cost += cart1.cart_items[i].item_quantity * \
            cart1.cart_items[i].item_price
        return total_cart_cost

    def print_total(self):
        if len(cart1.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(cart1.customer_name, cart1.date))
            total_items = cart1.get_num_items_in_cart()
            print('Number of Items: {}'.format(total_items))
            for i in range(len(cart1.cart_items)):
                print('{} {} @ ${:.2f} = ${:.2f}'.format(cart1.cart_items[i].item_name, \
                cart1.cart_items[i].item_quantity, \
                cart1.cart_items[i].item_price, \
                cart1.cart_items[i].item_price * cart1.cart_items[i].item_quantity))
            total_cart_cost = cart1.get_cost_of_cart()
            print('Total: ${:.2f}'.format(total_cart_cost))
        return

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}'.format(cart1.customer_name, cart1.date))
        print('Item Descriptions')

        for i in range(len(cart1.cart_items)):
            print('{}: {}'.format(cart1.cart_items[i].item_name, \
cart1.cart_items[i].item_description))

        return
#//////////////////////////////////////////////////////////////////////////////
# Display option menu to user. Get user inputs. Call to whichever functions are
#   required to satisfy user's option selection.
def print_menu(ShoppingCart):

    menu ="\nMENU\n \
a - Add item to cart\n \
r - Remove item from cart\n \
m - Modify item price, quantity, or description\n \
i - Output items' descriptions\n \
o - Output shopping cart\n \
q - Quit"

    user_input = ''

    while user_input.lower() != 'q':
        print(menu)
        user_input = input('Choose an option: ')
        if user_input.lower() == 'a':
            item = create_new_item()
            ShoppingCart.add_items(item)
        elif user_input.lower() == 'r':
            item = input('Enter the name of the item you\'d like to remove:\n')
            ShoppingCart.remove_items(item)
            #call function to remove item from cart
        elif user_input.lower() == 'm':
            item = input('Enter the name of the item you\'d like modify:\n')
            ShoppingCart.modify_item(item)
        elif user_input.lower() == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            ShoppingCart.print_descriptions()
        elif user_input.lower() == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.print_total()
        elif user_input.lower() == 'q':
            break
        else: # user entered invalid option
            print('Invalid input. Please choose an option:\n')

    return
#//////////////////////////////////////////////////////////////////////////////
# Creates a new item with name, price, quantity, and description attributes
#   input by the user.
def create_new_item():
    item = ItemToPurchase()
    item.item_name = input('Enter the item name:\n')

    while True: # Use while, try, and except to ensure valid price input
        item_price = input('Enter the item\'s price:\n').replace('$','')
        try:
            item.item_price = float(item_price)
        except ValueError:
            print('Invalid price. Please try again.\n')
            continue
        break

    while True: # Use while, try, and except to ensure valid price input
        try:
            item.item_quantity = int(input('Enter the item quantity:\n'))
        except ValueError:
            print('Invalid quantity. Please try again.\n')
            continue
        break

    item.item_description = input('Enter item description\n')

    return item
#//////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':

    # Create shopping cart and get user's info (name, date)
    cart1 = ShoppingCart()
    cart1.customer_name = input('Enter customer name: ')
    cart1.date = input('Enter date in the following format - \
Month Day, Year: ')
    # Display menu, prompt user for desired actions
    print_menu(cart1)

