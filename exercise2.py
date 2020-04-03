# Calculate amount of a tip to leave at a restaurant, and output the amount to be paid evenly when split
# Prompt the user for total bill amount, level of service, and how many ways to split the bill

# Setup
bill = float(input('How much is your bill? '))
service_message = '(Good, Fair, or Bad)'
level_of_service = input(f'How was your service?\n{service_message}\n').lower()
# determine if bill will be split
bill_split = int(input('Split how many ways? '))

# Calculate the tip and determine the level of service
# levels of service: good -> 20% , fair -> 15% , bad -> 10%

# Calculate tip amount
tip = float(0)
total_to_pay = float(0)
if level_of_service == 'good':
    tip = float(.20)
elif level_of_service == 'fair':
    tip = float(.15)
elif level_of_service == 'bad':
    tip = float(.10)
tip = bill * tip
total_to_pay = bill + tip
# Determine amount per person
individual_total = total_to_pay / float(bill_split)


# Output the tip amount, total with tip, and the amount to pay per person
print(f'Tip amount: ${"%.2f" % tip}')
print(f'Total amount: ${"%.2f" % total_to_pay}')
print(f'Amount per person: ${"%.2f" % individual_total}')