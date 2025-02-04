from transformers import pipeline

def zeroShot(firstrun, GMDNname, GMDNdesc, EMDNprefix):
    back = ""
    #declare model type and specific AI model from the Hub
    #classifier = pipeline("zero-shot-classification") #facebook bart takes long ish and seems quite accurate, but unsure
    #classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0") #this one takes ages and has better (?) outputs
    #classifier = pipeline("zero-shot-classification", model="MoritzLaurer/roberta-base-zeroshot-v2.0") #this one is fast and unsure as hell
    #classifier = pipeline("zero-shot-classification", model="MoritzLaurer/bge-m3-zeroshot-v2.0") #somewhere between fast and confident
    classifier = pipeline("zero-shot-classification", model="cointegrated/rubert-tiny-bilingual-nli") #very fast but very all over the place responses

    #collect labels for classification
    gimmenext = False
    rember = ""
    EMDNdict = {}
    EMDNINPUT = open('EMDNoutput.txt', "r", encoding="utf-8")
    for line in EMDNINPUT:  #TODO I need to postprocess the preporcessing because sometimes theres 2 newlines (?)
        if firstrun:
            if gimmenext:
                EMDNdict[rember] = line.rstrip()
                gimmenext = False
            if len(line.rstrip()) == 1:
                gimmenext = True
                rember = line.rstrip()
        else:
            if gimmenext:
                EMDNdict[rember] = line.rstrip()
                gimmenext = False
            if line.rstrip().startswith(EMDNprefix) and len(line.rstrip()) == len(EMDNprefix)+2:
                gimmenext = True
                rember = line.rstrip()
    print(list(EMDNdict.values()))
    print("")
    if not EMDNdict.values():
        return EMDNprefix

    if firstrun:
        for name in EMDNdict.values():
            tout = classifier(GMDNname, candidate_labels=[name, "aaaaaaaaaa"])
            print(tout)

    out = classifier(GMDNname,candidate_labels=list(EMDNdict.values()))
    print(out["sequence"])
    print(out["labels"][0])
    print(out["scores"][0])
    print(out["labels"][1])
    print(out["scores"][1])
    if firstrun:
        print(out)
    for key in EMDNdict.keys():
        if EMDNdict[key] == out["labels"][0]:
            back = key
    print("")
    out = classifier(GMDNdesc,candidate_labels=list(EMDNdict.values()))
    print(out["sequence"])
    print(out["labels"][0])
    print(out["scores"][0])
    print(out["labels"][1])
    print(out["scores"][1])
    if firstrun:
        print(out)

    #TODO implement a way to weigh both description and name output for this
    #for key in EMDNdict.keys():
    #    if EMDNdict[key] == out["labels"][0]:
    #        back = key
    return back