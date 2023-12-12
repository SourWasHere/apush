#change variable below to change unit
import random

unit = "5"
txt = open("C:/Users/sour/OneDrive/Documents/python/apush/terms/unit" + unit + "_terms.txt", encoding="utf-8")
txtread = txt.readlines()
print(txtread[0])
txt.close()

def inlist(list, elem):
    for elem_ in list:
        if elem_ == elem:
            return True
    return False

def makedict(obj):
    dict = {"who": obj.who, "what": obj.what, "when": obj.when, "significance": obj.signif}
    return dict

def readfirst(string, num):
    read = ""
    for i in range(0,num):
         read += string[i]
    return read

def assign(list,start):
    attrlist = ["term","who","wht","whn","sgn"]
    attrdict = {"who:":1, "wht:":2, "whn:": 3, "sgn:":4}
    for i in range(0,len(attrlist)):
            key = readfirst(list[i], 4)
            attr = list[i+start].replace(key, "")
            try:
                index = attrdict[key]

            except:
                attr = list[i+start]
                index = 0

            attrlist[index] = attr.replace("\n", "")
    return attrlist

class Term(): #Term(term, who, what, when, signif)
    def __init__(self, term, who, what, when, signif):
        self.term = term #term string
        self.who = who
        self.what = what
        self.when = when
        self.signif = signif


termslist = []
atts = 5
for i in range(0, len(txtread), atts + 1):
    list = assign(txtread, i)
    termslist.append(Term(list[0], list[1], list[2], list[3], list[4]))

#game
catgs = ["who","what","when","significance"] #different qs
right = 0
qs = 10 #number of questions
for i in range(0,qs):
    choices = [] #multiple choice
    choicenum = 3
    letters = ["a", "b", "c", "d"]
    term = termslist[random.randrange(0,len(termslist))]
    catgdict = makedict(term)
    catg = catgs[random.randrange(0,len(catgs))]
    choices.append(catgdict[catg])
    termscopy = termslist.copy()
    termscopy.remove(term)
    for i in range(0,choicenum):
        inc_term = termscopy[random.randrange(0,len(termscopy))]
        termscopy.remove(inc_term) #same term doesn't get picked twice
        catgdict2 = makedict(inc_term)
        choices.append(catgdict2[catg])
    choices.remove(catgdict[catg])
    choices.insert(random.randrange(0,len(choices)), catgdict[catg]) #moves to random place
    print(term.term + "\n") #(a) 1  (b) 2  (c) 3  (d) 4
    str2 = ""
    for letter in letters:
        str2 = str2 + "(" + letter + ") " + choices[letters.index(letter)] + "\n"
    print(str2)
    while True:
        ans = input(catg + ":").lower()
        if inlist(letters, ans):
            break
        else:
            print("\ntype a, b, c, or d\n")
    ansindex = letters.index(ans)
    if choices[ansindex] == catgdict[catg]:
        print("✅")
        right += 1
    else:
        print("❌")

print(str(right) + "/" + str(qs) + " correct")


