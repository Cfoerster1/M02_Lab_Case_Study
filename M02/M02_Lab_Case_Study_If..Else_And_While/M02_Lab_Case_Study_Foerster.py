# Author: Cody Foerster
# File name: M02_Lab_Case_Study_Foerster.py
# Description: This program accepts student
# first name, last name, and gpa to determine
# what awards they are elegible for

while True:
    # ask for and accept a student's last name
    last_name = input("Enter student's last name: ")
    
    # quit processing student records if the last name entered is 'ZZZ'
    if last_name == "ZZZ":
        break
    
    # ask for and accept a student's first name
    first_name = input("Enter student's first name: ")
    
    # ask for and accept the student's GPA as a float
    gpa = float(input("Enter student's GPA: "))
    
    # Deans list if gpa is 3.5 or higher
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    
    # Honor Roll if gpa is 3.25 or higher.
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll!")
    
    # No award if gpa is lower than 3.25
    else:
        print(f"{first_name} {last_name} doesn't qualify for any awards")