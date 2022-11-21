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
    newIsiFile = []
    for isi_dummy_isiFile in isiFile : #menghilangkan tab pada setiap baris
        isinyaNewIsiFile = []
        belumhuruf = False
        for isi_isi_dummy_isiFile in isi_dummy_isiFile : #cek depannya ada tab ga
            if (isi_isi_dummy_isiFile==' ' and not belumhuruf): #kalo ada tab, ganti jadi kosong
                isi_isi_dummy_isiFile = ''
            else :
                belumhuruf = True
            isinyaNewIsiFile.append(isi_isi_dummy_isiFile) #dibalikin jadi newIsiFile
        temp = ''.join(isinyaNewIsiFile)
        newIsiFile.append(temp)
    output = []
    # ilangin command
    for isi_isiFile in newIsiFile :
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
    output = re.split('(\s)', output)
    #print(output)
    output = list(output)
    spasi1 = False
    idx = 0
    idx2 = 0
    for i2 in range (len(output)) :
        if (output[idx2] == '') :
            output.pop(idx2)
            i2+=1
            idx2 -=1
        idx2+=1
    #print(output)
    for i in range (len(output)) :
        if (output[idx] == ' ' and spasi1):
            output.pop(idx)
            i+=1
            idx -=1
        elif (output[idx] == ' '):
            spasi1 = True
        else :
            spasi1 = False
        idx +=1
    for isi_output in  output:
        hasil_output = re.split('([(|)|;|-|+|*|/|%|!|=|<|>|&|?|~|^|0|1|2|3|4|5|6|7|8|9|:|{|}|`|\\\])', isi_output) # Memisahkan tanda dan angka
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
    # menghapus spasi antara any dengan selain huruf angka
    idx3 = 0
    ketemuhuruf = False
    ketemuhuruf2 = False
    for i3 in range (len(outputfix)):
        if((outputfix[idx3]!='a' and outputfix[idx3]!='b' and outputfix[idx3]!='c' and outputfix[idx3]!='d' and outputfix[idx3]!='e' and outputfix[idx3]!='f' and outputfix[idx3]!='g' and outputfix[idx3]!='h' and outputfix[idx3]!='i' and outputfix[idx3]!='j' and outputfix[idx3]!='k' and outputfix[idx3]!='l' and outputfix[idx3]!='m' and outputfix[idx3]!='n' and outputfix[idx3]!='n' and outputfix[idx3]!='o' and outputfix[idx3]!='p' and outputfix[idx3]!='q' and outputfix[idx3]!='r' and outputfix[idx3]!='s' and outputfix[idx3]!='t' and outputfix[idx3]!='u' and outputfix[idx3]!='v' and outputfix[idx3]!='w' and outputfix[idx3]!='x' and outputfix[idx3]!='y' and outputfix[idx3]!='z' and outputfix[idx3]!='A' and outputfix[idx3]!='B' and outputfix[idx3]!='C' and outputfix[idx3]!='D' and outputfix[idx3]!='E' and outputfix[idx3]!='F' and outputfix[idx3]!='G' and outputfix[idx3]!='H' and outputfix[idx3]!='I' and outputfix[idx3]!='J' and outputfix[idx3]!='K' and outputfix[idx3]!='L' and outputfix[idx3]!='M' and outputfix[idx3]!='N' and outputfix[idx3]!='O' and outputfix[idx3]!='P' and outputfix[idx3]!='Q' and outputfix[idx3]!='R' and outputfix[idx3]!='S' and outputfix[idx3]!='T' and outputfix[idx3]!='U' and outputfix[idx3]!='V' and outputfix[idx3]!='W' and outputfix[idx3]!='X' and outputfix[idx3]!='Y' and outputfix[idx3]!='Z' and outputfix[idx3]!='0' and outputfix[idx3]!='1' and outputfix[idx3]!='2' and outputfix[idx3]!='3' and outputfix[idx3]!='4' and outputfix[idx3]!='5' and outputfix[idx3]!='6' and outputfix[idx3]!='7' and outputfix[idx3]!='8' and outputfix[idx3]!='9' and outputfix[idx3]!='break' and outputfix[idx3]!='const' and outputfix[idx3]!='case' and outputfix[idx3]!='catch' and outputfix[idx3]!='continue' and outputfix[idx3]!='default' and outputfix[idx3]!='delete' and outputfix[idx3]!='else' and outputfix[idx3]!='false' and outputfix[idx3]!='finally' and outputfix[idx3]!='for' and outputfix[idx3]!='function' and outputfix[idx3]!='if' and outputfix[idx3]!='let' and outputfix[idx3]!='null' and outputfix[idx3]!='return' and outputfix[idx3]!='switch' and outputfix[idx3]!='throw' and outputfix[idx3]!='try' and outputfix[idx3]!='true' and outputfix[idx3]!='var' and outputfix[idx3]!='while' and outputfix[idx3]!='default') and ketemuhuruf2) :
            outputfix.pop(idx3-1)
            i3+=1
            idx3 -=1
            ketemuhuruf2 = False
        elif (outputfix[idx3]==' ' and ketemuhuruf):
            ketemuhuruf2 = True 
        elif (outputfix[idx3]!=' '):
            ketemuhuruf = True
            ketemuhuruf2 = False
        else :
            ketemuhuruf2 = False
            ketemuhuruf = True
        idx3 +=1

    # menghapus spasi antara selain huruf angka dengan huruf angka
    idx4 = 0
    ketemuhurufa = False
    ketemuhurufb = False
    for i4 in range (len(outputfix)):
        if((outputfix[idx4]=='a' or outputfix[idx4]=='b' or outputfix[idx4]=='c' or outputfix[idx4]=='d' or outputfix[idx4]=='e' or outputfix[idx4]=='f' or outputfix[idx4]=='g' or outputfix[idx4]=='h' or outputfix[idx4]=='i' or outputfix[idx4]=='j' or outputfix[idx4]=='k' or outputfix[idx4]=='l' or outputfix[idx4]=='m' or outputfix[idx4]=='n' or outputfix[idx4]=='n' or outputfix[idx4]=='o' or outputfix[idx4]=='p' or outputfix[idx4]=='q' or outputfix[idx4]=='r' or outputfix[idx4]=='s' or outputfix[idx4]=='t' or outputfix[idx4]=='u' or outputfix[idx4]=='v' or outputfix[idx4]=='w' or outputfix[idx4]=='x' or outputfix[idx4]=='y' or outputfix[idx4]=='z' or outputfix[idx4]=='A' or outputfix[idx4]=='B' or outputfix[idx4]=='C' or outputfix[idx4]=='D' or outputfix[idx4]=='E' or outputfix[idx4]=='F' or outputfix[idx4]=='G' or outputfix[idx4]=='H' or outputfix[idx4]=='I' or outputfix[idx4]=='J' or outputfix[idx4]=='K' or outputfix[idx4]=='L' or outputfix[idx4]=='M' or outputfix[idx4]=='N' or outputfix[idx4]=='O' or outputfix[idx4]=='P' or outputfix[idx4]=='Q' or outputfix[idx4]=='R' or outputfix[idx4]=='S' or outputfix[idx4]=='T' or outputfix[idx4]=='U' or outputfix[idx4]=='V' or outputfix[idx4]=='W' or outputfix[idx4]=='X' or outputfix[idx4]=='Y' or outputfix[idx4]=='Z' or outputfix[idx4]=='0' or outputfix[idx4]=='1' or outputfix[idx4]=='2' or outputfix[idx4]=='3' or outputfix[idx4]=='4' or outputfix[idx4]=='5' or outputfix[idx4]=='6' or outputfix[idx4]=='7' or outputfix[idx4]=='8' or outputfix[idx4]=='9' or outputfix[idx4]=='break' or outputfix[idx4]=='const' or outputfix[idx4]=='case' or outputfix[idx4]=='catch' or outputfix[idx4]=='continue' or outputfix[idx4]=='default' or outputfix[idx4]=='delete' or outputfix[idx4]=='else' or outputfix[idx4]=='false' or outputfix[idx4]=='finally' or outputfix[idx4]=='for' or outputfix[idx4]=='function' or outputfix[idx4]=='if' or outputfix[idx4]=='let' or outputfix[idx4]=='null' or outputfix[idx4]=='return' or outputfix[idx4]=='switch' or outputfix[idx4]=='throw' or outputfix[idx4]=='try' or outputfix[idx4]=='true' or outputfix[idx4]=='var' or outputfix[idx4]=='while' or outputfix[idx4]=='default' ) and ketemuhurufb) :
            outputfix.pop(idx4-1)
            i4+=1
            idx4 -=1
            ketemuhurufb = False
            ketemuhurufa = False
        elif (outputfix[idx4]==' ' and ketemuhurufa):
            ketemuhurufb = True 
        elif (outputfix[idx4]!='a' and outputfix[idx4]!='b' and outputfix[idx4]!='c' and outputfix[idx4]!='d' and outputfix[idx4]!='e' and outputfix[idx4]!='f' and outputfix[idx4]!='g' and outputfix[idx4]!='h' and outputfix[idx4]!='i' and outputfix[idx4]!='j' and outputfix[idx4]!='k' and outputfix[idx4]!='l' and outputfix[idx4]!='m' and outputfix[idx4]!='n' and outputfix[idx4]!='n' and outputfix[idx4]!='o' and outputfix[idx4]!='p' and outputfix[idx4]!='q' and outputfix[idx4]!='r' and outputfix[idx4]!='s' and outputfix[idx4]!='t' and outputfix[idx4]!='u' and outputfix[idx4]!='v' and outputfix[idx4]!='w' and outputfix[idx4]!='x' and outputfix[idx4]!='y' and outputfix[idx4]!='z' and outputfix[idx4]!='A' and outputfix[idx4]!='B' and outputfix[idx4]!='C' and outputfix[idx4]!='D' and outputfix[idx4]!='E' and outputfix[idx4]!='F' and outputfix[idx4]!='G' and outputfix[idx4]!='H' and outputfix[idx4]!='I' and outputfix[idx4]!='J' and outputfix[idx4]!='K' and outputfix[idx4]!='L' and outputfix[idx4]!='M' and outputfix[idx4]!='N' and outputfix[idx4]!='O' and outputfix[idx4]!='P' and outputfix[idx4]!='Q' and outputfix[idx4]!='R' and outputfix[idx4]!='S' and outputfix[idx4]!='T' and outputfix[idx4]!='U' and outputfix[idx4]!='V' and outputfix[idx4]!='W' and outputfix[idx4]!='X' and outputfix[idx4]!='Y' and outputfix[idx4]!='Z' and outputfix[idx4]!='0' and outputfix[idx4]!='1' and outputfix[idx4]!='2' and outputfix[idx4]!='3' and outputfix[idx4]!='4' and outputfix[idx4]!='5' and outputfix[idx4]!='6' and outputfix[idx4]!='7' and outputfix[idx4]!='8' and outputfix[idx4]!='9' and outputfix[idx4]!='break' and outputfix[idx4]!='const' and outputfix[idx4]!='case' and outputfix[idx4]!='catch' and outputfix[idx4]!='continue' and outputfix[idx4]!='default' and outputfix[idx4]!='delete' and outputfix[idx4]!='else' and outputfix[idx4]!='false' and outputfix[idx4]!='finally' and outputfix[idx4]!='for' and outputfix[idx4]!='function' and outputfix[idx4]!='if' and outputfix[idx4]!='let' and outputfix[idx4]!='null' and outputfix[idx4]!='return' and outputfix[idx4]!='switch' and outputfix[idx4]!='throw' and outputfix[idx4]!='try' and outputfix[idx4]!='true' and outputfix[idx4]!='var' and outputfix[idx4]!='while' and outputfix[idx4]!='default'):
            ketemuhurufa = True
            ketemuhurufb = False
        else :
            ketemuhurufb = False
            ketemuhurufa = False
        idx4 +=1
    return outputfix