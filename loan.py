money_owed = float(input("How much money you want?\n")) # $67,000
apr = float(input("What is the annual percentage rate?\n")) # 5%
payment = float(input("What will your monthly payment be,in dollars?\n")) # $1,000
months = int(input("How many months do you want to see results for?\n")) #24

# divide apr by 100 to make it a percent, then divide by 12 to make monthly

monthly_rate = apr/100/12

for i in range(months):
#add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("the last payment is", money_owed)
        print("you paid off the loan in", i+1, "months")
        break

# make payment
    money_owed = money_owed - payment

#print the result after this month

print("paid", payment, "of which", interest_paid, "was interest" , end=' ')
print("Now I owe", money_owed)