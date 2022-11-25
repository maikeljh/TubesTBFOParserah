from checkVariable import *

# Open file javascript
txt = open("../testcase/testVarValid.txt", "r")
# txt = open("../testcase/testVarNotValid.txt", "r")

# Read variable name
variable_name = txt.read()

# Validation with FA
state = 1 # Start State
for char in variable_name:
    if(state == 1):
        state = Var_state_1(char)
    elif(state == 2):
        state = Var_state_2(char)
    elif(state == 3):
        state = Var_state_3(char)

# Checking Variable Name Valid or Not
if(state == 2):
    print(variable_name, "is valid!")
else:
    print(variable_name, "is NOT valid!")
