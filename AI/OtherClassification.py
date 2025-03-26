import AI.LeafClassification
def otherCat(classifier, GMDNname, GMDNdesc, ListOfNine):
    ZndLayer = open('PreProcessing/EMDN2ndLayer.txt', "r", encoding="utf-8")
    EMDNLEAFS = open('PreProcessing/EMDNleafs.txt', "r", encoding="utf-8")
    j = 1
    catlist = []
    for line in ZndLayer:
        if j % 2 == 0:
            cat= line.rstrip()
            if "- OTHER" in cat or "- VARIOUS" in cat:
                catlist.append(cat)
            elif "IN OTHER CLASSES" in cat:
                catlist.append(cat)
            elif "NOT OTHERWISE CLASSIFIED" in cat:
                catlist.append(cat)
        j = j + 1
    nameTop = classifier(GMDNname, candidate_labels=catlist)
    descTop = classifier(GMDNdesc, candidate_labels=catlist)
    topList = []
    for i in range(len(nameTop["labels"])):
        topList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i]))
    topList.sort(reverse=True)
    topList = topList[0:4]
    for thing in topList:
        ZndLayer.seek(0)
        k=1
        remember = ""
        for line in ZndLayer.readlines():
            if k % 2 == 1:
                remember = line.rstrip()
            else:
                if thing[1] == line.rstrip():
                    topList.append((thing[0], remember))
            k=k+1
    topList = topList[4:8]
    mitlist = []
    for categ in topList:
        supList = []
        EMDNLEAFS.seek(0)
        for line in EMDNLEAFS:
            if line.startswith(categ[1]) and len(line.rstrip()) == 5:
                supList.append(line.rstrip())
        if supList:
            curr = AI.LeafClassification.zeroShot(classifier, GMDNname, GMDNdesc, categ[1])
            mitlist.append(curr)
        else:
            mitlist.append(categ)
    topList.extend(mitlist)
    topList = topList[4:8]
    topList.sort(reverse=True)
    reee = topList[0]
    topList.clear()
    topList.append(reee)
    Ninelist = []
    for categ in ListOfNine:
        EMDNLEAFS.seek(0)
        gimmenext = False
        j = 1
        leafList = []
        for line in EMDNLEAFS:
            if gimmenext:
                cat = line.rstrip()
                if "- OTHER" in cat or "- VARIOUS" in cat:
                    leafList.append(cat)
                elif "IN OTHER CLASSES" in cat:
                    leafList.append(cat)
                elif "NOT OTHERWISE CLASSIFIED" in cat:
                    leafList.append(cat)
                gimmenext = False
            if j % 2 == 1 and line.rstrip().startswith(categ[1]):
                gimmenext = True
            j = j + 1
        if not leafList:
            continue
        nameTop = classifier(GMDNname, candidate_labels=leafList)
        descTop = classifier(GMDNdesc, candidate_labels=leafList)
        newList = []
        for i in range(len(nameTop["labels"])):
            newList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i]))
        newList.sort(reverse=True)
        back = newList[0]
        EMDNLEAFS.seek(0)
        remember = ""
        k = 1
        for line in EMDNLEAFS.readlines():
            if k % 2 == 1:
                remember = line.rstrip()
            else:
                if back[1] == line.rstrip():
                    back = (back[0], remember)
            k = k + 1

        Ninelist.append(back)

    Ninelist.sort(reverse=True)
    topList.append(Ninelist[0])
    topList.sort(reverse=True)
    return topList