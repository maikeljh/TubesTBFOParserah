nullables = []
unitPairs = []

def ReadGrammer(relativePath):
    try:
        file = open(relativePath).read()

        productions = []

        terminals = file.split("#VARIABLES\n")[0].replace("#TERMINALS\n").replace("\n", "")
        variables = file.split("#VARIABLES\n")[1].split("#PRODUCTIONS\n")[0].replace("\n", "")
        temp = file.split("#PRODUCTIONS")[1].split("\n")

        for line in temp:
            head = line.split(" -> ")[0]
            bodyArr = line.split(" -> ")[1].split("  ")

            for body in bodyArr:
                productions.append((head, body.split(" ")))

        terminals = terminals.split("  ")
        variables = variables.split("  ")

        return terminals, variables, productions

    except:
        return [], [], []

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