import os.path

nullables = []
unitPairs = []

variablesJar = []

for i in range(1,10):
    for k in range(26):
        newJar = chr(65 + k) + str(i)
        variablesJar.append(newJar)
        
for i in range(1,10):
    for j in range(10):
        for k in range(26):
            newJar = chr(65 + k) + str(i) + str(j)
            variablesJar.append(newJar)

for i in range(1,10):
    for j in range(10):
        for l in range(10):
            for k in range(26):
                newJar = chr(65 + k) + str(i) + str(j) + str(l)
                variablesJar.append(newJar)
        
def ReadGrammer(relativePath):
    try:
        path = os.path.abspath(relativePath)
        file = open(path, encoding="utf8").read()

        productions = []

        terminals = file.split("#VARIABLES\n")[0].replace("#TERMINALS\n","").replace("\n", "")
        variables = file.split("#VARIABLES\n")[1].split("#PRODUCTIONS\n")[0].replace("\n", "")
        temp = file.split("#PRODUCTIONS")[1].split("\n")
        temp.pop(0)

        productions.append(("BLANK", [' ']))

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
    if (not(currentVar in variables) or not(currentVar in prodsDict.keys())):
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
    elif (currentVar in prodsDict.keys()):
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
        if (var in prodsDict.keys()):
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
    
    elif (currentPair[0] in prodsDict):
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

    # Create Production For Each Terminal that Exist in Productions (for example: D -> a)
    for production in productions:
        if(production[0] in variables and len(production[1]) == 1):
            if(production[1][0] in terminals and production[1][0] not in dictionary.keys()):
                newVar = variablesJar.pop()
                dictionary[production[1][0]] = newVar
                newProduction = (newVar, [production[1][0]])
                newProds.append(newProduction)
    
    # Append Production in form of (B -> b) or (from A -> aAa to D -> a and A -> DAD)
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

    # Changing Production from A -> DAD to A -> XD and X -> DA
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
    terminals, variables, productions = ReadGrammer("./CFG/TEST1.txt")
    for nonTerminals in variables :
        if nonTerminals in variablesJar:
            variablesJar.remove(nonTerminals)
    productionsFix = EliminateEpsilon(productions, variables)
    productionsFix = EliminateUnit(productionsFix, variables)
    productionsFix = eliminateUselessVariable(productionsFix,variables)
    productionsFix = ConvertToCNF(productionsFix, variables, terminals)
    productionsFix = ConvertToDict(productionsFix)
    print(productionsFix)
    return productionsFix