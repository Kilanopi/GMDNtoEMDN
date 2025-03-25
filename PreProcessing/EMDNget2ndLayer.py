inpt = open("PreProcessing/EMDNoutput.txt","r", encoding="utf-8")
outp = open('PreProcessing/EMDN2ndLayer.txt', "w", encoding="utf-8")
outp2 = open('PreProcessing/EMDNZ12.txt', "w", encoding="utf-8")

FirstList = []
for line in inpt.readlines():
    if len(line.rstrip()) == 1:
        FirstList.append(line.rstrip())

for cat in FirstList:
    inpt.seek(0)
    gimmenext = False
    rember = ""
    j=1
    for line in inpt:
        if gimmenext:
            outp.write(rember)
            outp.write("\n")
            outp.write(line.rstrip())
            outp.write("\n")
            gimmenext = False
        if j % 2 == 1 and line.rstrip().startswith(cat) and len(line.rstrip()) == 3:
            gimmenext = True
            rember = line.rstrip()
        j=j+1

inpt.seek(0)
gimmenext = False
rember = ""
j = 1
for line in inpt:
    if gimmenext:
        outp2.write(rember)
        outp2.write("\n")
        outp2.write(line.rstrip())
        outp2.write("\n")
        gimmenext = False
    if j % 2 == 1 and line.rstrip().startswith("Z12") and len(line.rstrip()) == 5:
        gimmenext = True
        rember = line.rstrip()
    j = j + 1