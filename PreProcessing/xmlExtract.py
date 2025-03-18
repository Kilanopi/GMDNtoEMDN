from lxml import etree

outp = open('output.txt', "w", encoding="utf-8")
#etree.register_namespace("gudid", "http://www.fda.gov/cdrh/gudid/gudid.xsd")
idlist= list()
string="//*"
for j in range(182):
    file1 =  'gmdn/FULLDownload_Part' + str(j+1) + '_Of_182_2024-10-01.xml'
    print(file1)
    tree = etree.parse(file1)
    #outp.write("xxfile " + str(j+1) + "\n")
    elem = tree.getroot()
    para = elem.xpath(string)
    i=0
    for e in para:
        if etree.QName(e).localname=="gmdnCode":
            if e.text not in idlist:
                idlist.append(e.text)
                #print(e.text)
                outp.write(e.text)
                outp.write("\n")
                i=4
        if etree.QName(e).localname=="gmdnPTName":
            if i==4:
                #print(e.text)
                outp.write(e.text)
                outp.write("\n")
                i=3
        if etree.QName(e).localname=="gmdnPTDefinition":
            if i==3:
                #print(e.text)
                outp.write(e.text)
                outp.write("\n")
                i=2
        if etree.QName(e).localname=="gmdnCodeStatus":
            if i==2:
                #print(e.text)
                outp.write(e.text)
                outp.write("\n")
                outp.write("\n")
                i=0