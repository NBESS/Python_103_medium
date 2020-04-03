# Calculate amount of a tip to leave at a restaurant.
# Prompt the user for two things, total bill amount and level of service

# Setup
bill = float(input('How much is your bill? '))
service_message = 'Good, Fair, or Bad'
level_of_service = input(f'How was your service?\n{service_message}\n').lower()

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


# Output the tip amount based on level of service
print(f'Tip amount: ${"%.2f" % tip}')
print(f'Total amount: ${"%.2f" % total_to_pay}')