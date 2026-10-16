
#   \'	Single Quote	
#   \\	Backslash	
#   \n	New Line	
#   \r	Carriage Return	     It moves the output cursor back to the beginning of the current line without advancing to a new line, allowing you to overwrite existing text on that line.
#   \t	Tab	
#   \b	Backspace	
#   \f	Form Feed	
#   \ooo	Octal value	
#   \xhh	Hex value


txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

# lower() vs casefold()
# lower()       Preparing text for display to the user.
# casefold()    Evaluating user input and matching data.

txt = "banana å"

x = txt.center(20, '-')     # take space of 120 characters with banana in the middle
y = txt.encode()
print(y)

# format()
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

We have 49                   chickens.