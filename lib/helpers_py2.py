from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        'Department {} not found'.format(name))


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print('Department {} not found'.format(id_))


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print('Success: {}'.format(department))
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print('Success: {}'.format(department))
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print('Department {} not found'.format(id_))


def delete_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print('Department {} deleted'.format(id_))
    else:
        print('Department {} not found'.format(id_))


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print('Employee {} not found'.format(name))


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print('Employee {} not found'.format(id_))


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id:")
    try:
        employee = Employee.create(name, job_title, int(department_id))
        print('Success: {}'.format(employee))
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        try:
            name = input("Enter the employees's new name: ")
            employee.name = name
            job_title = input("Enter the employee's new job title:")
            employee.job_title = job_title
            department_id = input("Enter the employees's new department id: ")
            employee.department_id = int(department_id)
            employee.update()
            print('Success: {}'.format(employee))
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print('Employee {} not found'.format(id_))


def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print('Employee {} deleted'.format(id_))
    else:
        print('Employee {} not found'.format(id_))


def list_department_employees():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print('Department {} not found'.format(id_))