# Making FA to check if a variable is valid or not

# Start state (var_state_1)
def var_state_1(char):
    # Checking the first character of the variable
    state = 0
    if((ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    else:
        state = 3
    return state

# Final State (var_state_2)
def var_state_2(char):
    # Checking the rest character of the variable
    state = 0
    if((ord(char) == 36) or (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    else:
        state = 3
    return state

# State 3 (var_state_3)
def var_state_3(char):
    # Dead state (variable name not valid)
    state = 0
    if(char):
        state = 3
    else:
        state = 3
    return state