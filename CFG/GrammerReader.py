import os.path

nullables = []
unitPairs = []

variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5"]

def ReadGrammer(relativePath):
    file = open(relativePath, encoding="utf8").read()

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

def IsEpsilonProd(body):
    return (len(body) == 1 and body[0] == "")

def IsNullable(currentVar, prodsDict, variables):

    # Basis untuk nullable
    if (currentVar in nullables):
        return True

    elif (IsEpsilonProd(prodsDict[currentVar])):
        nullables.append(currentVar)
        return True
    
    # rekurens dan basis di dalam loop
    else:
        for body in prodsDict[currentVar]:
            res = True

            for symbol in body:
                if (symbol in variables):
                    res = res and IsNullable(symbol, prodsDict, variables)

                    if (res):
                        nullables.append(currentVar)

                    else:
                        break

                else:
                    res = False
                    break
            
            if (res):
                return True
    
    return False

def GenerateFromNullable(body):
    newBodies = []
    for symbol in body:

        newSubBodies = GenerateFromNullable(body[1:])
        for newBody in newSubBodies:
            newBodies.append([symbol + newBody])

            if (IsNullable(symbol)):
                newBodies.append(newBody)

    return newBodies

def EliminateElipson(productions, variables):
    prodsDict = ConvertToDict(productions)
    newProds = list.copy(productions)

    for var in variables:
        for body in prodsDict[var]:
            newBodies = GenerateFromNullable(body)

            for i in range(1, len(newBodies)):
                newProds.append((var, newBodies[i]))

    for prod in productions:
        if (IsEpsilonProd(prod[1])):
            newProds.remove(prod)
    
    return newProds


def IsUnitBody(body, variables):
    return (len(body) == 1 and (body[0] in variables))

def IsUnitPairs(currentPair, prodsDict, variables):
    if (currentPair in unitPairs):
        return True
    
    elif (currentPair[0] == currentPair[1]):
        unitPairs.append(currentPair)
        return True
    
    else:
        for body in prodsDict[currentPair[0]]:
            if (IsUnitBody(body, variables)):
                res = IsUnitPairs((body[0], currentPair[1]), prodsDict, variables)

                if (res):
                    unitPairs.append(currentPair)
                    return True
                else:
                    return False

    
    return False

def EliminateUnit(productions, variables):
    prodsDict = ConvertToDict(productions)
    newProds = []

    for var1 in variables:
        for var2 in variables:
            if (IsUnitPairs((var1, var2), prodsDict, variables)):
                for body in prodsDict[var1]:
                    if(IsUnitBody(body, variables)):
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


def eliminate_terakhir(productions):#ini blm ya
    return productions

def convertCFGtoCNY():
    terminals, variables, productions = ReadGrammer("C:/Users/michj/Desktop/Folders/Coding/TubesTBFO/TubesTBFO/CFG/CFG.txt")
    for nonTerminals in variables :
        if nonTerminals in variablesJar:
            variablesJar.remove(nonTerminals)
    productionsFix = EliminateElipson(productions, variables)
    productionsFix = EliminateUnit(productionsFix, variables)
    productionsFix = eliminateUselessVariable(productionsFix,variables)
    productionsFix = eliminate_terakhir(productionsFix)
    productionsFix = ConvertToDict(productionsFix)
    return productionsFix

fix = convertCFGtoCNY()