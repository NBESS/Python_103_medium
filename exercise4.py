# Prompt a user for additional coins until they refuse.
# Increase amount with each coin and tell user new total.
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