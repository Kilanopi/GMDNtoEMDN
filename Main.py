import learningCourse.ZeroShotClassif

#collect GMDN Input
#TODO make this part of the whole loop for a full run
GMDNINPUT = open('output.txt', "r", encoding="utf-8")
i1 = 1
tempten = 120 #TODO only for testing specific GMDNs
for line in GMDNINPUT:
    if i1 % 5 == 1:
        GMDNID = line.rstrip()
    if i1 % 5 == 2:
        GMDNname = line.rstrip()
    if i1 % 5 == 3:
        GMDNdesc = line.rstrip()
    if i1 % 5 == 4:
        GMDNactv = line.rstrip()
    if i1 % tempten == 0:
        break
    i1 = i1+1

#remove these, just for testing
print(GMDNID)
print(GMDNname)
print(GMDNdesc)
print(GMDNactv)

firstclass = learningCourse.ZeroShotClassif.zeroShot(True, GMDNname, GMDNdesc, "")
print(firstclass)

newclass = ""
nfrun = False
while firstclass != newclass:
    if nfrun:
        firstclass = newclass
    newclass = learningCourse.ZeroShotClassif.zeroShot(False, GMDNname,GMDNdesc, firstclass)
    nfrun = True
    print(newclass)

print(GMDNID)
print(GMDNname)
print(GMDNdesc)
print("")
print(firstclass)