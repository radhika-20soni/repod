current_age = int(input("Enter your current age: "))
desired_age = int(input("Enter desired marriage age: "))
estimated_expenses = float(input("Enter estimated wedding expenses: "))
current_savings = float(input("Enter current savings: "))
annual_savings = float(input("Enter annual savings: "))

if desired_age <= current_age:
    print("Error: Desired marriage age must be greater than current age.")
else:
    years_to_marriage = desired_age - current_age
    if estimated_expenses > current_savings:
        remaining = estimated_expenses - current_savings
        if remaining / annual_savings > years_to_marriage:
            print("It's not possible to save enough money by the desired marriage age.")
        else:
            print("It is possible to save enough money.")
            years_to_save = (remaining + annual_savings - 1) // annual_savings
            print(f"You need {years_to_save} more years to save enough.")
    else:
        print("You have enough savings.")

