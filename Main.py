import Models.ZeroShotClassif
import Models.VagueCategorization
from transformers import pipeline
'''
WHILE NOT ALL CLASSIFIED
    take next item that is to classify
    Strong AI -> classify it by the top categories
        top three of those -> classify it by categories beneath that, take top 3 again
    ->list of 9 categories, collect all leafs under those
    (Weak AI) -> classify item to one of those leafs

'''
# declare model type and specific AI model from the Hub
strongClassifier = pipeline("zero-shot-classification", multi_label=True) #facebook bart takes long ish and seems quite accurate, but unsure
weakClassifier = pipeline("zero-shot-classification", model="cointegrated/rubert-tiny-bilingual-nli", multi_label=True)  # very fast but very all over the place responses
# classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0") #this one takes ages and has better (?) outputs
# classifier = pipeline("zero-shot-classification", model="MoritzLaurer/roberta-base-zeroshot-v2.0") #this one is fast and unsure as hell
# classifier = pipeline("zero-shot-classification", model="MoritzLaurer/bge-m3-zeroshot-v2.0") #somewhere between fast and confident

#collect GMDN Input
#TODO make this part of the whole loop for a full run
GMDNINPUT = open('output.txt', "r", encoding="utf-8")
MAPPING = open('fullmapping.txt', "w", encoding="utf-8")

i1 = 1
tempten = 70 #TODO only for testing specific GMDNs
for line in GMDNINPUT:
    if i1 % 5 == 1:
        GMDNID = line.rstrip()
    if i1 % 5 == 2:
        GMDNname = line.rstrip()
    if i1 % 5 == 3:
        GMDNdesc = line.rstrip()
    if i1 % 5 == 4:
        GMDNactv = line.rstrip()
    if i1 % tempten == 0:
        break
    i1 = i1+1

#remove these, just for testing
print(GMDNID)
print(GMDNname)
print(GMDNdesc)
print(GMDNactv)
print("")

listOfNine = Models.VagueCategorization.nineCats(strongClassifier, GMDNname, GMDNdesc)
print(listOfNine)

bestNine = []
for categ in listOfNine:
    curr = Models.ZeroShotClassif.zeroShot(strongClassifier, GMDNname, GMDNdesc, categ[1])
    print(curr)
    bestNine.append(((curr[0]+categ[0])/2 ,curr[1]))

bestNine.sort(reverse=True)
print(bestNine)
MAPPING.write(GMDNID + " " + bestNine[0][1])