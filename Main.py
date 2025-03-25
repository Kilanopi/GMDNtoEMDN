import AI.LeafClassification
import AI.VagueClassification
from transformers import pipeline

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
tempten = 42 #TODO only for testing specific GMDNs
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
    bestNine.append(curr)

bestNine.sort(reverse=True)
print(bestNine)
MAPPING.write(GMDNID + " " + bestNine[0][1])