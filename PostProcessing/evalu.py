def exaczMatces(itera):
    matches=0
    matchlist = []
    handmapped = open("Input/handmapped.txt", "r", encoding="utf-8")
    curr = "SampleOutput/FullMaps/fullmapping" + str(itera) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    handmapped.seek(0)
    for line in handmapped.readlines():
        mapping.seek(0)
        hand = line.rstrip()
        handbk=hand[8:]
        handfr=hand[:5]
        for sline in mapping.readlines():
            if sline.rstrip().startswith(handfr):
                slinebk = sline.rstrip()[6:]
                if slinebk.startswith(handbk) and not handfr in matchlist:
                    matches=matches+1
                    matchlist.append(handfr)
    print(matches)
    #print(matchlist)
def catsMatces(itera):
    matches = 0
    matchlist = []
    handmapped = open("Input/handmapped.txt", "r", encoding="utf-8")
    curr = "SampleOutput/FullMaps/fullmapping" + str(itera) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    handmapped.seek(0)
    for line in handmapped.readlines():
        mapping.seek(0)
        hand = line.rstrip()
        handbk = hand[8:9]
        handfr = hand[:5]
        for sline in mapping.readlines():
            if sline.rstrip().startswith(handfr):
                slinebk = sline.rstrip()[6:]
                if slinebk.startswith(handbk) and not handfr in matchlist:
                    matches = matches + 1
                    matchlist.append(handfr)
    print(matches)
    #print(matchlist)

def grupMatces(itera):
    matches = 0
    matchlist = []
    handmapped = open("Input/handmapped.txt", "r", encoding="utf-8")
    curr = "SampleOutput/FullMaps/fullmapping" + str(itera) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    handmapped.seek(0)
    for line in handmapped.readlines():
        mapping.seek(0)
        hand = line.rstrip()
        handbk = hand[8:11]
        handfr = hand[:5]
        for sline in mapping.readlines():
            if sline.rstrip().startswith(handfr):
                slinebk = sline.rstrip()[6:]
                if slinebk.startswith(handbk) and not handfr in matchlist:
                    matches = matches + 1
                    matchlist.append(handfr)
    print(matches)
    #print(matchlist)

def preLifMatces(itera):
    matches = 0
    matchlist = []
    handmapped = open("Input/handmapped.txt", "r", encoding="utf-8")
    curr = "SampleOutput/FullMaps/fullmapping" + str(itera) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    handmapped.seek(0)
    for line in handmapped.readlines():
        mapping.seek(0)
        hand = line.rstrip()
        handbk = hand[8:-2]
        handfr = hand[:5]
        for sline in mapping.readlines():
            if sline.rstrip().startswith(handfr):
                slinebk = sline.rstrip()[6:]
                if slinebk.startswith(handbk) and not handfr in matchlist:
                    matches = matches + 1
                    matchlist.append(handfr)
    print(matches)
    #print(matchlist)

def OdirMatces(itera):
    matches = 0
    matchlist = []
    handmapped = open("Input/handmapped.txt", "r", encoding="utf-8")
    curr = "SampleOutput/FullMaps/fullmapping" + str(itera) + ".txt"
    mapping = open(curr, "r", encoding="utf-8")
    handmapped.seek(0)
    for line in handmapped.readlines():
        mapping.seek(0)
        hand = line.rstrip()
        handbk = hand[8:9]
        handfr = hand[:5]
        i=1
        for sline in mapping.readlines():
            if i%7 ==6:
                if sline.rstrip().startswith(handfr):
                    slinebk = sline.rstrip()[6:]
                    if slinebk.startswith(handbk) and not handfr in matchlist:
                        matches = matches + 1
                        matchlist.append(handfr)
            i=i+1
    print(matches)
    #print(matchlist)

for i in range(5):
    print("mapping #" + str(i+1) + "________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("category Matches:--------------------")
    catsMatces(i+1)
    print("group Matches:--------------------")
    grupMatces(i+1)
    print("PreLeaf Matches:--------------------")
    preLifMatces(i+1)
    print("exact Matches:--------------------")
    exaczMatces(i + 1)
    print("OTHERNODE Matches:--------------------")
    OdirMatces(i + 1)
