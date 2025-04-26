class Student:
    def __init__(self):
        self.name = ""
        self.dob = ""
        self.gender = ""
        self.father = ""
        self.nationality = ""
        self.address = ""
        self.phone_number = ""
        self.email = ""
        self.passout = ""
        self.ten = ""
        self.twelve = ""
        self.percent = 0
        self.clgname = ""
        self.code = ""
        self.selected_course = ""
        self.course_fees = ""
        self.course_duration = ""

    def Student_details(self):
        self.name = input("Enter your name: ")
        self.dob = input("Enter your date of birth (YYYY-MM-DD): ")
        self.gender = input("Enter your gender (Male/Female/Other): ")
        self.father = input("Enter your father's name: ")
        self.nationality = input("Enter your nationality: ")
        self.address = input("Enter your address: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email address: ")
        self.passout = input("Enter your year of passout: ")
        self.ten = input("Enter your 10th school name: ")
        self.twelve = input("Enter your 12th school name: ")
        self.percent = float(input("Enter your 12th marks in percentage: "))

        if self.percent > 50:
            print("You are Eligible to apply for both Arts and Engineering Colleges.")
            self.choose_field()  
        else:
            print("You are Eligible only for Arts Colleges.")
            self.choose_Arts()
            
    def choose_field(self):
        field = input("Do you want to pursue Engineering or Arts? (Enter 'Engineering' or 'Arts'): ").strip().lower()

        if field== "engineering":
            self.choose_Engineering()
        elif field == "arts":
            self.choose_Arts()
        else:
            print("Invalid choice! Please choose either 'Engineering' or 'Arts'.")
            self.choose_field()
            
    def choose_Engineering(self):
        self.clgname = input("Enter your Engineering College Name: ")
        self.code = input("Enter your Engineering College Code: ")
        self.display_Engineering()

    def display_Engineering(self):
        courses = {
            'Computer Science Engineering': {
                'fees': '₹2,00,000 per year',
                'duration': '4 years'
            },
            'Aerospace Engineering': {
                'fees': '₹1,50,000 per year',
                'duration': '4 years'
            },
            'Mechanical Engineering': {
                'fees': '₹80,000 per year',
                'duration': '4 years'
            },
            'Electrical and Electronics Engineering': {
                'fees': '₹1,00,000 per year',
                'duration': '4 years'
            },
            'Biotech Engineering': {
                'fees': '₹60,000 per year',
                'duration': '4 years'
            },
            'Civil Engineering': {
                'fees': '₹90,000 per year',
                'duration': '4 years'
            }
        }

        print("\nOffered Engineering Courses with Fees and Duration:")
        for course, details in courses.items():
            print(f"{course} - Fees: {details['fees']} - Duration: {details['duration']}")

        selected_course = input("Enter the engineering course you want to select: ")
        if selected_course in courses:
            self.selected_course = selected_course
            self.course_fees = courses[selected_course]['fees']
            self.course_duration = courses[selected_course]['duration']
            print(f"You selected: {selected_course}")
            print(f"Fees: {self.course_fees}")
            print(f"Duration: {self.course_duration}")
        else:
            print("Invalid course selection. Please try again.")
            self.display_Engineering() 

    def choose_Arts(self):
        self.clgname = input("Enter your Arts College Name: ")
        self.code = input("Enter your Arts College Code: ")
        self.display_Arts()

    def display_Arts(self):
        courses = {
            'Bachelor of Arts (English, Tamil, Mathematics, Physics, Chemistry, Botany, Zoology)': {
                'fees': '₹50,000 per year',
                'duration': '3 years'
            },
            'Bachelor of Fine Arts': {
                'fees': '₹70,000 per year',
                'duration': '4 years'
            },
            'Bachelor of Animation': {
                'fees': '₹80,000 per year',
                'duration': '3 years'
            },
            'Bachelor of Economics': {
                'fees': '₹60,000 per year',
                'duration': '3 years'
            },
            'Bachelor of Arts (Zoology)': {
                'fees': '₹50,000 per year',
                'duration': '3 years'
            },
            'Bachelor of Metallurgy': {
                'fees': '₹90,000 per year',
                'duration': '4 years'
            }
        }

        print("\nOffered Arts Courses with Fees and Duration:")
        for course, details in courses.items():
            print(f"{course} - Fees: {details['fees']} - Duration: {details['duration']}")

        selected_course = input("Enter the arts course you want to select: ")
        if selected_course in courses:
            self.selected_course = selected_course
            self.course_fees = courses[selected_course]['fees']
            self.course_duration = courses[selected_course]['duration']
            print(f"You selected: {selected_course}")
            print(f"Fees: {self.course_fees}")
            print(f"Duration: {self.course_duration}")
        else:
            print("Invalid course selection. Please try again.")
            self.display_Arts()

    
    

    def display_all_details(self):
        print("\n Student Details:")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Gender: {self.gender}")
        print(f"Father's Name: {self.father}")
        print(f"Nationality: {self.nationality}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"Year of Passout: {self.passout}")
        print(f"10th School: {self.ten}")
        print(f"12th School: {self.twelve}")
        print(f"12th Percentage: {self.percent}%")
        print(f"College Name: {self.clgname}")
        print(f"College Code: {self.code}")
        print(f"Selected Course: {self.selected_course}")
        print(f"Course Fees: {self.course_fees}")
        print(f"Course Duration: {self.course_duration}")
        print(f"Is there any changes in the form yes or no")
        confirmation = input("\nAre these details correct? (yes/no): ").strip().lower()
        if  confirmation == "yes":
          print("The Form submitted Successfully")
        else:
         while confirmation == "no":
            field_to_change = input("\nWhich field would you like to change? (Enter the field name or type 'all' to change everything): ").strip().lower()
            if field_to_change == "name":
              name = input("Enter your name: ")
            elif field_to_change == "dob":
              dob = input("Enter your date of birth (YYYY-MM-DD): ")
            elif field_to_change == "gender":
              gender = input("Enter your gender (Male/Female/Other): ")
            elif field_to_change == "father":
              father = input("Enter your father's name: ")
            elif field_to_change == "nationality":
              nationality = input("Enter your nationality: ")
            elif field_to_change == "address":
              address = input("Enter your address: ")
            elif field_to_change == "phone_number":
              phone_number = input("Enter your phone number: ")
            elif field_to_change == "email":
              email = input("Enter your email address: ")
            elif field_to_change == "passout":
              passout = input("Enter your year of passout: ")
            elif field_to_change == "ten":
              ten = input("Enter your 10th school name: ")
            elif field_to_change == "twelve":
              twelve = input("Enter your 12th school name: ")
            elif field_to_change == "percent":
              percent = float(input("Enter your 12th marks in percentage: "))
            elif field_to_change == "all":
              return self.Student_details()  
            else:
              print("Invalid field name. Please try again.")
              continue 
              student.display_all_details()

          

student = Student()
student.Student_details()
student.display_all_details()
