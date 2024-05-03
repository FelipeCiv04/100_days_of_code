#tarefa para calcular a conta e dividir ela entre um determinado número de pessoas
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $ \n"))
tip_to_give = int(input("How much tip would you like to give? 10, 12 or 15? \n"))
people = int(input("How many people to split the bill? \n"))

tipx = int(tip_to_give) / 100
account = float(total_bill) * float(tipx)
new_bill = float(total_bill) + float(account)
spliting = float(new_bill) / int(people)

final_amount = "{:.2f}".format(spliting)

print(f"each person should pay : $ {final_amount}")