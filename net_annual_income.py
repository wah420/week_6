def annual_net_income(gross_salary):

    if gross_salary >= 45000:
        tax_rate = 0.50
    elif 30000 <= gross_salary < 45000:
        tax_rate = 0.30
    else: 
        tax_rate = 0.15

    net_salary = gross_salary * (1 - tax_rate)
    return net_salary

try:
    gross_salary = float(input("Enter your annual gross salary: £"))
    net_salary = annual_net_income(gross_salary)
    print(f"Your annual net income after tax is: £{net_salary:.2f}")
except ValueError:
    print("Invalid input! Please enter a valid number for the salary.")
