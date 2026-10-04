expenses = []
while True:
    print("-------------Expense Tracker------------------")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
     try:
        name = input("Enter item name: ")
        amount = float(input("Enter price amount: "))
        if amount > 0:
         expenses.append({
            "name": name,
            "amount": amount
        })
         print("Item added successfully")
        else:
         print("Amount must be greater than 0")
     except ValueError:
      print("Please enter a valid input!")
    elif choice == "2":
        if expenses:
         for expense in expenses:
            print(expense["name"],"-",expense["amount"])
        else:
           print("No expenses found!!!")
    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print("Total: ",total)
    elif choice == "4":
        print("Goodbye")
        break
    else:
     print("Invalid choice! Please enter 1-4.")
