from CYK import cyk as cyk
from CodeSplitter import tempCodeSplitter as cs
from CFG import GrammerReader as cfg

print("Loading...")

CNF = cfg.convertCFGtoCNY()

print("\nWelcome To Our Javascript Parser!")

file = str(input("Please Input Your File Javascript (type EXIT to exit): "))

while(file != "EXIT"):
    if (not(".js" in file)):
        file += ".js"
    try:
        output = cs.Code_splitter("./" + file)
        print(output)
        cyk.CYK(output, CNF)
    except:
        print("\nFile not found.")

    file = str(input("\nPlease Input Your File Javascript (type EXIT to exit): "))
    
print("\nThank You! Have A Nice Day :)")