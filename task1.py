employees = [
    {'Name': 'Anu', 'age': 21, 'des': "Junior Developer", "Exp_in_years": 1},
    {'Name': 'Pooja', 'age': 25, 'des': "Senior Developer", "Exp_in_years": 4},
    {'Name': 'Sam', 'age': 28, 'des': "Senior Developer", "Exp_in_years": 8},
    {'Name': 'Priya', 'age': 27, 'des': "Senior Developer", "Exp_in_years": 7},
    {'Name': 'James', 'age': 22, 'des': "Junior Developer", "Exp_in_years": 2},
    {'Name': 'Ajay', 'age': 26, 'des': "Senior Developer", "Exp_in_years": 5}
]

def get_employee_detail():
    user_input = input("Enter the employee's name: ")
    
    normalized_input = user_input.lower()

    
    for employee in employees:
        if employee['Name'].lower() == normalized_input:
            print(f"Employee found: {employee}")
            return

    
    print("Employee not found.")
    add_employee = input("Would you like to add this employee's details? (yes/no): ").lower()

    if add_employee in ['yes', 'y']:
        name = input("Enter the employee's name: ")
        age = int(input("Enter the employee's age: "))
        des = input("Enter the employee's designation: ")
        exp = int(input("Enter the employee's experience in years: "))
        
        
        new_employee = {'Name': name, 'age': age, 'des': des, 'Exp_in_years': exp}
        employees.append(new_employee)
        print(f"Employee {name} added successfully.")
    else:
        print("Operation aborted.")

get_employee_detail()
