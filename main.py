from CYK import cyk as cyk
from CodeSplitter import codeSplitter as cs
from CFG import GrammerReader as cfg

CNF = cfg.convertCFGtoCNY()
for item in CNF.items():
    print(item)
output = cs.Code_splitter("./test.js")
print(output)
cyk.CYK(output, CNF)