import shlex

def Read_file(inputFile) :
    f = open(inputFile, "r")
    isiFile = f.read()
    f.close()
    return isiFile

def Code_splitter(inputFile):
    #Read File
    isiFile = Read_file(inputFile)

    #Pisahin spasi yang ada di isi file
    output = shlex.split(isiFile, posix=False)
    return output
    #operator yang ada
    """operators = ['=','+','*','**','/','%','++','--','+=','-=','*=','%=','**=','==','===','!=','!==','<','>','>=','<=','?','&&','||','!','&','|','~','^','<<','>>','>>>','break','default','const','delete','case','else','catch','false','continue','finally','for','function','if','let','null','return','switch','throw','try','true','var','while']
    #split string setiap operators
    for isi_operators in operators:
        hasil_split_operators = []
        for isi_output in output :
            hasil_dummy = re.split(r'', isi_output)
            for isi_hasil_dummy in hasil_dummy :
                hasil_split_operators.append(isi_hasil_dummy)
        output = hasil_split_operators
    
    return hasil_split_operators"""





