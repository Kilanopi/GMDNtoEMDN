from transformers import pipeline

def zeroShot(classifier, GMDNname, GMDNdesc, EMDNprefix):
    back = ""
    #collect labels for classification
    EMDNINPUT = open('EMDNoutput.txt', "r", encoding="utf-8")
    EMDNLEAFS = open('EMDNleafs.txt', "r", encoding="utf-8")
    gimmenext = False
    rember = ""
    j = 1
    leafDict = {}
    for line in EMDNLEAFS:
        if gimmenext:
            leafDict[rember] = line.rstrip()
            gimmenext = False
        if j % 2 == 1 and line.rstrip().startswith(EMDNprefix):
            gimmenext = True
            rember = line.rstrip()
        j = j + 1

    names = classifier(GMDNname, candidate_labels=list(leafDict.values()))
    descr = classifier(GMDNdesc, candidate_labels=list(leafDict.values()))
    topList = []
    for i in range(len(names["labels"])):
        topList.append(((names["scores"][i] + descr["scores"][i]) / 2, names["labels"][i]))
    topList.sort(reverse=True)
    back = topList[0]
    EMDNLEAFS.seek(0)
    remember = ""
    k=0
    for line in EMDNLEAFS.readlines():
        if k % 2 == 1:
            remember = line.rstrip()
        else:
            if back[1] == line.rstrip():
                back = (back[0], remember)
        k=k+1

    return back