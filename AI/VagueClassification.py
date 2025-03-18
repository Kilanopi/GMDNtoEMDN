from transformers import pipeline
import math
def nineCats(classifier, GMDNname, GMDNdesc):
    ZndLayer = open('EMDN2ndLayer.txt', "r", encoding="utf-8")
    EMDNINPUT = open('EMDNoutput.txt', "r", encoding="utf-8")
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
            if j % 3 == 1 and line.rstrip().startswith(cat) and len(line.rstrip()) == 3:
                gimmenext = True
            j = j + 1

    nameTop = classifier(GMDNname, candidate_labels=catlist)
    descTop = classifier(GMDNdesc, candidate_labels=catlist)
    print(nameTop)
    print(descTop)
    topList = []
    for i in range(len(nameTop["labels"])):
        topList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i]))
    topList.sort(reverse=True)
    topList = topList[0:9]
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
    '''
    EMDNINPUT = open('EMDNoutput.txt', "r", encoding="utf-8")
    gimmenext = False
    rember = ""
    EMDNdict = {}
    for line in EMDNINPUT:
        if gimmenext:
            EMDNdict[rember] = line.rstrip()
            gimmenext = False
        if len(line.rstrip()) == 1:
            gimmenext = True
            rember = line.rstrip()

    nameTop = classifier(GMDNname, candidate_labels=list(EMDNdict.values()))
    descTop = classifier(GMDNdesc, candidate_labels=list(EMDNdict.values()))
    topList = []
    for i in range(len(nameTop["labels"])):
        topList.append(((nameTop["scores"][i] + descTop["scores"][i]) / 2, nameTop["labels"][i])) #= nameTop["scores"][i] + descTop["scores"][i] / 2
    topList.sort(reverse=True)
    topList = topList[0:3]

    for item in topList:
        if item[1] in EMDNdict.values():
            for stuff in EMDNdict.items():
                if item[1] == stuff[1]:
                    eurokey = stuff[0]
            topList.append((item[0],eurokey))
    topList = topList[3:6]
    i=0
    DictList = [{},{},{}]
    for key in topList:
        EMDNINPUT.seek(0)
        gimmenext = False
        rember = ""
        j=1
        for line in EMDNINPUT:
            if gimmenext:
                DictList[i][rember] = line.rstrip()
                gimmenext = False
            if j % 3 == 1 and line.rstrip().startswith(key[1]) and len(line.rstrip()) == 3:
                gimmenext = True
                rember = line.rstrip()
            j=j+1
        i=i+1
    k=0
    nineOut = []
    for dick in DictList:
        names = classifier(GMDNname, candidate_labels=list(dick.values()))
        descr = classifier(GMDNdesc, candidate_labels=list(dick.values()))
        newList = []
        for i in range(len(names["labels"])):
            newList.append((((names["scores"][i] + descr["scores"][i]) / 2 + topList[k][0]) / 2, names["labels"][i]))
        newList.sort(reverse=True)
        newList = newList[0:3]
        nineOut.extend(newList)
        k=k+1
    k=0
    topList.clear()
    for item in nineOut:
        if item[1] in DictList[math.floor(k/3)].values():
            for stuff in DictList[math.floor(k/3)].items():
                if item[1] == stuff[1]:
                    eurokey = stuff[0]
            topList.append((item[0],eurokey))
        k=k+1
    topList.sort(reverse=True)
    '''
    return topList