
'''
Remaining tasks:
- Check that adding dmg reports works
- Consider a method to auto-associate damage reports w/ known potholes
- Consider adding a method to prevent duplicate pothole reports
- Submit/Edit/Delete/Display work orders
--- Should work orders be part of the Pothole class? or their own class? 
- Explore outputting damage reports to an external file (maybe ask instructor
if this is what he wants)
- Figure out the difference between Critical Thinkingi 5 and 6
'''

class PHTRS():
    def __init__(self):
        self.name = 'Pothole Tracking and Repair System'
        self.potholeDB = []
        self.workorderDB = []
        self.damageDB = []

    def add_pothole(self, pothole):
        self.potholeDB.append(pothole)
        return

    def remove_pothole(self):
        print('**POTHOLE DATABASE**')
        for i in range(len(self.potholeDB)):
            print(f'Pothole ID: {self.potholeDB[i].ID}')
            print(f'Pothole street: {self.potholeDB[i].street_address}')
            print(f'Pothole size: {self.potholeDB[i].size}')
            print(f'Pothole location: {self.potholeDB[i].location}')

        pothole_to_remove = input('Enter the ID of the pothole you want to remove: ')
        for i in range(len(self.potholeDB)):
            if self.potholeDB[i].ID == pothole_to_remove:
                del self.potholeDB[i]
                print(f'Pothole {pothole_to_remove} has been delted.\n')
                return
        # If pothole ID not found in potholeDB, tell user, return to main menu.
        print(f'Pothole ID {pothole_to_remove} not found in database.\n')
        return

    def display_potholeDB(self):
        print('\n**POTHOLE DATABASE**')
        for i in range(len(self.potholeDB)):
            print(f'Pothole ID: {self.potholeDB[i].ID}')
            print(f'Pothole street: {self.potholeDB[i].street_address}')
            print(f'Pothole size: {self.potholeDB[i].size}')
            print(f'Pothole location: {self.potholeDB[i].location}')
        return

    def display_damageDB(self):
        print('\n**DAMAGE DATABASE**')
        for i in range(len(self.damageDB)):
            print(f'Name of individual: {self.damageDB[i].name}')
            print(f'Address: {self.damageDB[i].address}')
            print(f'Phone number: {self.damageDB[i].number}')
            print(f'Dagame type: {self.damageDB[i].type}')
            print(f'Amount: ${self.damageDB[i].amount}')
        return

    def add_workorder(self, dmg_report):
        self.damageDB.append(dmg_report)
        return

    def add_damagereport(self):
        pass
        return

class Pothole:
    def __init__(self):
        self.ID = 'none'
        self.street_address = 'none'
        self.size = 0
        self.location = 'none'
        self.district = 'none'
        self.priority = 0
        self.crew_ID = self.ID
        self.crew_size = 0
        self.crew_eqip = []
        self.hours = 0
        self.status = 'none'
        self.filler = 0
        self.cost = 0
        self.damage_caused = []

# class WorkOrder:
# 	def __init__(self):
# 		self.ID = ''
# 		self.street_address = ''
# 		self.size = 0
# 		self.crew_ID = ''
# 		self.crew_size = 0
# 		self.crew_eqip = []
# 		self.hours = 0
# 		self.status = ''
# 		self.filler = 0
# 		self.cost = 0

class DamageReport:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.number = ''
        self.type = ''
        self.amount = 0
#////////////////////////////////////////////////////////////////
def new_pothole(PHTRS):
    pothole = Pothole()
    # Need to add option/interface to back out if user didnt mean to get here
    pothole.ID = len(PHTRS.potholeDB)
    pothole.street_address = input('Enter the street the pothole is one: ')
    pothole.size = int(input('Enter the size of the hole (1-10): '))
    pothole.location = input('Where is the pothole located (street, curb, etc.)? ')
    pothole.district = input('Enter the disctrict the pothole is in: ')
    # priority would need to be chosen by public works folks,
    # not the person reporting a pothole online
    ####pothole.priority = Reverse of size
    pothole.priority = pothole.size

    user_input = input('Would you like to submit a damage rerport for this hole? (yes or no)\n')
    if user_input == 'yes':
        dmg_report = new_damage_report()
        pothole.damage_caused.append(dmg_report)
        PHTRS.damageDB.append(dmg_report)
    
    print()
    return pothole
#///////////////////////////////////////////////////////////////
def new_damage_report():
    dmg_report = DamageReport()
    dmg_report.name = input('Enter your name: ')
    dmg_report.address = input('Enter your address: ')
    dmg_report.number = input('Enter your phone number: ')
    dmg_report.type = input('Enter the type of damage incurred: ')
    dmg_report.amount = int(input('Enter the dollar amount of damage caused: '))
    return dmg_report
#///////////////////////////////////////////////////////////////
def remove_pothole():

    return
#////////////////////////////////////////////////////////////////
def menu():
    menu ="\nMENU\n \
1. - Add pothole report\n \
2. - Remove pothole report\n \
3. - Submit damage report\n \
4. - Submit work order\n \
5. - Edit work order\n \
6. - Display pothole/work order/damage info\n \
7. - Quit"

    user_input = ''
    while user_input != '7':
        print(menu)
        user_input = input('Choose an option: ')
        if user_input == '1':
            pothole = new_pothole(PHTRS)
            PHTRS.add_pothole(pothole)
        elif user_input == '2':
            PHTRS.remove_pothole()
        elif user_input == '3':
            dmg_report = new_damage_report()
            PHTRS.add_damagereport(dmg_report)
        elif user_input == '4':
            pass
        elif user_input == '5':
            pass
        elif user_input == '6':
            print('Choose an option: ')
            print('1. Pothole Database')
            print('2. Work Order Database')
            print('3. Damage Report Database')
            answer = input()
            if answer == '1':
                PHTRS.display_potholeDB()
            elif answer == '2':
                pass
            elif answer == '3':
                PHTRS.display_damageDB()
            else:
                print('Invalid input.\n')
        elif user_input == '7':
            break
        else:
            print('Invalid Input. Please choose an option:\n')
            
    return
#///////////////////////////////////////////////////////////////
if __name__ == '__main__':
    PHTRS = PHTRS()
    menu()