# Print multipulcation tables from 1 to 10 in the following format:
# "1 x 1 = 1"

# Setup
num1 = 1

# Do the work
while num1 < 11:
    num2 = 0
    while num2 < 13:
        product = num1 * num2
        print(f'{num1} x {num2} = {product}')
        num2 += 1
    num1 += 1