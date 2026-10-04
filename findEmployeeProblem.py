# Problem:  Search for an employee using EmployeeID ask user to enter employee ID and search it.
employees = [
 (101, "Alice", 50000),
 (102, "Bob", 65000),
 (103, "Charlie", 45000)
]
search_id = int(input("Enter employee ID: "))
for employee in employees:
    id = employee[0]
    if search_id == id:
        print("Employee found!!!")
        print("Employee id: ",employee[0])
        print("Employee name: ",employee[1])
        print("Employee salary: ",employee[2])
        break
if id != search_id:
    print("No employee found")
