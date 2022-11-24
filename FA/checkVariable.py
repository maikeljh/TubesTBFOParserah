# Making FA to check if a variable is valid or not

# Start state (var_state_1)
def Var_state_1(char):
    """
    State 1 of FA Check Variable

    Args:
        char (char): char of variable

    Returns:
        state (int): next state
    """
    # Checking the first character of the variable
    state = 0
    if((ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    else:
        state = 3
    return state

# Final State (var_state_2)
def Var_state_2(char):
    """
    State 2 of FA Check Variable

    Args:
        char (char): char of variable

    Returns:
        state (int): next state
    """
    # Checking the rest character of the variable
    state = 0
    if((ord(char) == 36) or (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    else:
        state = 3
    return state

# State 3 (var_state_3)
def Var_state_3(char):
    """
    State 3 of FA Check Variable

    Args:
        char (char): char of variable

    Returns:
        state (int): next state
    """
    # Dead state (variable name not valid)
    state = 0
    if(char):
        state = 3
    else:
        state = 3
    return state

# Function FA for checking a variable name valid or not
def CheckVariable(variable_name):
    """
    Function for FA Check Variable

    Args:
        variable_name (string): variable name

    Returns:
        boolean : True if variable name valid
    """
    state = 1 # Start State
    for char in variable_name:
        if(state == 1):
            state = Var_state_1(char)
        elif(state == 2):
            state = Var_state_2(char)
        elif(state == 3):
            state = Var_state_3(char)
    if(state == 2):
        return True
    else:
        return False