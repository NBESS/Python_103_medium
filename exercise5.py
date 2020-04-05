# Print a triangle of "*" characters

# Make the shape consiset of a 'center--character' enclosed by an even number of 'end--characters on both sides


# Determine the amount of characters on each side
char_on_each_side = int(input('How many characters on each side of center_character? '))

# Do the work

count = 0
while count < 1:
    center_char = '*'
    end_char = " "
    left_end_char = char_on_each_side * end_char
    right_end_char = char_on_each_side * end_char    
    print(f'{left_end_char}{center_char}{right_end_char}')
    levels = 0
    space_on_side = char_on_each_side
    new_center_char = '*'
    while levels < char_on_each_side:
        space_on_side -= 1
        left_end_char = space_on_side * end_char
        right_end_char = space_on_side * end_char         
        print(f'{left_end_char}{new_center_char}{center_char}{new_center_char}{right_end_char}')
        new_center_char += '*'
        levels += 1
    count += 1
