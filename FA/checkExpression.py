# Making FA to check expression is valid or not

# Start State
def Expression_state_1(char):
    """
    State 1 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking the first character of the variable
    state = 0
    if((ord(char) == 33) or (ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif(ord(char) >= 48 and ord(char) <= 57):
        state = 4
    else:
        state = 3
    return state

# First Final State
def Expression_state_2(char):
    """
    State 2 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking the rest character of the variable
    state = 0
    if((ord(char) == 36) or (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif(ord(char) == 32):
        state = 5
    elif(ord(char) == 37 or ord(char) == 42 or ord(char) == 43 or ord(char) == 45 or ord(char) == 47):
        state = 6
    elif(ord(char) == 38):
        state = 7
    elif(ord(char) == 124):
        state = 8
    elif(ord(char) == 60 or ord(char) == 62):
        state = 9
    elif(ord(char) == 61 or ord(char) == 33):
        state = 10
    else:
        state = 3
    return state

def Expression_state_3(char):
    """
    State 3 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Dead state (Expression not valid)
    state = 0
    if(char):
        state = 3
    else:
        state = 3
    return state

# Second Final State
def Expression_state_4(char):
    """
    State 4 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if the number consist of number only or not
    state = 0
    if(ord(char) >= 48 and ord(char) <= 57):
        state = 4
    elif(ord(char) == 32):
        state = 5
    elif(ord(char) == 37 or ord(char) == 42 or ord(char) == 43 or ord(char) == 45 or ord(char) == 47):
        state = 6
    elif(ord(char) == 38):
        state = 7
    elif(ord(char) == 124):
        state = 8
    elif(ord(char) == 60 or ord(char) == 62):
        state = 9
    elif(ord(char) == 61 or ord(char) == 33):
        state = 10
    else:
        state = 3
    return state

def Expression_state_5(char):
    """
    State 5 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if blank or operator is valid or not
    state = 0
    if(ord(char) == 32):
        state = 5
    elif(ord(char) == 37 or ord(char) == 42 or ord(char) == 43 or ord(char) == 45 or ord(char) == 47):
        state = 6
    elif(ord(char) == 38):
        state = 7
    elif(ord(char) == 124):
        state = 8
    elif(ord(char) == 60 or ord(char) == 62):
        state = 9
    elif(ord(char) == 61 or ord(char) == 33):
        state = 10
    else:
        state = 3
    return state

def Expression_state_6(char):
    """
    State 6 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if blank or make sure there is number or variable after operator
    state = 0
    if(ord(char) == 32):
        state = 6
    elif((ord(char) == 33) or (ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif(ord(char) >= 48 and ord(char) <= 57):
        state = 4
    else:
        state = 3
    return state

def Expression_state_7(char):
    """
    State 7 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if there is another & after & (&&) or make sure there is number or variable after &
    state = 0
    if((ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif(ord(char) >= 48 and ord(char) <= 57):
        state = 4
    if(ord(char) == 38 or ord(char) == 32):
        state = 6
    else:
        state = 3
    return state

def Expression_state_8(char):
    """
    State 8 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if there is another | after | (||) or make sure there is number or variable after |
    state = 0
    if((ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif(ord(char) >= 48 and ord(char) <= 57):
        state = 4
    elif(ord(char) == 124 or ord(char) == 32):
        state = 6
    else:
        state = 3
    return state

def Expression_state_9(char):
    """
    State 9 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if there is = after < or > (<= or >=) or make sure there is number or variable after < or >
    state = 0
    if((ord(char) == 36) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) == 95) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif(ord(char) >= 48 and ord(char) <= 57):
        state = 4
    elif(ord(char) == 61 or ord(char) == 32):
        state = 6
    else:
        state = 3
    return state

def Expression_state_10(char):
    """
    State 10 of FA Check Expression

    Args:
        char (char): char of expression

    Returns:
        state (int): next state
    """
    # Checking if there is = after = (==)
    state = 0
    if(ord(char) == 61):
        state = 6
    else:
        state = 3
    return state

# FA to check if an expression is valid or not
def CheckExpression(expression):
    """
    Function FA to check expression valid or not

    Args:
        expression (string) : expression

    Returns:
        boolean : True if expression valid
    """
    state = 1
    for char in expression:
        if(state == 1):
            state = Expression_state_1(char)
        elif(state == 2):
            state = Expression_state_2(char)
        elif(state == 3):
            state = Expression_state_3(char)
        elif(state == 4):
            state = Expression_state_4(char)
        elif(state == 5):
            state = Expression_state_5(char)
        elif(state == 6):
            state = Expression_state_6(char)
        elif(state == 7):
            state = Expression_state_7(char)
        elif(state == 8):
            state = Expression_state_8(char)
        elif(state == 9):
            state = Expression_state_9(char)
        elif(state == 10):
            state = Expression_state_10(char)
    
    if(state == 2 or state == 4):
        return True
    else:
        return False

