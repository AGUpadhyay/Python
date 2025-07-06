# User Steps to Use Personal Expense Tracker
# Open the Program
# Run the expense tracker script in your console/terminal.

# See the Main Menu
# The program will show a list of options, like:

                # Add a new expense

                # Remove an expense

                # Show all expenses

                # Show categories

                # Show total spending

                # Show spending per category

                # Exit

# Choose an Action
# The user types the number or command corresponding to what they want to do.

# If Adding Expense:

# Enter category (like “food”, “transport”)

# Enter date (e.g., 2025-06-30)

# Enter amount spent (e.g., 250)

# If Removing Expense:

# See a numbered list of expenses

# Enter the number of the expense to remove

# If Viewing Expenses or Categories:

# The program prints the relevant info nicely formatted

# If Viewing Totals:

# Total spent or spending per category is displayed

# Repeat or Exit

# After each action, the main menu shows again

# User can do more actions or exit by choosing “Exit”

total_expance=[]
cat=[]
spent=[]
cat_spent=[]
def new_expence(a,b,c):
    return[a,b,c]

while True:
    print("1. Add a new expense")
    print("2. Remove an expense")
    print("3. Show all expenses")
    print("4. Show categories")
    print("5. Show total spending")
    print("6. Show spending per category")
    print("Exit")
    x=int(input("Enter a value"))
    if x==1:
        print("Add a new expense")
        category=str(input("Add a new category"))
        date=input("Add a new Date")
        amount=float(input("Add a new Amount"))
        d=new_expence(category,date,amount)
        total_expance.append(d)
        print("Value added for category, date and amount",d)

    elif x==2:
        print("Remove an expense")
        print("Total Expence is", total_expance)
        del_elem=int(input("Choose Element"))
        total_expance.pop(del_elem-1)
        print("Now available total expence is ", total_expance)

    elif x==3:
        print("All expenses is", total_expance)

    elif x==4:
        print("Show categories")
        for n in total_expance:
            cat.append(n[0])
        print("Available Category is")
        print(cat)
    elif x==5:
        print("Total Spend:-\t")
        for n in total_expance:
            spent.append(n[2])
        print("Total Spend is\t")
        print(sum(spent))
    elif x==6:
        print("6. Show spending per category")
    else:
        break