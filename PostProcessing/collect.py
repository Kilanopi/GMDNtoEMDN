ripList = []
for i in range(13167):
    curr = "Daten/fullmapping_" + str(i+1) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    if mapping.readline() == "" or not mapping:
        ripList.append(i+1)

curr = ""
outtxtfile = 'fullmapping.txt'
outp = open(outtxtfile, "w", encoding="utf-8")
for i in range(13167):
    if (i+1) not in ripList:
        curr = "Daten/fullmapping_" + str(i + 1) + ".txt"
        mapping = open(curr, "r", encoding="utf-8")
        mapping.seek(0)
        for line in mapping.readlines():
            outp.write(line)