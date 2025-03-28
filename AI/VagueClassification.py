def nineCats(classifier, GMDNname, GMDNdesc):
    ZndLayer = open('PreProcessing/EMDN2ndLayer.txt', "r", encoding="utf-8")
    Z12layer = open('PreProcessing/EMDNZ12.txt', "r", encoding="utf-8")
    j = 1
    catlist = []
    for line in ZndLayer:
        if j % 2 == 0:
            catlist.append(line.rstrip())
        j = j + 1
    newlist = []
    i=0
    for cat in catlist: #TODO better to split the string -> radiOTHERapy
        if "single-use" in GMDNname and "REUSABLE" in cat and not "SINGLE-USE" in cat:
            newlist.append(cat)
        elif "reusable" in GMDNname and "SINGLE-USE" in cat and not "REUSABLE" in cat:
            newlist.append(cat)
        elif "- OTHER" in cat or "- VARIOUS" in cat:
            newlist.append(cat)
        elif "IN OTHER CLASSES" in cat:
            newlist.append(cat)
        elif "NOT OTHERWISE CLASSIFIED" in cat:
            newlist.append(cat)
        elif ("reagent" not in GMDNname or "reagent" not in GMDNdesc) and "REAGENTS" in cat:
            newlist.append(cat)
        i=i+1
    for cat in newlist:
        catlist.remove(cat)
    nameTop = classifier(GMDNname, candidate_labels=catlist)
    descTop = classifier(GMDNdesc, candidate_labels=catlist)
    topList = []
    for i in range(len(nameTop["labels"])):
        topList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i]))
    topList.sort(reverse=True)
    topList = topList[0:9]
    i=0
    Z12=False
    for thing in topList:
        if thing[1] == "INSTRUMENTS FOR FUNCTIONAL EXPLORATIONS AND THERAPEUTIC INTERVENTIONS":
            topList.pop(i) #TODO find a way to look through Z12 seperately
            Z12 = True
            break
        i=i+1
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
    if not Z12:
        topList = topList[9:18]
    else:
        topList = topList[8:17]
        j = 1
        ZcatList = []
        for line in Z12layer:
            if j % 2 == 0:
                ZcatList.append(line.rstrip())
            j = j + 1
        nameTop = classifier(GMDNname, candidate_labels=ZcatList)
        descTop = classifier(GMDNdesc, candidate_labels=ZcatList)
        ZList = []
        for i in range(len(nameTop["labels"])):
            ZList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i]))
        ZList.sort(reverse=True)
        top = ZList.pop(0)
        Z12layer.seek(0)
        member = ""
        for line in Z12layer:
            if line.rstrip() == top[1]:
                top = (top[0], member)
            member = line.rstrip()
        topList.append(top)
        topList.sort(reverse=True)
    return topList