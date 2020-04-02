# Calculate amount of a tip to leave at a restaurant.
# Prompt the user for two things, total bill amount and level of service

# Setup
bill = float(input('How much is your bill? '))
service_message = 'Good, Fair, or Bad'
level_of_service = input(f'How was your service?\n{service_message}').lower()

# Calculate the tip and determine the level of service
# levels of service: good -> 20% , fair -> 15% , bad -> 10%
total_to_pay =


# Output the tip amount based on level of service
print("%.2f" % total_to_pay)