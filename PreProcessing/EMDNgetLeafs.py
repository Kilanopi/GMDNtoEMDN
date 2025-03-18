inpt = open("EMDNoutput.txt","r", encoding="utf-8")
outp = open('EMDNleafs.txt', "w", encoding="utf-8")

def recme(prefix):
    leaflist=[]
    linenum=1
    inpt.seek(0)
    next=False
    for liner in inpt.readlines():
        if liner.rstrip() == "" and next:
            continue
        if liner.rstrip() == "":
            next=True
        else:
            next=False
        if linenum % 3 == 1:
            if liner.rstrip().startswith(prefix) and len(liner.rstrip()) == len(prefix) + 2:
                leaflist.append(liner.rstrip())
        linenum=linenum+1
    if len(leaflist) == 0:
        outp.write(prefix)
        outp.write("\n")
        inpt.seek(0)
        rember=False
        for thisline in inpt.readlines():
            if rember:
                outp.write(thisline.rstrip())
                rember = False
            if thisline.rstrip() == prefix:
                rember = True
        outp.write("\n")
        print(prefix)
    else:
        for leaf in leaflist:
            recme(leaf)

Singles=[]
for line in inpt.readlines():
    if len(line.rstrip()) == 1:
        Singles.append(line.rstrip())
for single in Singles:
    recme(single)