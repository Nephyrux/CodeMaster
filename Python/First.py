''' !   Time to start a new exciting journey. This is the main file for the rest of the python scripts
        Lets become the best at this. '''
# Assigning multiple variables
first_string, second_string, exclamation_mark = 'Hello', 'World', '!'
print( first_string + ' ' + second_string + exclamation_mark )

# Constants ( All caps )
PI = 3.1415926

# Functions
def function_sample(): # function name is known as the FUNCTION SIGNATURE
    print( 'This is just a sample.' )

print( 'This executes before the function.' )
function_sample()

# Text files
from os import curdir
f = open( 'test_file.txt' )
content = f.read()
print( content )
f.close

# OR (which closes the file automatically)
with open( 'test_file.txt' ) as f:
    content = f.read()
    print( content )