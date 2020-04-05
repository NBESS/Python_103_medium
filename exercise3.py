### Find out how many coins a user wants.
# Begin with no coins, Print tally. 
# Ask if user wants a coin? If "yes", Give one coin, 
# Print out the updated tally. 
# If "no", stop the program

count = 0
farewell = 'Goodbye!'

#show amount in hand
coin_total = 0
coin_message = f'You have {coin_total} coins.'

#display coin amount
print(coin_message)

#continue asking for another until the answer is no
while input('Would you like another: ').lower() == 'yes':
    #add another if yes
    coin_total += 1
    print(f'you have {coin_total} coins')
    count += 1

print(farewell)