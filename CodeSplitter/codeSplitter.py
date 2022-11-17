import shlex
import re

def Read_file(inputFile) :
    f = open(inputFile, "r")
    isiFile = f.read()
    f.close()
    return isiFile

def Code_splitter(inputFile):
    #Read File
    outputfix = []
    isiFile = Read_file(inputFile)
    #Pisahin spasi yang ada di isi file
    output = shlex.split(isiFile, posix=False)
    for isi_output in  output:
        hasil_output = re.split('([(|)|;|-|+|*|/|%|!|=|<|>|&|?|~|^|0|1|2|3|4|5|6|7|8|9])', isi_output)
        for isi_hasil_output1 in hasil_output :
            if (isi_hasil_output1 != "break" and isi_hasil_output1 != 'const' and isi_hasil_output1 != 'case' and isi_hasil_output1 != 'catch' and isi_hasil_output1 != 'continue' and isi_hasil_output1 != 'default' and isi_hasil_output1 != 'delete' and isi_hasil_output1 != 'else' and isi_hasil_output1 != 'false' and isi_hasil_output1 != 'finally' and isi_hasil_output1 != "for" and isi_hasil_output1 != 'function' and isi_hasil_output1 != 'if' and isi_hasil_output1 != 'let' and isi_hasil_output1 != 'null' and isi_hasil_output1 != 'return' and isi_hasil_output1 != 'switch' and isi_hasil_output1 != 'throw' and isi_hasil_output1 != 'try' and isi_hasil_output1 != 'true' and isi_hasil_output1 != 'var' and isi_hasil_output1 != 'while' ):
                hasil_output2 = re.split('(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)', isi_hasil_output1)
                for isi_hasil_output2 in hasil_output2 :
                    if (isi_hasil_output2 !=''):
                        outputfix.append(isi_hasil_output2)
            else :
                isi_hasil_output2 = isi_hasil_output1
                if (isi_hasil_output2 !=''):
                        outputfix.append(isi_hasil_output2)
    return outputfix





