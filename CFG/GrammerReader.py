import os.path

nullables = []
unitPairs = []

variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5",
"A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6", "O6", "P6", "Q6", "R6", "S6", "T6", "U6", "V6", "W6", "X6", "Y6", "Z6",
"A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "K7", "L7", "M7", "N7", "O7", "P7", "Q7", "R7", "S7", "T7", "U7", "V7", "W7", "X7", "Y7", "Z7",
"A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "K8", "L8", "M8", "N8", "O8", "P8", "Q8", "R8", "S8", "T8", "U8", "V8", "W8", "X8", "Y8", "Z8",
"A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "K9", "L9", "M9", "N9", "O9", "P9", "Q9", "R9", "S9", "T9", "U9", "V9", "W9", "X9", "Y9", "Z9",
"A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "K10", "L10", "M10", "N10", "O10", "P10", "Q10", "R10", "S10", "T10", "U10", "V10", "W10", "X10", "Y10", "Z10",
"A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11", "I11", "J11", "K11", "L11", "M11", "N11", "O11", "P11", "Q11", "R11", "S11", "T11", "U11", "V11", "W11", "X11", "Y11", "Z11",
"A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12", "I12", "J12", "K12", "L12", "M12", "N12", "O12", "P12", "Q12", "R12", "S12", "T12", "U12", "V12", "W12", "X12", "Y12", "Z12",
"A13", "B13", "C13", "D13", "E13", "F13", "G13", "H13", "I13", "J13", "K13", "L13", "M13", "N13", "O13", "P13", "Q13", "R13", "S13", "T13", "U13", "V13", "W13", "X13", "Y13", "Z13",
"A14", "B14", "C14", "D14", "E14", "F14", "G14", "H14", "I14", "J14", "K14", "L14", "M14", "N14", "O14", "P14", "Q14", "R14", "S14", "T14", "U14", "V14", "W14", "X14", "Y14", "Z14",
"A15", "B15", "C15", "D15", "E15", "F15", "G15", "H15", "I15", "J15", "K15", "L15", "M15", "N15", "O15", "P15", "Q15", "R15", "S15", "T15", "U15", "V15", "W15", "X15", "Y15", "Z15",
"A16", "B16", "C16", "D16", "E16", "F16", "G16", "H16", "I16", "J16", "K16", "L16", "M16", "N16", "O16", "P16", "Q16", "R16", "S16", "T16", "U16", "V16", "W16", "X16", "Y16", "Z16",
"A17", "B17", "C17", "D17", "E17", "F17", "G17", "H17", "I17", "J17", "K17", "L17", "M17", "N17", "O17", "P17", "Q17", "R17", "S17", "T17", "U17", "V17", "W17", "X17", "Y17", "Z17",
"A18", "B18", "C18", "D18", "E18", "F18", "G18", "H18", "I18", "J18", "K18", "L18", "M18", "N18", "O18", "P18", "Q18", "R18", "S18", "T18", "U18", "V18", "W18", "X18", "Y18", "Z18",
"A19", "B19", "C19", "D19", "E19", "F19", "G19", "H19", "I19", "J19", "K19", "L19", "M19", "N19", "O19", "P19", "Q19", "R19", "S19", "T19", "U19", "V19", "W19", "X19", "Y19", "Z19"]

def ReadGrammer(relativePath):
    try:
        path = os.path.abspath(relativePath)
        file = open(path, encoding="utf8").read()

        productions = []

        terminals = file.split("#VARIABLES\n")[0].replace("#TERMINALS\n","").replace("\n", "")
        variables = file.split("#VARIABLES\n")[1].split("#PRODUCTIONS\n")[0].replace("\n", "")
        temp = file.split("#PRODUCTIONS")[1].split("\n")
        temp.pop(0)

        for line in temp:
            head = line.split(" -> ")[0]
            bodyArr = line.split(" -> ")[1].split("  ")

            for body in bodyArr:
                productions.append((head, body.split(" ")))

        terminals = terminals.split("  ")
        variables = variables.split("  ")

        return terminals, variables, productions
    
    except:
        print("FAILED TO READ FILE")
        return [], [], []

def IsEpsilonProd(body):

    return ((len(body) == 1 and body[0] == '') or len(body) == 0)

def IsEpsilonVar(currentVar, prodsDict, variables):
    if (not(currentVar in variables)):
        return False

    prods = prodsDict[currentVar]

    return(len(prods) == 1 and IsEpsilonProd(prods[0]))

def IsNullable(currentVar, prodsDict, variables, processedVar):

    if (currentVar in processedVar):
        return False

    processedVar.append(currentVar)
    # Basis untuk nullable
    finalResult = False
    
    if (not (currentVar in variables)):
        finalResult = False

    elif (currentVar in nullables):
        finalResult = True
           
    # rekurens dan basis di dalam loop
    else:
        for body in prodsDict[currentVar]:
            
            # basis epsilon
            if (IsEpsilonProd(body)):
                nullables.append(currentVar)
                
                finalResult = True
                break

            res = True
            valid = True
            
            for symbol in body:
                if (symbol in variables):

                    if (symbol != currentVar):
                        res = res and IsNullable(symbol, prodsDict, variables, processedVar)

                        if (res and not(symbol in nullables)):
                            nullables.append(symbol)

                        elif (not res):
                            break
                    
                    else:
                        valid = False
                        continue
                else:
                    res = False
                    break
            
            if (res and valid):
                finalResult = True

            if(finalResult):
                break

    if (not(currentVar in nullables) and finalResult):
        nullables.append(currentVar)   

    processedVar.remove(currentVar)
    return finalResult

def GenerateFromNullable(body, prodsDict, variables):
    
    newBodies = []
    
    if (len(body) == 0):
        return newBodies

    symbol = body[0]

    if(len(body) > 1):
        newSubBodies = GenerateFromNullable(body[1:], prodsDict, variables)
        
    
        for newBody in newSubBodies:
            newBodies.append([symbol] + newBody)

            if (IsNullable(symbol, prodsDict, variables, [])):
                newBodies.append(newBody)
        
    else:
        newBodies = [body]

        if (IsNullable(symbol, prodsDict, variables, [])):
            newBodies.append([])

    return newBodies

def EliminateEpsilon(productions, variables):
    prodsDict = ConvertToDict(productions)
    newProds = list.copy(productions)

    for var in variables:
        for body in prodsDict[var]:
            newBodies = GenerateFromNullable(body, prodsDict, variables)
            for i in range(1, len(newBodies)):
                if(not((var, newBodies[i]) in newProds)):
                    newProds.append((var, newBodies[i]))

    newProds = [prod for prod in newProds if not(IsEpsilonProd(prod[1]))]
    for var in variables:
        if (IsEpsilonVar(var, prodsDict, variables)):
            newProds = [prod for prod in newProds if (not(var in prod[1]))]

    return newProds

def updateVariable(newProduction, variables):
    for var in variables:
        if (len([(x,y) for (x,y) in newProduction if x == var]) == 0):
            variables.remove(var)

def IsUnitBody(body, variables):
    return (len(body) == 1 and (body[0] in variables))

def IsUnitPairs(currentPair, prodsDict, variables, processedPair):

    if (currentPair in processedPair):
        return False

    processedPair.append(currentPair)
    finalResult = False

    if (currentPair in unitPairs):
        finalResult = True
    
    elif (currentPair[0] == currentPair[1]):
        finalResult = True
    
    else:
        for body in prodsDict[currentPair[0]]:
            if (IsUnitBody(body, variables)):
                res = IsUnitPairs((body[0], currentPair[1]), prodsDict, variables, processedPair)

                if (res):
                    unitPairs.append(currentPair)
                    finalResult = True
                    break

    if (not(currentPair in unitPairs) and finalResult):
        unitPairs.append(currentPair)

    processedPair.remove(currentPair)

    return finalResult

def EliminateUnit(productions, variables):
    prodsDict = ConvertToDict(productions)
    newProds = []

    for var1 in variables:
        for var2 in variables:
            if (IsUnitPairs((var1, var2), prodsDict, variables, [])):
                for body in prodsDict[var2]:
                    if((not ((var1, body) in newProds)) and (not(IsUnitBody(body, variables)))):
                        newProds.append((var1, body))

    return newProds

def isDerivateTerminal(production, variables, productions):
    for product in productions:
        if(product[0] == production):
            for item in product[1]:
                if(item not in variables):
                    return True
    
    return False


def eliminateUselessVariable(productions, variables):
    nonUselessVariables = []
    tempProds = []
    newProds = []

    # STEP 1 (Append Variables that derivate terminal)
    for var in variables:
        for production in productions:
            if(isDerivateTerminal(production[0], variables, productions)):
                if(production[0] not in nonUselessVariables):
                    nonUselessVariables.append(production[0])
    
    # STEP 2 (Append Variables that derivate non useless variable)
    for var in variables:
        for production in productions:
            if(production[0] not in nonUselessVariables):
                for item in production[1]:
                    if(item in nonUselessVariables):
                        nonUselessVariables.append(production[0])
    
    # STEP 3 (Append production which the left side is not a useless variable)
    for production in productions:
        if(production[0] in nonUselessVariables):
            tempProds.append(production)

    # STEP 4 (Pop Useless Variables on right side production)
    for production in tempProds:
        check = True
        for i in range(len(production[1])):
            if (production[1][i] in variables and production[1][i] not in nonUselessVariables):
                check = False
        if(check):
            newProds.append(production)

    return newProds

def ConvertToDict (productions):
    dictionary = {}
    for production in productions :
        if(production[0] in dictionary.keys()):
            dictionary[production[0]].append(production[1])
        else :
            dictionary[production[0]] = []
            dictionary[production[0]].append(production[1])
    return dictionary


def ConvertToCNF(productions, variables, terminals):
    newProds = []

    dictionary = {}
    for production in productions:
        if(production[0] in variables and len(production[1]) == 1):
            if(production[1][0] in terminals and production[1][0] not in dictionary.keys()):
                newVar = variablesJar.pop()
                dictionary[production[1][0]] = newVar
                newProduction = (newVar, [production[1][0]])
                newProds.append(newProduction)

    for production in productions:
        if(production[0] in variables and len(production[1]) == 1 and production not in newProds):
            newProds.append(production)
        else:
            for terminal in terminals:
                for i in range(len(production[1])):
                    if(terminal == production[1][i] and not terminal in dictionary):
                        dictionary[terminal] = variablesJar.pop()
                        newProds.append((dictionary[terminal], [terminal]))
                        production[1][i] = dictionary[terminal]
                    elif terminal == production[1][i]:
                        production[1][i] = dictionary[terminal]
            set = (production[0], production[1])
            if(set not in newProds):
                newProds.append((production[0], production[1]))

    result = []

    for production in newProds:
        panjang = len(production[1])
        if panjang <= 2:
            result.append(production)
        else :
            newVar = variablesJar.pop(0)
            variables.append(newVar+'1')
            result.append((production[0],[production[1][0]]+[newVar+'1']))
            for i in range (1,panjang-2):
                var, var2 = newVar+str(i), newVar+str(i+1)
                variables.append(var2)
                result.append((var, [production[1][i],var2]))
            result.append((newVar+str(panjang-2),production[1][panjang-2:panjang]))

    return result
    
def convertCFGtoCNY():
    terminals, variables, productions = ReadGrammer("./CFG/CFG.txt")

    for nonTerminals in variables :
        if nonTerminals in variablesJar:
            variablesJar.remove(nonTerminals)

    productionsFix = EliminateEpsilon(productions, variables)
    productionsFix = EliminateUnit(productionsFix, variables)
    productionsFix = eliminateUselessVariable(productionsFix,variables)
    productionsFix = ConvertToCNF(productionsFix, variables, terminals)
    productionsFix = ConvertToDict(productionsFix)
    return productionsFix