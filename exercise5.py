# Print a triangle of "*" characters

# Make the shape consiset of a 'center--character' enclosed by an even number of 'end--characters on both sides


# Determine the amount of characters on each side
char_on_each_side = int(input('How many characters on each side of center_character? '))

# Do the work
center_char = '*'
left_end_char = char_on_each_side * center_char
right_end_char = char_on_each_side * center_char

count = 0
while count < 1:
    end_char = " "
    print(f'{left_end_char}{center_char}{right_end_char}')



# Print the output