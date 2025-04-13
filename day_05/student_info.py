import re

class Student:
    """a model of a student"""
    def __init__(self, first, last, ID):
        """the attributes of a student"""
        if not isinstance(ID, str) or len(ID) != 10:
            raise ValueError("ID must be a string of exactly 10 characters.")

        self.first = first
        self.last = last
        self.ID = ID
        self.courses = []
        self.status = None
        self.year = None
        self.dob = None
        self.phone = None
        self.email = None

    def __str__(self):
        desc = f"{'First name:':>15}\t{self.first}\n"
        desc += f"{'Last name:':>15}\t{self.last}\n"
        desc += f"{'ID:':>15}\t{self.ID}\n"
        if self.courses:
            desc += f"{'Courses:':>15}\t{self.courses}\n"
        if self.status:
            desc += f"{'Status:':>15}\t{self.status}\n"
        if self.year:
            desc += f"{'Year:':>15}\t{self.year}\n"
        if self.dob:
            desc += f"{'Date of Birth:':>15}\t{self.dob}\n"
        if self.phone:
            desc += f"{'Phone:':>15}\t{self.phone}\n"
        if self.email:
            desc += f"{'Email:':>15}\t{self.email}\n"
        return desc

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_full_name(self):
        """Returns the student's full name"""
        return f"{self.first.title()} {self.last.title()}"

    def get_ID(self):
        return self.ID

    def get_courses(self):
        return self.courses

    def set_courses(self, *courses):
        for course in courses:
            self.courses.append(course)

    def add_courses(self, course):
         self.courses.append(course)

    def get_status(self):
        return self.status

    def set_status(self, status):
        statuses = ['active', 'full time', 'part time', 'expelled']
        if status.lower() in statuses:
            self.status = status
        else:
            print(f"Invalid option. {status}")

    def get_year(self):
        return self.year

    def set_year(self, year):
        years = ['freshman', 'sophomore', 'junior', 'senior', 'super senior']
        if year.lower() in years:
            self.year = year
        else:
            print(f"Invalid year option. {years}")

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        if dob is not None:
            dob_pattern = r"^\d{2}-\d{2}-\d{4}$"
            if not isinstance(dob, str) or not re.match(dob_pattern, dob):
                print("Date of birth must be a string in 'MM-DD-YYYY' format (e.g., '12-24-2004').")
        self.dob = dob

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        if phone is not None:
            phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
            if not isinstance(phone, str) or not re.match(phone_pattern, phone):
                print("Phone must be a string in '###-###-####' format (e.g., '555-555-1234').")
        self.phone = phone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email