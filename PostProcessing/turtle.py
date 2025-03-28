import rdflib

curr = ""
g = rdflib.Graph()
p = rdflib.Graph()
for i in range(14):
    curr = "fullmapping" + str(i + 1) + ".ttl"
    p.parse(curr, format="ttl")
    print(i+1)
    for node in p:
        g.add(node)
outttlfile = 'fullmappingCOMPLETE.ttl'
g.serialize(outttlfile, format='turtle')
exit()
ripList = []
for i in range(13167):
    curr = "Daten/fullmapping_" + str(i+1) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    if mapping.readline() == "" or not mapping:
        ripList.append(i+1)

curr = ""
g = rdflib.Graph()
p = rdflib.Graph()
for i in range(13167):
    if 13000 <= i <= 14000:
        if (i+1) not in ripList:
            curr = "Daten/fullmapping_" + str(i + 1) + ".ttl"
            p.parse(curr, format="ttl")
            for node in p:
                g.add(node)
        print(i)
outttlfile = 'fullmapping14.ttl'
g.serialize(outttlfile, format='turtle')