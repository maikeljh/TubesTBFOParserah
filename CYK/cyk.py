# CYK Function
def CYK(splittedCode, CNF):
    # Initialize Table For CYK
    Table = [[set([]) for i in range(len(splittedCode))] for j in range(len(splittedCode))]

    # Table Filling Algorithm
    # Step 1
    for i in range(len(splittedCode)):
        # For Each Variable
        for var in CNF.items():
            # We check if Var -> Terminal is a rule and Terminal = Wi for some i
            for production in var[1]:
                if(len(production) == 1 and production[0] == splittedCode[i]):
                    # If so, we place Var in cell (i, i) of our table
                    Table[i][i] = var[0]
    
    # Step 2
    for l in range(1, len(splittedCode)):
        for i in range(len(splittedCode) - l + 1):
            j = i + l - 1
            for k in range(i, j):
                # For each rule A -> BC
                for var in CNF.items():
                    for production in var[1]:
                        if(len(production) == 2):
                            # We check if (i , k) cell contains B and (k + 1, j) cell contains C
                            if(production[0] in Table[i][k] and production[1] in Table[k+1][j]):
                                # If so, we put A in cell (i, j) of our table
                                Table[i][j] = var[0]

    # Step 3
    # We check if CODE is in (0, len(splittedCode) - 1)
    if "CODE" in Table[0][len(splittedCode) - 1]:
        # If so, we accept the string
        print("Accepted")
    else:
        # Else, we reject
        print("Syntax Error")