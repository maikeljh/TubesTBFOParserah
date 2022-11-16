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
        hasil_output = re.split('([(|)|;])', isi_output)
        for isi_hasil_output in hasil_output :
            if (isi_hasil_output !=''):
                outputfix.append(isi_hasil_output)
    return outputfix





