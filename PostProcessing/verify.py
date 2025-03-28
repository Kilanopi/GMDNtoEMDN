ripList = []
for i in range(13167):
    curr = "Daten/fullmapping_" + str(i+1) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    if mapping.readline() == "" or not mapping:
        ripList.append(i+1)
print(ripList)
print(len(ripList))

GMDNINPUT = open('../FP/PreProcessing/output.txt', "r", encoding="utf-8")
i1 = 1
outtxtfile = 'wrongs.txt'
MAPPING = open(outtxtfile, "w", encoding="utf-8")
for numb in ripList:
    GMDNINPUT.seek(0)
    serch = numb*3
    for line in GMDNINPUT:
        if i1 % 3 == 1:
            GMDNID = line.rstrip()
        if i1 % 3 == 2:
            GMDNname = line.rstrip()
        if i1 % 3 == 0:
            GMDNdesc = line.rstrip()
        if i1 % serch == 0:
            break
        i1 = i1+1
    MAPPING.write(GMDNID)
    MAPPING.write("\n")
    MAPPING.write(GMDNname)
    MAPPING.write("\n")
    MAPPING.write(GMDNdesc)
    MAPPING.write("\n")
    MAPPING.write("\n")