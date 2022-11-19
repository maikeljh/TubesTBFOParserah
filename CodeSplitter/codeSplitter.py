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
    # pisahin isi_File dengan new line
    isiFile= re.split('\n',isiFile)
    output = []
    # ilangin command
    for isi_isiFile in isiFile :
        found = False
        ketemu = False
        # Cari yang ada //
        for isi_isi_isiFile in isi_isiFile :
            if(isi_isi_isiFile=='/' and not(ketemu)):
                ketemu = True
            elif (isi_isi_isiFile=='/' and ketemu):
                found = True
                ketemu = False
            else :
                ketemu = False
        if(not found): # Kalo gada //, barisnya diappend ulang
            output.append(isi_isiFile)
        else : # kalo ada //, barisnya displit lagi 
            isi_isiFile2 = re.split('(//)', isi_isiFile)
            found3 = False
            isi_isiFile2fix = []
            for isi_isi_isiFile2 in isi_isiFile2 : # Kalo ketemu //, next nya stringnya ditambah //
                if(isi_isi_isiFile2 == '//'):
                    found3 = True
                elif(found3):
                    isi_isi_isiFile2 = '//' + isi_isi_isiFile2
                isi_isiFile2fix.append(isi_isi_isiFile2)
            for isi_isi_isiFile2 in isi_isiFile2fix : # Buat semua yang ada // ga diappend, sisanya diappend
                found2 = False
                ketemu2 = False
                for isi_isi_isi_isiFile2 in isi_isi_isiFile2 :
                    if(isi_isi_isi_isiFile2=='/' and not(ketemu2)):
                        ketemu2 = True
                    elif (isi_isi_isi_isiFile2=='/' and ketemu2):
                        found2 = True
                        ketemu2 = False
                    else :
                        ketemu2 = False
                if (not found2):
                    output.append(isi_isi_isiFile2)
    # Semua output yang diappend, dijadikan 1 string lagi
    output = ''.join(output)
    #ini misahin spasi
    output = shlex.split(output, posix=False)
    for isi_output in  output:
        hasil_output = re.split('([(|)|;|-|+|*|/|%|!|=|<|>|&|?|~|^|0|1|2|3|4|5|6|7|8|9|:|{|}])', isi_output) # Memisahkan tanda dan angka
        for isi_hasil_output1 in hasil_output : #memisahkan huruf jika tidak termasuk fungsi
            if (isi_hasil_output1 != "break" and isi_hasil_output1 != 'const' and isi_hasil_output1 != 'case' and isi_hasil_output1 != 'catch' and isi_hasil_output1 != 'continue' and isi_hasil_output1 != 'default' and isi_hasil_output1 != 'delete' and isi_hasil_output1 != 'else' and isi_hasil_output1 != 'false' and isi_hasil_output1 != 'finally' and isi_hasil_output1 != "for" and isi_hasil_output1 != 'function' and isi_hasil_output1 != 'if' and isi_hasil_output1 != 'let' and isi_hasil_output1 != 'null' and isi_hasil_output1 != 'return' and isi_hasil_output1 != 'switch' and isi_hasil_output1 != 'throw' and isi_hasil_output1 != 'try' and isi_hasil_output1 != 'true' and isi_hasil_output1 != 'var' and isi_hasil_output1 != 'while' and isi_hasil_output1!='default' ):
                hasil_output2 = re.split('(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)', isi_hasil_output1)
                for isi_hasil_output2 in hasil_output2 :
                    if (isi_hasil_output2 !=''):
                        outputfix.append(isi_hasil_output2)
            else :
                isi_hasil_output2 = isi_hasil_output1
                if (isi_hasil_output2 !=''):
                        outputfix.append(isi_hasil_output2)
    return outputfix