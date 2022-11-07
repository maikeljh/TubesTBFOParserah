# Making FA to check expression is valid or not

# Start State
def Expression_state_1(char):
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
    # Dead state (Expression not valid)
    state = 0
    if(char):
        state = 3
    else:
        state = 3
    return state

# Second Final State
def Expression_state_4(char):
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
    # Checking if there is = after = (==)
    state = 0
    if(ord(char) == 61):
        state = 6
    else:
        state = 3
    return state

# FA to check if an expression is valid or not
def CheckExpression(expression):
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

