from models.department import Department
from models.employee import Employee
import unittest


class TestEmployeeProperties(unittest.TestCase):
    '''Class Employee in employee.py'''

    def setUp(self):
        '''drop and recreate tables prior to each test.'''
        Employee.drop_table()
        Department.drop_table()
        Department.create_table()
        Employee.create_table()
        # clear the object cache
        Department.all = {}
        Employee.all = {}

    def test_name_job_department_valid(self):
        '''validates name, job title, department id are valid'''
        # should not raise exception
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)

    def test_name_is_string(self):
        '''validates name property is assigned a string'''
        with self.assertRaises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)
            employee.name = 7

    def test_name_string_length(self):
        '''validates name property length > 0'''
        with self.assertRaises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)
            employee.name = ''

    def test_location_is_string(self):
        '''validates job_title property is assigned a string'''
        with self.assertRaises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)
            employee.job_title = 7

    def test_location_string_length(self):
        '''validates job_title property length > 0'''
        with self.assertRaises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department.id)
            employee.job_title = ''

    def test_department_property(self):
        department = Department.create("Payroll", "Building C, 3rd Floor")
        employee = Employee.create(
            "Raha", "Accountant", department.id)  # no exception

    def test_department_property_fk(self):
        with self.assertRaises(ValueError):
            Employee.create("Raha", "Accountant", 7)

    def test_department_property_type(self):
        with self.assertRaises(ValueError):
            employee = Employee.create("Raha", "Accountant", "abc")
