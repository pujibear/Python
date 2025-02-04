
# Bryan Cruz
#Github Link: https://github.com/pujibear/Python/blob/main/Homework%203



# This first section I have to find the amount from the user using the input function and decided to use a float function to convert the string to a float
# to be able to calculations. 
mortgage = input("Tell me how much you pay for your mortgage?")
mortgage = float(mortgage)
utilities = input("Tell me how much you spend on utilities?")
utilities =float(utilities)
groceries = input("Tell me how much you spend on groceries?")
groceries =float(groceries)
transportation = input("Tell me how much you spend on transportation?")
transportation =float(transportation)
healthcare = input("Tell me how much you spend on healthcare?")
healthcare =float(healthcare)
personalcare = input("Tell me how much you spend on yourself?")
personalcare =float(personalcare)
clothing = input("Tell me how much you spend on clothing?")
clothing =float(clothing)
debt = input("Tell me how much your paying towards debt?")
debt =float(debt)

total = mortgage + utilities + groceries + transportation + healthcare + personalcare + clothing + debt #Total of all expenses 

#This bottom section is find the percentage of each category and prints it out for the user. 

percent1 = (mortgage / total) * 100 
print(f"Your mortgage is {percent1:.2f}% of your total budget")

percent2 = (utilities / total) * 100 
print(f"Your utilities is {percent2:.2f}% of your total budget")

percent3 = (groceries / total) * 100 
print(f"Your groceries is {percent3:.2f}% of your total budget")

percent4 = (transportation / total) * 100 
print(f"Your transportation is {percent4:.2f}% of your total budget")

percent5 = (healthcare / total) * 100 
print(f"Your healthcare is {percent5:.2f}% of your total budget")

percent6 = (personalcare / total) * 100 
print(f"Your personalcare is {percent6:.2f}% of your total budget")

percent7 = (clothing / total) * 100 
print(f"Your clothing is {percent7:.2f}% of your total budget")

percent8 = (debt / total) * 100 
print(f"Your debt is {percent8:.2f}% of your total budget")
