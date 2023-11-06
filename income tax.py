while True:
    try:
        income = int(input("Please enter your taxable income in India: "))
    except ValueError:
        print("Sorry, We didn't understand that please enter taxable income as a number")
        continue
    else:
        break

print("-----------------------------------")
print("Income of the Employee:", income)
print("-----------------------------------")
no_tax_amount =  250000 

discount_amount = 50000

# deducted 50000 from the annual income

final_income = income - discount_amount

print("Tax Charges on this Income:", final_income)
print("-----------------------------------")
# if the income is below 250000 then the tax amount should be null or 0 

if final_income<=250000:
    print("Tax amount for", income, "is :", 0)
    print("-----------------------------------")

#This is the condition for the first_tax amount

first_tax = final_income>250000 and final_income<=500000
# if the income is between 250000 and 500000 then the tax is
if first_tax:
    print("Tax amount for", income, "is", int((final_income-250000)*5/100))
    print("-----------------------------------")
    
#This is the condition for the second_tax amount

second_tax = final_income>500000 and final_income<=750000
# if the income is between 500000 and 750000 then the tax is
if second_tax:
    print("Tax amount for", income, "is :", int(((final_income-500000) * 10/100) + no_tax_amount * (5/100)))
    print("-----------------------------------")

#This is the condition for the third_tax amount

third_tax = final_income > 750000 and final_income<=1000000
# if the income is between 500000 and 750000 then the tax is
if third_tax:
    print("Tax amount for", income, "is :", int((final_income - 750000) * 15/100 + no_tax_amount* (10/100) + no_tax_amount* (5/100)))
    print("-----------------------------------")

#This is the condition for the fourth_tax amount

fourth_tax = final_income > 1000000 and final_income<= 1250000
# if the income is between 750000 and 1000000 then the tax is
if fourth_tax:
    print("Tax amount for", income, "is :", int(((final_income-1000000) * 20/100+ no_tax_amount * (10/100) + no_tax_amount* (5/100) + no_tax_amount * (15/100))))
    print("-----------------------------------")

#This is the condition for the fifth_tax amount

fifth_tax = final_income > 1250000 and final_income <= 1500000
# if the income is between 1000000 and 1500000 then the tax is
if fifth_tax:
    print("Tax amount for", income, "is :", int((final_income - 1250000) * 25/100 + no_tax_amount* (10/100) + no_tax_amount* (5/100) + no_tax_amount * (15/100)+no_tax_amount*(20/100) ))
    print("-----------------------------------")

#This is the condition for the last_tax amount

last_tax = final_income>1500000
# if the income is greater than 1500000 then the tax is
if last_tax :
    print("Tax amount for", income, "is :", int((final_income-1500000) * 30/100 +  no_tax_amount * (10/100) + no_tax_amount * (5/100) + no_tax_amount * (15/100)+ no_tax_amount *(20/100) + no_tax_amount*(25/100)))
    print("-----------------------------------")
