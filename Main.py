import AI.LeafClassification
import AI.VagueClassification
import AI.OtherClassification
from transformers import pipeline
import rdflib
import sys

def mapAI(n):
    g = rdflib.Graph()
    itonum = int(n)/3
    # declare model type and specific AI model from the Hub
    strongClassifier = pipeline("zero-shot-classification", multi_label=True) #facebook bart takes long ish and seems quite accurate, but unsure
    #weakClassifier = pipeline("zero-shot-classification", model="cointegrated/rubert-tiny-bilingual-nli", multi_label=True)  # very fast but very all over the place responses
    #strongClassifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0") #this one takes ages and has better (?) outputs
    #classifier = pipeline("zero-shot-classification", model="MoritzLaurer/roberta-base-zeroshot-v2.0") #this one is fast and unsure as hell
    #classifier = pipeline("zero-shot-classification", model="MoritzLaurer/bge-m3-zeroshot-v2.0") #somewhere between fast and confident

    #collect GMDN Input
    GMDNINPUT = open('PreProcessing/output.txt', "r", encoding="utf-8")
    i1 = 1
    tempten = int(n)
    for line in GMDNINPUT:
        if i1 % 3 == 1:
            GMDNID = line.rstrip()
        if i1 % 3 == 2:
            GMDNname = line.rstrip()
        if i1 % 3 == 0:
            GMDNdesc = line.rstrip()
        if i1 % tempten == 0:
            break
        i1 = i1+1

    #remove these, just for testing
    print(GMDNID)
    print(GMDNname)
    print(GMDNdesc)
    print("")

    listOfNine = AI.VagueClassification.nineCats(strongClassifier, GMDNname, GMDNdesc)
    print(listOfNine)

    bestNine = []
    for categ in listOfNine:
        curr = AI.LeafClassification.zeroShot(strongClassifier, GMDNname, GMDNdesc, categ[1])
        print(curr)
        if curr == categ[1]:
            bestNine.append(categ)
        else:
            bestNine.append(curr)

    bestNine.sort(reverse=True)
    print(bestNine)

    otherTwo = AI.OtherClassification.otherCat(strongClassifier, GMDNname, GMDNdesc, listOfNine)
    print(otherTwo)

    outtxtfile = 'fullmapping_' + str(int(itonum)) + '.txt'
    MAPPING = open(outtxtfile, "w", encoding="utf-8")
    for i in range(4):
        g.add((rdflib.URIRef("http://example.org/" + GMDNID.rstrip()), rdflib.URIRef("http://example.org/" + bestNine[i][1]), rdflib.Literal(bestNine[i][0])))
        MAPPING.write(GMDNID.rstrip() + " " + bestNine[i][1] + " " + str(bestNine[i][0]))
        MAPPING.write("\n")

    for i in range(2):
        g.add((rdflib.URIRef("http://example.org/" + GMDNID.rstrip()), rdflib.URIRef("http://example.org/" + otherTwo[i][1]), rdflib.Literal(otherTwo[i][0])))
        MAPPING.write(GMDNID.rstrip() + " " + otherTwo[i][1] + " " + str(otherTwo[i][0]))
        MAPPING.write("\n")
    MAPPING.write("\n")
    outttlfile = 'fullmapping_' + str(int(itonum)) + '.ttl'
    g.serialize(outttlfile,format='turtle')

if __name__ == "__main__":
  nu = sys.argv[1]
  mapAI(nu)