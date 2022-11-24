from CYK import cyk as cyk
from CodeSplitter import codeSplitter as cs
from CFG import GrammerReader as cfg

print("\nLoading...")

CNF = cfg.convertCFGtoCNY()

print("")
print("      _                                _       _     ____                          ")
print("     | | __ ___   ____ _ ___  ___ _ __(_)_ __ | |_  |  _ \ __ _ _ __ ___  ___ _ __ ")
print("  _  | |/ _` \ \ / / _` / __|/ __| '__| | '_ \| __| | |_) / _` | '__/ __|/ _ \ '__|")
print(" | |_| | (_| |\ V / (_| \__ \ (__| |  | | |_) | |_  |  __/ (_| | |  \__ \  __/ |   ")
print("  \___/ \__,_| \_/ \__,_|___/\___|_|  |_| .__/ \__| |_|   \__,_|_|  |___/\___|_|   ")
print("                                        |_| \n")

print("Made by:")
print("1. Michael Jonathan Halim | 13521124")
print("2. Raynard Tanadi         | 13521143")
print("3. Johanes Lee            | 13521148")

print("\nWelcome To Our Javascript Parser!\n")

file = str(input("Please Input Your File Javascript (type EXIT to exit): "))

while(file != "EXIT"):
    if (not(".js" in file)):
        file += ".js"
    try:
        output = cs.Code_splitter("./" + file)
        print(output)
        print("\nParsing...\n")
        cyk.CYK(output, CNF)
    except:
        print("\nFile not found.")

    file = str(input("\nPlease Input Your File Javascript (type EXIT to exit): "))
    
print("\nThank You! Have A Nice Day :)")