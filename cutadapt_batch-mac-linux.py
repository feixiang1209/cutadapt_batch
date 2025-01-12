import os
import easygui

choices=["Path of the DATA", "Sequence of F primer", "Sequence of R primer", "Filename of any of R1 files "]
values=easygui.multenterbox("", "",choices)



path=values[0]
Fprimer=values[1]
Rprimer=values[2]
samplename=values[3]
output=path+"/"+"cleanseqs"


try: os.system("mkdir %s" %output)
except: None



lst1=[]



if samplename[-2:] == 'gz':    

    for file in os.listdir(path):
        
        if "gz" in file:
            lst1.append(file)
elif samplename[-2:]=="tq":
    for file in os.listdir(path):
        
        if "fastq" in file:
            lst1.append(file)

n=samplename.rfind("R1")
n1=n-len(samplename)+1
#print(n1)

for file in lst1:
    
    file_name=file.split("/")[-1]
    
    if file_name[n1]=="1":



        namelog=output+"/"+file_name.split("_")[0]
        name1=file_name.split("_")[0]+"_F"
        name2=file_name.split("_")[0]+"_R"
        nameR=file_name[0:n1]+"2"+file_name[(n1+1):]
        cmd="cutadapt --minimum-length 200 -e 0.2 -g %s -G %s -o %s/%s.fastq -p %s/%s.fastq %s/%s %s/%s >%s.log" %(Fprimer,Rprimer,output,name1,output,name2,path,file_name,path,nameR,namelog)

        os.system(cmd)
        




