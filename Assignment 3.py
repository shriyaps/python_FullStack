##Create a class for patient appointment booking.
##Create two methods
##1. To ask the details of the patient
##2. To display the appointment details.

class Patient:
    def __init__(self, fn = ' ', ln = ' ', a = 0, g = ' ', p = 0):
        self.fname = fn
        self.lname = ln
        self.age = a
        self.gender = g
        self.phone = p

    def detail(self):
        print(10*"----")    
        print("Details of the Patient: ")
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Contact No.: ", self.phone)

    def appointment(self):
        print(10*"----")
        doctor = input("Enter doctor's name: ")
        date = input("Appointment Date: ")
        time = input("Appointment Time: ")
        print(f"Your appointment with Dr. {doctor} will be on {date} at {time}!")

fname = input("Enter first name: ")
lname = input("Enter last name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
phone = int(input("Enter contact number: "))


p1 = Patient(fname, lname, age, gender, phone)
p1.detail()
p1.appointment()
            
            
            
            
