from checkExpression import *

# Open file javascript
txt = open("./testcase/testExpValid.txt", "r")
# txt = open("./testcase/testExpNotValid.txt", "r")

# Read variable name
expression = txt.read()

if(CheckExpression(expression)):
    print(expression, "is valid!")
else:
    print(expression, "is NOT valid!")
