inpt = open("EMDNoutput.txt","r", encoding="utf-8")
outp = open('EMDN2ndLayer.txt', "w", encoding="utf-8")


#def ZndLayer():
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
            #print(rember)
            outp.write("\n")
            gimmenext = False
        if j % 3 == 1 and line.rstrip().startswith(cat) and len(line.rstrip()) == 3:
            gimmenext = True
            rember = line.rstrip()
        j=j+1