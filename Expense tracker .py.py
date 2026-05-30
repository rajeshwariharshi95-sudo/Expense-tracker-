expenseslist = []

print("Welcome to Expense Tracker: Kharcha kam kara karo")

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        date = input("On which date did you spend the money?: ")
        category = input("Which type of expenditure (food, travel, makeup, books)?: ")
        description = input("Give more details about the expenditure: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenseslist.append(expense)
        print("Expense added successfully!")

    elif choice == 2:
        if len(expenseslist) == 0:
            print("No expenses added.")
        else:
            print("\n=== All Expenses ===")
            count = 1

            for expenditure in expenseslist:
                print(
                    f"{count}. {expenditure['date']} | "
                    f"{expenditure['category']} | "
                    f"{expenditure['description']} | "
                    f"₹{expenditure['amount']}"
                )
                count += 1

    elif choice == 3:
        total = 0

        for expenditure in expenseslist:
            total += expenditure["amount"]

        print(f"\nTotal Expenditure = ₹{total}")

    elif choice == 4:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice. Try Again.")
