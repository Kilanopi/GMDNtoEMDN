import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('2021-09-29_ EMDN_EUDAMED + DYNA_v1.1.xlsx')

#inpt1 = open('EMDNcode.txt', "r", encoding="utf-8")
#inpt2 = open('EMDNdescr.txt', "r", encoding="utf-8")
outp = open('EMDNoutput.txt', "w", encoding="utf-8")
#lines1=inpt1.readlines()
#lines2=inpt2.readlines()
liste = dataframe1.values.tolist()
i=0
g=12.0

for x in liste:
    if str(liste[i][2]) != "nan":
        outp.write(str(liste[i][2]))
        outp.write("\n")
    if str(liste[i][11]) != "nan":
        outp.write(str(liste[i][11]))
        outp.write("\n")
        outp.write("\n")
        i=i+1