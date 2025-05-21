import pandas as pd
dataframe1 = pd.read_excel('Input/EMDNV2.xlsx')
outp = open('PreProcessing/EMDNoutput.txt', "w", encoding="utf-8")
liste = dataframe1.values.tolist()
i=0
for x in liste:
    if i < 1:
        print(x)
        i=i+1
        continue
    print(str(liste[i][2]).rstrip())
    outp.write(str(liste[i][2]).rstrip())
    outp.write("\n")
    outp.write(str(liste[i][3]).rstrip())
    outp.write("\n")
    i=i+1