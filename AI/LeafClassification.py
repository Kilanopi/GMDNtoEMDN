def zeroShot(classifier, GMDNname, GMDNdesc, EMDNprefix):
    #collect labels for classification
    EMDNLEAFS = open('PreProcessing/EMDNleafs.txt', "r", encoding="utf-8")
    gimmenext = False
    j = 1
    leafList = []
    for line in EMDNLEAFS:
        if gimmenext:
            leafList.append(line.rstrip())
            gimmenext = False
        if j % 2 == 1 and line.rstrip().startswith(EMDNprefix):
            gimmenext = True
        j = j + 1

    newlist = []
    i = 0
    for cat in leafList:  # TODO better to split the string -> radiOTHERapy
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
        i = i + 1
    for cat in newlist:
        leafList.remove(cat)
    names = classifier(GMDNname, candidate_labels=list(leafList))
    descr = classifier(GMDNdesc, candidate_labels=list(leafList))
    topList = []
    for i in range(len(names["labels"])):
        topList.append(((names["scores"][i] + descr["scores"][i]) / 2, names["labels"][i]))
    topList.sort(reverse=True)
    back = topList[0]
    EMDNLEAFS.seek(0)
    remember = ""
    k=1
    for line in EMDNLEAFS.readlines():
        if k % 2 == 1:
            remember = line.rstrip()
        else:
            if back[1] == line.rstrip():
                back = (back[0], remember)
        k=k+1

    return back