### Find out how many coins a user wants.
# Begin with no coins, Print tally. 
# Ask if user wants a coin? If "yes", Give one coin, 
# Print out the updated tally. 
# If "no", stop the program


# Setup
coin_amount = 0
tally_message = f'You have {coin_amount} coins.'
coin_prompt = input('Would you lke another? ').lower()
final_message = 'Goodbye!'

# Perform Operation
# Output tally
print(tally_message)

# Continue asking user for coins until they answer "no"
while coin_prompt == 'yes':         # Ask user for coin 
    coin_amount = coin_amount + 1           
    print(tally_message)            # Print the updated tally
    if coin_prompt == 'no':          # If no stop the program
        print(final_message)