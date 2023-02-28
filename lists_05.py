

employees = []

number_of_employees = int(input("Koliko djelatnika zelite kreirati? "))

for i in range(number_of_employees):
    full_name = input(f"Upisite puno ime {i + 1}. djelatnika: ")
    employees.append(full_name)
    
for employee in employees:
    print(employee) 
    

