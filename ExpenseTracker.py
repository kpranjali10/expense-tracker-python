expenses = []
print("EXPENSE TRACKER")    
print()
print("welocme!")
print("USE YOUR MONEY WISELY!")
print()

while True:
    print("========MENU========")
    print("1. add expense")
    print("2. view all expenses")
    print("3. view total amount spent")
    print("4. exit")

    choice = input("enter your choice (1-4): ")

    if choice == "1":
        date = input("enter the date:")
        amount = float(input("enter the amount:"))
        category = input("enter the category (e.g., food, transportation):")
        description = input("enter the description (e.g., dinner at restaurant):")

        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        print("expense added sucessfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("no expenses added yet")
        else:
            print("======HERE ARE YOUR EXPENSES======")
            count = 1
            for eachexpense in expenses:
                print(f"{count}. date: {eachexpense['date']} \n amount: {eachexpense['amount']}\n category: {eachexpense['category']} \n description: {eachexpense['description']}")
                count += 1

    elif choice == "3":
        total = 0
        for eachexpense in expenses:
            total += eachexpense['amount']
        print(f"total amount spent:{total}")

    elif choice == "4":
        print("exiting the expense tracker...")
        print("thankyou for using the expense tracker.")
        break

    else:
        print("invalid choice. please try again.")

