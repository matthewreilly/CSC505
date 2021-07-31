# Abstract course
class Course:
  
    def __init__(self):
        self.name()
        self.Fee()
        self.available_batches()
  
    def name(self):
        raise NotImplementedError

    def Fee(self):
        raise NotImplementedError
  
    def available_batches(self):
        raise NotImplementedError
  
    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)
  
# concrete course
class DSA(Course):
  
    """Class for Data Structures and Algorithms"""
  
    def Fee(self):
        self.fee = 8000
  
    def available_batches(self):
        self.batches = 5
  
    def __str__(self):
        return "DSA"
  
# concrete course
class SDE(Course):
  
    """Class for Software Development Engineer"""
  
    def Fee(self):
        self.fee = 10000
  
    def available_batches(self):
        self.batches = 4
  
    def __str__(self):
        return "SDE"
  
# concrete course
class STL(Course):
  
    """Class for Standard Template Library"""
  
    def Fee(self):
        self.fee = 5000
  
    def available_batches(self):
        self.batches = 7
  
    def __str__(self):
        return "STL"
 
class user_course(Course):
    """Class that the user enters"""

    def name(self):
        self.name = input('Enter course name: ')
    
    def Fee(self):
        self.fee = input('Enter fee: ')
    
    def available_batches(self):
        self.batches = input('Enter number of batches: ')

    def __str__(self):
        name = input('Enter name of class: ')
        return name

# main method
if __name__ == "__main__":
  
    # dsa = DSA()  # object for DSA course
    # sde = SDE()  # object for SDE course
    # stl = STL()  # object for STL course
  
    course_list = []
    user_input = ''
    while user_input != '3':
        print('\n**CHOOSE AN OPTION**')
        user_input = input('1. Add course\n\
2. Display course list\n\
3. Quit.\n')

        if user_input == '1':
            new_course = user_course()
            course_list.append(new_course)
        elif user_input == '2':
            print('***COURSE LIST***')
            for i in range(len(course_list)):
                print(f'\nCourse name: {course_list[i].name}')
                print(f'Course cost: ${course_list[i].fee}')
                print(f'course batches: {course_list[i].batches}\n')
        elif user_input == '3':
            break
        else:
            print('Invalid input\n')


    # course1 = user_course()
    # print(f'course1: {course1}')
    # print(f'course1.fee: {course1.fee}')
    # print(f'course1.batches: {course1.batches}')
    