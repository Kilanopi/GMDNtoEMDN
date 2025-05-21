ripList = []
for i in range(13167):
    curr = "SampleOutput/5/fullmapping_" + str(i+1) + ".txt" #Change the 1/ to wherever all the fullmappings are saved
    try:
        mapping = open(curr, "r", encoding="utf-8")
    except FileNotFoundError:
        ripList.append(i + 1)
        continue
    if mapping.readline() == "" or not mapping:
        ripList.append(i+1)
print(ripList)
print(len(ripList))
outtxtfile = 'wrongs.txt'
MAPPING = open(outtxtfile, "a", encoding="utf-8")
for numb in ripList:
    MAPPING.write(str(numb))
    MAPPING.write(" ")