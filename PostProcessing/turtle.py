import rdflib
def tootal(itera):
    curr = ""
    g = rdflib.Graph()
    p = rdflib.Graph()
    for i in range(13167):
        if 0 <= i < 1000:
            curr = "SampleOutput/"+ str(itera) +"/fullmapping_" + str(i + 1) + ".ttl"
            p.parse(curr, format="ttl")
            print(i+1)
            for node in p:
                g.add(node)
            print(i)
    outttlfile = 'fullmapping' + str(itera) + '_14.ttl'
    g.serialize(outttlfile, format='turtle')

def compl(itera):
    curr = ""
    g = rdflib.Graph()
    p = rdflib.Graph()
    for i in range(14):
        curr = "fullmapping" + str(itera) + "_" + str(i + 1) + ".ttl"
        p.parse(curr, format="ttl")
        print(i+1)
        for node in p:
            g.add(node)
    outttlfile = 'SampleOutput/fullmapping'+ str(itera) + '.ttl'
    g.serialize(outttlfile, format='turtle')

for i in range(5):
    compl(i+1)