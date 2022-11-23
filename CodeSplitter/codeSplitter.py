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
        hasil_output = re.split('([(|)|;|-|+|*|/|%|!|=|<|>|&|?|~|^|0|1|2|3|4|5|6|7|8|9|:|{|}|`|\\\|"])', isi_output) # Memisahkan tanda dan angka
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
        if((outputfix[idx3]!= '_' and outputfix[idx3] != '$' and outputfix[idx3]!='a' and outputfix[idx3]!='b' and outputfix[idx3]!='c' and outputfix[idx3]!='d' and outputfix[idx3]!='e' and outputfix[idx3]!='f' and outputfix[idx3]!='g' and outputfix[idx3]!='h' and outputfix[idx3]!='i' and outputfix[idx3]!='j' and outputfix[idx3]!='k' and outputfix[idx3]!='l' and outputfix[idx3]!='m' and outputfix[idx3]!='n' and outputfix[idx3]!='n' and outputfix[idx3]!='o' and outputfix[idx3]!='p' and outputfix[idx3]!='q' and outputfix[idx3]!='r' and outputfix[idx3]!='s' and outputfix[idx3]!='t' and outputfix[idx3]!='u' and outputfix[idx3]!='v' and outputfix[idx3]!='w' and outputfix[idx3]!='x' and outputfix[idx3]!='y' and outputfix[idx3]!='z' and outputfix[idx3]!='A' and outputfix[idx3]!='B' and outputfix[idx3]!='C' and outputfix[idx3]!='D' and outputfix[idx3]!='E' and outputfix[idx3]!='F' and outputfix[idx3]!='G' and outputfix[idx3]!='H' and outputfix[idx3]!='I' and outputfix[idx3]!='J' and outputfix[idx3]!='K' and outputfix[idx3]!='L' and outputfix[idx3]!='M' and outputfix[idx3]!='N' and outputfix[idx3]!='O' and outputfix[idx3]!='P' and outputfix[idx3]!='Q' and outputfix[idx3]!='R' and outputfix[idx3]!='S' and outputfix[idx3]!='T' and outputfix[idx3]!='U' and outputfix[idx3]!='V' and outputfix[idx3]!='W' and outputfix[idx3]!='X' and outputfix[idx3]!='Y' and outputfix[idx3]!='Z' and outputfix[idx3]!='0' and outputfix[idx3]!='1' and outputfix[idx3]!='2' and outputfix[idx3]!='3' and outputfix[idx3]!='4' and outputfix[idx3]!='5' and outputfix[idx3]!='6' and outputfix[idx3]!='7' and outputfix[idx3]!='8' and outputfix[idx3]!='9') and ketemuhuruf2) :
            outputfix.pop(idx3-1)
            i3+=1
            idx3 -=1
            ketemuhuruf2 = False
            ketemuhuruf = False
        elif (outputfix[idx3]==' ' and ketemuhuruf):
            ketemuhuruf2 = True 
        elif(outputfix[idx3]==' ' and not ketemuhuruf):
            outputfix.pop(idx3)
            i3+=1
            idx3 -=1
            ketemuhuruf2 = False
            ketemuhuruf = False
        elif (outputfix[idx3]!=' ' and (outputfix[idx3]== '_' or outputfix[idx3] == '$' or outputfix[idx3]=='a' or outputfix[idx3]=='b' or outputfix[idx3]=='c' or outputfix[idx3]=='d' or outputfix[idx3]=='e' or outputfix[idx3]=='f' or outputfix[idx3]=='g' or outputfix[idx3]=='h' or outputfix[idx3]=='i' or outputfix[idx3]=='j' or outputfix[idx3]=='k' or outputfix[idx3]=='l' or outputfix[idx3]=='m' or outputfix[idx3]=='n' or outputfix[idx3]=='n' or outputfix[idx3]=='o' or outputfix[idx3]=='p' or outputfix[idx3]=='q' or outputfix[idx3]=='r' or outputfix[idx3]=='s' or outputfix[idx3]=='t' or outputfix[idx3]=='u' or outputfix[idx3]=='v' or outputfix[idx3]=='w' or outputfix[idx3]=='x' or outputfix[idx3]=='y' or outputfix[idx3]=='z' or outputfix[idx3]=='A' or outputfix[idx3]=='B' or outputfix[idx3]=='C' or outputfix[idx3]=='D' or outputfix[idx3]=='E' or outputfix[idx3]=='F' or outputfix[idx3]=='G' or outputfix[idx3]=='H' or outputfix[idx3]=='I' or outputfix[idx3]=='J' or outputfix[idx3]=='K' or outputfix[idx3]=='L' or outputfix[idx3]=='M' or outputfix[idx3]=='N' or outputfix[idx3]=='O' or outputfix[idx3]=='P' or outputfix[idx3]=='Q' or outputfix[idx3]=='R' or outputfix[idx3]=='S' or outputfix[idx3]=='T' or outputfix[idx3]=='U' or outputfix[idx3]=='V' or outputfix[idx3]=='W' or outputfix[idx3]=='X' or outputfix[idx3]=='Y' or outputfix[idx3]=='Z' or outputfix[idx3]=='0' or outputfix[idx3]=='1' or outputfix[idx3]=='2' or outputfix[idx3]=='3' or outputfix[idx3]=='4' or outputfix[idx3]=='5' or outputfix[idx3]=='6' or outputfix[idx3]=='7' or outputfix[idx3]=='8' or outputfix[idx3]=='9')):
            ketemuhuruf = True
            ketemuhuruf2 = False
        else :
            ketemuhuruf2 = False
            ketemuhuruf = False
        idx3 +=1
    # menghapus spasi antara selain huruf angka dengan huruf angka
    idx4 = 0
    ketemuhurufa = False
    ketemuhurufb = False
    for i4 in range (len(outputfix)):
        if((outputfix[idx4]=='_' or outputfix[idx4]=='$' or outputfix[idx4]=='a' or outputfix[idx4]=='b' or outputfix[idx4]=='c' or outputfix[idx4]=='d' or outputfix[idx4]=='e' or outputfix[idx4]=='f' or outputfix[idx4]=='g' or outputfix[idx4]=='h' or outputfix[idx4]=='i' or outputfix[idx4]=='j' or outputfix[idx4]=='k' or outputfix[idx4]=='l' or outputfix[idx4]=='m' or outputfix[idx4]=='n' or outputfix[idx4]=='n' or outputfix[idx4]=='o' or outputfix[idx4]=='p' or outputfix[idx4]=='q' or outputfix[idx4]=='r' or outputfix[idx4]=='s' or outputfix[idx4]=='t' or outputfix[idx4]=='u' or outputfix[idx4]=='v' or outputfix[idx4]=='w' or outputfix[idx4]=='x' or outputfix[idx4]=='y' or outputfix[idx4]=='z' or outputfix[idx4]=='A' or outputfix[idx4]=='B' or outputfix[idx4]=='C' or outputfix[idx4]=='D' or outputfix[idx4]=='E' or outputfix[idx4]=='F' or outputfix[idx4]=='G' or outputfix[idx4]=='H' or outputfix[idx4]=='I' or outputfix[idx4]=='J' or outputfix[idx4]=='K' or outputfix[idx4]=='L' or outputfix[idx4]=='M' or outputfix[idx4]=='N' or outputfix[idx4]=='O' or outputfix[idx4]=='P' or outputfix[idx4]=='Q' or outputfix[idx4]=='R' or outputfix[idx4]=='S' or outputfix[idx4]=='T' or outputfix[idx4]=='U' or outputfix[idx4]=='V' or outputfix[idx4]=='W' or outputfix[idx4]=='X' or outputfix[idx4]=='Y' or outputfix[idx4]=='Z' or outputfix[idx4]=='0' or outputfix[idx4]=='1' or outputfix[idx4]=='2' or outputfix[idx4]=='3' or outputfix[idx4]=='4' or outputfix[idx4]=='5' or outputfix[idx4]=='6' or outputfix[idx4]=='7' or outputfix[idx4]=='8' or outputfix[idx4]=='9') and ketemuhurufb) :
            outputfix.pop(idx4-1)
            i4+=1
            idx4 -=1
            ketemuhurufb = False
            ketemuhurufa = False
        elif (outputfix[idx4]==' ' and ketemuhurufa):
            ketemuhurufb = True 
        elif (outputfix[idx4]!='$' and outputfix[idx4]!='_' and outputfix[idx4]!='' and outputfix[idx4]!='a' and outputfix[idx4]!='b' and outputfix[idx4]!='c' and outputfix[idx4]!='d' and outputfix[idx4]!='e' and outputfix[idx4]!='f' and outputfix[idx4]!='g' and outputfix[idx4]!='h' and outputfix[idx4]!='i' and outputfix[idx4]!='j' and outputfix[idx4]!='k' and outputfix[idx4]!='l' and outputfix[idx4]!='m' and outputfix[idx4]!='n' and outputfix[idx4]!='n' and outputfix[idx4]!='o' and outputfix[idx4]!='p' and outputfix[idx4]!='q' and outputfix[idx4]!='r' and outputfix[idx4]!='s' and outputfix[idx4]!='t' and outputfix[idx4]!='u' and outputfix[idx4]!='v' and outputfix[idx4]!='w' and outputfix[idx4]!='x' and outputfix[idx4]!='y' and outputfix[idx4]!='z' and outputfix[idx4]!='A' and outputfix[idx4]!='B' and outputfix[idx4]!='C' and outputfix[idx4]!='D' and outputfix[idx4]!='E' and outputfix[idx4]!='F' and outputfix[idx4]!='G' and outputfix[idx4]!='H' and outputfix[idx4]!='I' and outputfix[idx4]!='J' and outputfix[idx4]!='K' and outputfix[idx4]!='L' and outputfix[idx4]!='M' and outputfix[idx4]!='N' and outputfix[idx4]!='O' and outputfix[idx4]!='P' and outputfix[idx4]!='Q' and outputfix[idx4]!='R' and outputfix[idx4]!='S' and outputfix[idx4]!='T' and outputfix[idx4]!='U' and outputfix[idx4]!='V' and outputfix[idx4]!='W' and outputfix[idx4]!='X' and outputfix[idx4]!='Y' and outputfix[idx4]!='Z' and outputfix[idx4]!='0' and outputfix[idx4]!='1' and outputfix[idx4]!='2' and outputfix[idx4]!='3' and outputfix[idx4]!='4' and outputfix[idx4]!='5' and outputfix[idx4]!='6' and outputfix[idx4]!='7' and outputfix[idx4]!='8' and outputfix[idx4]!='9'):
            ketemuhurufa = True
            ketemuhurufb = False
        else :
            ketemuhurufb = False
            ketemuhurufa = False
        idx4 +=1
    
    result = []
    check1 = False
    check2 = False
    for i in range (len(outputfix)):
        if((outputfix[i] == "/") and not check1 and not check2):
            temp = outputfix[i]
            check1 = True
            check2 = False
        elif ((outputfix[i] == "*") and not check2 and not check1):
            temp = outputfix[i]
            check2 = True
            check1 = False
        elif (check1 and (outputfix[i] == "*")):
            result.append(temp + outputfix[i])
            check1 = False
        elif (check2 and (outputfix[i] == "/")):
            result.append(temp + outputfix[i])
            check2 = False
        elif (check1 and (outputfix[i] != "*")):
            result.append(temp)
            result.append(outputfix[i])
            check1 = False
            check2 = False
        elif (check2 and (outputfix[i] != "/")):
            result.append(temp)
            result.append(outputfix[i])
            check1 = False
            check2 = False
        else:
            result.append(outputfix[i])
            check1 = False
            check2 = False

    resultbeneran = []
    fase1 = False
    fase2 = False
    for i5 in range (len(result)):
        if (not fase1 and not fase2 and result[i5]!='-' and result[i5]!='+' and result[i5]!='$' and result[i5]!='_' and result[i5]!='' and result[i5]!='a' and result[i5]!='b' and result[i5]!='c' and result[i5]!='d' and result[i5]!='e' and result[i5]!='f' and result[i5]!='g' and result[i5]!='h' and result[i5]!='i' and result[i5]!='j' and result[i5]!='k' and result[i5]!='l' and result[i5]!='m' and result[i5]!='n' and result[i5]!='n' and result[i5]!='o' and result[i5]!='p' and result[i5]!='q' and result[i5]!='r' and result[i5]!='s' and result[i5]!='t' and result[i5]!='u' and result[i5]!='v' and result[i5]!='w' and result[i5]!='x' and result[i5]!='y' and result[i5]!='z' and result[i5]!='A' and result[i5]!='B' and result[i5]!='C' and result[i5]!='D' and result[i5]!='E' and result[i5]!='F' and result[i5]!='G' and result[i5]!='H' and result[i5]!='I' and result[i5]!='J' and result[i5]!='K' and result[i5]!='L' and result[i5]!='M' and result[i5]!='N' and result[i5]!='O' and result[i5]!='P' and result[i5]!='Q' and result[i5]!='R' and result[i5]!='S' and result[i5]!='T' and result[i5]!='U' and result[i5]!='V' and result[i5]!='W' and result[i5]!='X' and result[i5]!='Y' and result[i5]!='Z' and result[i5]!='0' and result[i5]!='1' and result[i5]!='2' and result[i5]!='3' and result[i5]!='4' and result[i5]!='5' and result[i5]!='6' and result[i5]!='7' and result[i5]!='8' and result[i5]!='9' and result[i5]!='break' and result[i5]!='const' and result[i5]!='case' and result[i5]!='catch' and result[i5]!='continue' and result[i5]!='default' and result[i5]!='delete' and result[i5]!='else' and result[i5]!='false' and result[i5]!='finally' and result[i5]!='for' and result[i5]!='function' and result[i5]!='if' and result[i5]!='let' and result[i5]!='null' and result[i5]!='return' and result[i5]!='switch' and result[i5]!='throw' and result[i5]!='try' and result[i5]!='true' and result[i5]!='var' and result[i5]!='while' and result[i5]!='default') :
            resultbeneran.append(result[i5])
            fase1 = True
        elif (fase1 and result[i5]==" "):
            fase2 = True
            temp2 = result[i5]
        elif (fase2 and fase1 and (result[i5]=='+' or result[i5]=='-')):
            resultbeneran.append(result[i5])
            fase2 = False
            fase1 = False
        elif (fase2 and fase1 and not (result[i5]=='+' or result[i5]=='-') and result[i5]!='$' and result[i5]!='_' and result[i5]!='' and result[i5]!='a' and result[i5]!='b' and result[i5]!='c' and result[i5]!='d' and result[i5]!='e' and result[i5]!='f' and result[i5]!='g' and result[i5]!='h' and result[i5]!='i' and result[i5]!='j' and result[i5]!='k' and result[i5]!='l' and result[i5]!='m' and result[i5]!='n' and result[i5]!='n' and result[i5]!='o' and result[i5]!='p' and result[i5]!='q' and result[i5]!='r' and result[i5]!='s' and result[i5]!='t' and result[i5]!='u' and result[i5]!='v' and result[i5]!='w' and result[i5]!='x' and result[i5]!='y' and result[i5]!='z' and result[i5]!='A' and result[i5]!='B' and result[i5]!='C' and result[i5]!='D' and result[i5]!='E' and result[i5]!='F' and result[i5]!='G' and result[i5]!='H' and result[i5]!='I' and result[i5]!='J' and result[i5]!='K' and result[i5]!='L' and result[i5]!='M' and result[i5]!='N' and result[i5]!='O' and result[i5]!='P' and result[i5]!='Q' and result[i5]!='R' and result[i5]!='S' and result[i5]!='T' and result[i5]!='U' and result[i5]!='V' and result[i5]!='W' and result[i5]!='X' and result[i5]!='Y' and result[i5]!='Z' and result[i5]!='0' and result[i5]!='1' and result[i5]!='2' and result[i5]!='3' and result[i5]!='4' and result[i5]!='5' and result[i5]!='6' and result[i5]!='7' and result[i5]!='8' and result[i5]!='9' and result[i5]!='break' and result[i5]!='const' and result[i5]!='case' and result[i5]!='catch' and result[i5]!='continue' and result[i5]!='default' and result[i5]!='delete' and result[i5]!='else' and result[i5]!='false' and result[i5]!='finally' and result[i5]!='for' and result[i5]!='function' and result[i5]!='if' and result[i5]!='let' and result[i5]!='null' and result[i5]!='return' and result[i5]!='switch' and result[i5]!='throw' and result[i5]!='try' and result[i5]!='true' and result[i5]!='var' and result[i5]!='while' and result[i5]!='default'):
            resultbeneran.append(temp2)
            resultbeneran.append(result[i5])
            fase2 = False
        else :
            fase2 = False
            fase1 = False
            resultbeneran.append(result[i5])

    result = []
    check = False
    for i in range(len(resultbeneran)):
        if(check and resultbeneran[i] == " "):
            continue
        elif(resultbeneran[i] == "/*"):
            check = True
        elif(resultbeneran[i] == "*/"):
            check = False
        result.append(resultbeneran[i])
    
    resultbeneranbanget = []
    belom = False
    for i in range (len(result)):
        if(result[i]=='\\' and not belom):
            temp =result[i]
            belom = True
        elif ((result[i]=='"' or result[i]=="'") and belom):
            resultbeneranbanget.append(temp + result[i])
            belom = False
        else :
            resultbeneranbanget.append(result[i])
            belom = False

    return resultbeneranbanget