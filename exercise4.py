# make a square with user input length as string of "*"
# make user's input for height string "*  *" 
# on the first and last numbers in shape only

count = 0
shape_char_width = ''
width = int(input('Enter width: '))
shape_char_height = ''
height = int(input('Enter height: '))
spaces = 0
    
### to make shape an empty box
# print shape's base -- to make top of shape

# length of users input equal string of desired length
# base is equal to designated -- shape_char, "*" 
# multiplied by the width, integer

# Top of shape
shape_char_width = width * '*'

# to make shape's height, print sides
# sides will be print "shape_char_height, string" for sides 
# consisting of a string of "spaces", 
# that continue for "width - 2", as to avoid exceeding 
# length of shape
# thus allowing the "spaces" to be enclosed in, "shape_char,'*' 

while count < 2:
    shape_char_height += '*'
    count += 1
    while width > 2 and spaces < width - 2:
        shape_char_height += ' '
        spaces += 1
print(shape_char_height)

# print to make bottom of shape
print(shape_char_width)