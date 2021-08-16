def calculate_bill_per_person(bill, people_number, tip):
    return round((bill * (1 + tip/100)) / people_number, 2)

def main():
    print("Welcome to the tip calculator")
    total_bill = float(input("What was the total bill? $"))
    people_number = float(input("How many people to split the bill? "))
    percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
    result = calculate_bill_per_person(total_bill, people_number, percentage_tip)
    print("Each person should pay: " + str(result))

if __name__ == '__main__':
    main()