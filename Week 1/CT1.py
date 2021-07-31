# Module 1: Option 1
# Matt Reilly
# Colorado State University Global
# CSC505: Principles of Software Development
# Dr. Joseph Issa
# July 25, 2021

# DESCRIPTION:
#   This script creates a list of cars' make, model, and price. The user has the
# option to add cars to the list, remove cars from the list, and dislpay the
# list. Future improvements to the script could allow for additional car details
# (ex: max range, top speed, safety rating, etc) and methods of filtering the
# list of cars based on various criteria (ex: price from lowest to highest).
#////////////////////////////////////////////////////////////
# Creates a new object class that will be used for all cars in this script
class Car:
    def __init__(self):
        self.car_make = 'none'
        self.car_model =  'none'
        self.car_price = 0
        # self.car_speed = 0
        # self.car_range = 0
        return
#////////////////////////////////////////////////////////////
# Creates an object class that will be used to contain the list of cars
class CarList:
    def __init__(self):
        self.customer_name = 'none'
        self.CarList_items = []

    def add_car(self, CarToAdd):
        self.CarList_items.append(CarToAdd)
        return

    # Check if car is in the list. If it's not, tell the user. If it is, remove it
    def remove_car(self, CarToRemove):
        for i in range(len(self.CarList_items)):
            if CarToRemove == self.CarList_items[i].car_model:
                print('{} {} was removed from your list.\n'.format(self.CarList_items[i].car_make, \
                CarToRemove))
                del self.CarList_items[i]
                return
        print('Car not found in list.\n')
        return

    def print_list(self):
        if len(CarList.CarList_items) == 0:
            print('Car list is empty')
        else:
            print('\n{}\'s Car List:'.format(CarList.customer_name))
            # total_cars = CarList.get_num_cars()
            for i in range(len(CarList.CarList_items)):
                print('{} {} @ ${:.0f}'.format(CarList.CarList_items[i].car_make, \
                CarList.CarList_items[i].car_model, \
                CarList.CarList_items[i].car_price))
        return

#////////////////////////////////////////////////////////////
#   Display option menu to user. Get user inputs. Call to whichever functions are
# required to satisfy user's option selection.
def print_menu(CarList):
    menu = "\nMENU\n \
a - Add car to list\n \
r - Remove car from list\n \
o - Output list\n \
q - Quit"

    user_input = ''

    while user_input.lower() != 'q':
        print(menu)
        user_input = input('Choose an option: ')
        if user_input.lower() == 'a':
            car = create_new_car()
            CarList.add_car(car)
        elif user_input.lower() == 'r':
            car = input('Enter the model of the car you\'d like to remove:\n')
            CarList.remove_car(car)
        elif user_input.lower() == 'o':
            CarList.print_list()
        elif user_input.lower() == 'q':
            break
        else: #user entered invalid option
            print('Inavlid input. Please choose an option:\n')

    return

#////////////////////////////////////////////////////////////
#   Creates a new instance of the Car() class with make, model, and price
# attributes input by the user.
def create_new_car():
    car = Car()
    car.car_make = input('Enter the car\'s make:\n')
    car.car_model = input('Enter the car\'s model:\n')

    # Use while, try, and except to ensure valid price input
    while True:
        car_price = input('Enter the car\'s price:\n').replace('$','')
        try:
            car.car_price = float(car_price)
        except ValueError:
            print('Invalid price. Please try again.\n')
            continue
        break
    return car
#////////////////////////////////////////////////////////////
if __name__ == '__main__':
    CarList = CarList() # Create a list of cars for comparison
    CarList.customer_name = input('Enter your name: ') # Get user's name
    print_menu(CarList) # Displaly menu & prompt user for desired actions
