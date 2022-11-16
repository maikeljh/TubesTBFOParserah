import os.path

nullables = []
unitPairs = []

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
                res = IsUnitPairs(body[0], currentPair[1])

                if (res):
                    unitPairs.append(currentPair)
                    return True

    
    return False

def EliminateUnit(productions, variables):

    prodsDict = ConvertToDict(productions)
    newProds = []

    for var in variables:
        for var in variables:
            if (IsUnitPairs((var, var))):
                for body in prodsDict[var]:
                    if(IsUnitBody):
                        newProds.append((var, body))

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
                print(production[1])
        if(check):
            newProds.append(production)

    return newProds


def convertCFGtoCNY():
    terminal, variable, production = ReadGrammer("C:/Users/michj/Desktop/Folders/Coding/TubesTBFO/TubesTBFO/CFG/CFG.txt")