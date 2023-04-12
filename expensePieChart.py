#Peter Parrella
#CS175L-02
#ExpensePieChart

import matplotlib.pyplot as plt

def main():

    try:

        with open("expenses.txt", "r") as f:
            data = f.readlines()

    except IOError:
        print("Error: Could not open the file")
        return

    expenses = {}

    for line in data:

        try:
            category, amount = line.strip().split('\t')
            expenses[category] = int(amount)

        except ValueError:
            print("Error: Could not convert data to integer")
            return

    labels = list(expenses.keys())
    values = list(expenses.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == '__main__':
    main()
