from transformers import pipeline
import math
def nineCats(classifier, GMDNname, GMDNdesc):
    ZndLayer = open('PreProcessing/EMDN2ndLayer.txt', "r", encoding="utf-8")
    EMDNINPUT = open('PreProcessing/EMDNoutput.txt', "r", encoding="utf-8")
    prelist = []
    for line in ZndLayer.readlines():
        prelist.append(line.rstrip())
    catlist = []
    for cat in prelist:
        EMDNINPUT.seek(0)
        gimmenext = False
        j = 1
        for line in EMDNINPUT:
            if gimmenext:
                catlist.append(line.rstrip())
                gimmenext = False
            if j % 2 == 1 and line.rstrip().startswith(cat) and len(line.rstrip()) == 3:
                gimmenext = True
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
        if cat in catlist:
            catlist.remove(cat)


    nameTop = classifier(GMDNname, candidate_labels=catlist)
    descTop = classifier(GMDNdesc, candidate_labels=catlist)
    topList = []
    for i in range(len(nameTop["labels"])):
        topList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i]))
    topList.sort(reverse=True)
    topList = topList[0:9]
    #i=0
    #for thing in topList:
    #    if thing[1] == "INSTRUMENTS FOR FUNCTIONAL EXPLORATIONS AND THERAPEUTIC INTERVENTIONS":
    #        topList.remove(i) #TODO find a way to look through Z12 seperately
    #    i=i+1

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
    topList = topList[9:18]
    return topList