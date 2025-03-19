from lxml import etree

outp = open('PreProcessing/output.txt', "w", encoding="utf-8")
idlist= list()
string="//*"
for j in range(182):
    file1 =  'Input/20250304/FULLDownload_Part' + str(j+1) + '_Of_188_2025-03-03.xml' #TODO change this so it works with all dates
    print(file1)
    tree = etree.parse(file1)
    elem = tree.getroot()
    para = elem.xpath(string)
    i=0
    for e in para:
        if etree.QName(e).localname=="gmdnCode":
            if e.text not in idlist:
                idlist.append(e.text)
                outp.write(e.text)
                outp.write("\n")
                i=4
        if etree.QName(e).localname=="gmdnPTName":
            if i==4:
                outp.write(e.text)
                outp.write("\n")
                i=3
        if etree.QName(e).localname=="gmdnPTDefinition":
            if i==3:
                outp.write(e.text)
                outp.write("\n")
                i=2
        if etree.QName(e).localname=="gmdnCodeStatus":
            if i==2:
                i=0