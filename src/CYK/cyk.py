# CYK Function
def CYK(splittedCode, CNF):
    """
    Function algorithm of CYK Table Filling

    Args:
        splittedCode (array): list of terminals of string code
        CNF (dictionary): dictionary of CNF
    """
    # Initialize Table For CYK
    Table = [[set([]) for i in range(len(splittedCode))] for j in range(len(splittedCode))]

    # Create Dictionary For Terminal
    dictionary_terminal = {}
    for var in CNF.items():
        # We check if Var -> Terminal is a rule
        for production in var[1]:
            if(len(production) == 1):
                if(production[0] not in dictionary_terminal.keys()):
                    dictionary_terminal[production[0]] = []
                    dictionary_terminal[production[0]].append(var[0])
                else:
                    dictionary_terminal[production[0]].append(var[0])

    # Create Dictionary For Two Variables
    dictionary_two_variables = {}
    for var in CNF.items():
        # We check if Var -> AB is a rule
        for production in var[1]:
            if(len(production) == 2):
                temp = (production[0], production[1])
                if(temp not in dictionary_two_variables.keys()):
                    dictionary_two_variables[temp] = []
                    dictionary_two_variables[temp].append(var[0])
                else:
                    dictionary_two_variables[temp].append(var[0])
    
    try:
        # Table Filling Algorithm
        # Step 1
        for i in range(len(splittedCode)):
            # For Each Variable
            for item in dictionary_terminal[splittedCode[i]]:
                Table[i][i].add(item)
        
        # Step 2
        for l in range(2, len(splittedCode) + 1):
            for i in range(len(splittedCode) - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    # For each rule A -> BC
                    for item in dictionary_two_variables.items():
                        # We check if (i , k) cell contains B and (k + 1, j) cell contains C
                        if(item[0][0] in Table[i][k] and item[0][1] in Table[k+1][j]):
                            # If so, we put A in cell (i, j) of our table
                            for var in dictionary_two_variables[item[0]]:
                                Table[i][j].add(var)

        # Step 3
        # We check if CODE is in (0, len(splittedCode) - 1)
        if "CODE" in Table[0][len(splittedCode) - 1]:
            # If so, we accept the string
            print("Accepted")
        else:
            # Else, we reject
            print("Syntax Error")

    except:
        print("Terminal not defined")