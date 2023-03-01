# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 3/1/2023
# Description: Class named employee that has private data members and uses them to initialize
#              the data members. Separate function that takes a list to create an employee
#              object which creates and returns resulting dictionary.

class Employee:
    """Employee private data information"""
    def __init__(self, name, id_number, salary, email_address):
        """Initializes data members with argument values"""
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address

def make_employee_dict(names, id_numbers, salaries, email_addresses):
    """Creates an employee object from a list, adds them to a dictionary to be returned.
    The key is the ID number and the value for the key is the employee object. Returns
    resulting dictionary.
    """
    employee_dict = {} # creates dictionary
    for i in range(len(names)): # makes employee to add to dictionary
        employee = Employee(names[i], id_numbers[i], salaries[i], email_addresses[i])
        employee_dict[id_numbers[i]] = employee
    return employee_dict


# emp_names = ["Jean", "Kat", "Pomona"]
# emp_ids = ["100", "101", "102"]
# emp_sals = [30, 35, 28]
# emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
# result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
# print(result["100"].get_name())