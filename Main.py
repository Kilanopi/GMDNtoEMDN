import AI.LeafClassification
import AI.VagueClassification
import AI.OtherClassification
from transformers import pipeline
import rdflib

g = rdflib.Graph()
# declare model type and specific AI model from the Hub
strongClassifier = pipeline("zero-shot-classification", multi_label=True) #facebook bart takes long ish and seems quite accurate, but unsure
weakClassifier = pipeline("zero-shot-classification", model="cointegrated/rubert-tiny-bilingual-nli", multi_label=True)  # very fast but very all over the place responses
# classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0") #this one takes ages and has better (?) outputs
# classifier = pipeline("zero-shot-classification", model="MoritzLaurer/roberta-base-zeroshot-v2.0") #this one is fast and unsure as hell
# classifier = pipeline("zero-shot-classification", model="MoritzLaurer/bge-m3-zeroshot-v2.0") #somewhere between fast and confident

#collect GMDN Input
#TODO make this part of the whole loop for a full run
GMDNINPUT = open('PreProcessing/output.txt', "r", encoding="utf-8")
MAPPING = open('fullmapping.txt', "w", encoding="utf-8")

i1 = 1
tempten = 8421 #TODO only for testing specific GMDNs
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

#AI.OtherClassification.otherCat(strongClassifier, GMDNname, GMDNdesc, [(0.8065924644470215, 'L24'), (0.7723210155963898, 'L03'), (0.6678230166435242, 'L01'), (0.6496760547161102, 'L04'), (0.6374847888946533, 'V04'), (0.6147002577781677, 'X02'), (0.583263486623764, 'M02'), (0.5182857662439346, 'T03'), (0.504276692867279, 'Z1290')])
#exit()

listOfNine = AI.VagueClassification.nineCats(strongClassifier, GMDNname, GMDNdesc)
print(listOfNine)

bestNine = []
for categ in listOfNine:
    curr = AI.LeafClassification.zeroShot(strongClassifier, GMDNname, GMDNdesc, categ[1])
    print(curr)
    bestNine.append(curr)

bestNine.sort(reverse=True)
print(bestNine)

for i in range(4):
    g.add((rdflib.URIRef("http://example.org/" + GMDNID.rstrip()), rdflib.URIRef("http://example.org/" + bestNine[i][1]), rdflib.Literal(bestNine[i][0])))
    MAPPING.write(GMDNID.rstrip() + " " + bestNine[i][1] + " " + str(bestNine[i][0]))
    MAPPING.write("\n")


otherTwo = AI.OtherClassification.otherCat(strongClassifier, GMDNname, GMDNdesc,listOfNine)
for i in range(2):
    g.add((rdflib.URIRef("http://example.org/" + GMDNID.rstrip()), rdflib.URIRef("http://example.org/" + otherTwo[i][1]), rdflib.Literal(otherTwo[i][0])))
    MAPPING.write(GMDNID.rstrip() + " " + otherTwo[i][1] + " " + str(otherTwo[i][0]))
    MAPPING.write("\n")
MAPPING.write("\n")

g.serialize('fullmapping.ttl',format='turtle')