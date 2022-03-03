cipherText1 = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi

bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx

ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr

yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk

lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi

iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m

vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd

wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr

jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii

ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh

mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb

bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd

wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr

riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""
cipherText1 = cipherText1.replace('\n',' ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
freqTable = {'a':0.0817,'b':0.0150,'c':0.0278,'d':0.0425,'e':0.1270,'f':0.0223,
            'g':0.0202,'h':0.0609,'i':0.0697,'j':0.0015,'k':0.0077,'l':0.0403,
            'm':0.0241,'n':0.0675,'o':0.0751,'p':0.0193,'q':0.0010,'r':0.0599,
            's':0.0633,'t':0.0906,'u':0.0276,'v':0.0098,'w':0.0236,'x':0.0015,
            'y':0.0197,'z':0.0007}

key = {}
arr=[]
plainText = ''
def searchText(char, text = cipherText1):
    text = text.replace(' ', '')
    count = 0
    for i in range(len(text)):
        if(text[i] == char):
            count+=1
    return [char, count/len(text)]

for x in alphabet:
	arr +=[searchText(x, cipherText1)]

def BestAorI(text = cipherText1):
    for i in range(len(text)):
        if text[i - 1] == ' ' and text[i + 1] == ' ':
             z = searchText(cipherText1[i])
             if(z[1] >= freqTable['i']+.005):
                 key[z[0]] = 'a'
             else:
                 key[z[0]] = 'i'

def BestTHE(text = cipherText1):
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-4 == lastSpace:
                possible = [text[lastSpace+1:i]]
            lastSpace = i
    count = 0
    bestThe = ''
    for x in possible:
        if text.count(x) > count:
            bestThe = x
    for i in range(len(bestThe)):
        if i == 0:
            key[bestThe[i]] = 't'
        elif i == 1:
            key[bestThe[i]] = 'h'
        else:
            key[bestThe[i]] = 'e'
def BestIS(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('i')],'i')
    temp = ''
    for i in range(len(text)):
        if text[i] == 'i' and text[i+2] == ' ' and text[i-1] == ' ':
            z = searchText(text[i])
            key[z[0]] = 's'
def BestAND(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('a')],'a')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-4 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[0] == 'a':
                    key[possible[1]] = 'n'
                    key[possible[2]]= 'd'
            lastSpace = i
def BestDO(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('d')],'d')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-3 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[0] == 'd':
                    key[possible[1]] = 'o'
            lastSpace = i
def BestOF(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('o')],'o')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-3 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[0] == 'o' and (possible[1] not in key):
                    key[possible[1]] = 'f'
            lastSpace = i
def BestBE(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('e')],'e')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-3 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[1] == 'e' and (possible[0] not in key):
                    key[possible[0]] = 'b'
            lastSpace = i
def BestTRY(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('t')],'t')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-4 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[0] == 't' and (possible[1] not in key and possible[2] not in key):
                    key[possible[1]] = 'r'
                    key[possible[2]]= 'y'
            lastSpace = i
def BestMY(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('y')],'y')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-3 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[1] == 'y' and (possible[0] not in key):
                    key[possible[0]] = 'm'
            lastSpace = i
def BestDoubles(text = cipherText1):
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            continue
        if text[i] == text[i-1]:
            possible = text[i]
            if (searchText(possible)[1]) > (freqTable['l'] - .005) and possible not in key:
                key[possible] = 'l'
            elif (searchText(possible)[1]) < (freqTable['p'] +.01) and possible not in key:
                key[possible] = 'p'
            elif possible not in key:
                key[possible] = 'c'
def BestING(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('i')],'i')
    text = text.replace(list(key.keys())[list(key.values()).index('n')],'n')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            possible = text[i-3:i+1]
            if len(possible) >= 3:
                if possible == 'in'+possible[2]+' ' and possible[2] not in key:
                    key[possible[2]] = 'g'
                    break
def BestUN(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('n')],'n')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if text[i+2] == 'n':
                possible = text[i:i+3]
                if possible[2] == 'n' and (possible[1] not in key):
                    key[possible[1]] = 'u'
                    break
def BestQU(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('u')],'u')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if text[i+2] == 'u':
                possible = text[i:i+3]
                if possible[2] == 'u' and (possible[1] not in key):
                    key[possible[1]] = 'q'
                    break
def BestX(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('e')],'e')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if text[i+1] == 'e':
                possible = text[i:i+3]
                if possible[1] == 'e' and (possible[2] not in key):
                    key[possible[2]] = 'x'
                    break
def BestK(text = cipherText1):
    arrLeft = []
    temp = ['',0]
    for x in alphabet:
        if x not in key:
            arrLeft += [searchText(x)]
    for x in arrLeft:
        if temp[1] < x[1]:
            temp = x
    key[temp[0]] = 'k'
def BestW(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('i')],'i')
    text = text.replace(list(key.keys())[list(key.values()).index('l')],'l')
    lastSpace = ''
    possible = []
    for i in range(len(text)):
        if text[i] == ' ':
            if i-5 == lastSpace:
                possible = text[lastSpace+1:i]
                if possible[1:] == 'ill' and (possible[0] not in key):
                    key[possible[0]] = 'w'
            lastSpace = i
def BestJ(text = cipherText1):
    text = text.replace(list(key.keys())[list(key.values()).index('a')],'a')
    text = text.replace(list(key.keys())[list(key.values()).index('e')],'e')
    text = text.replace(list(key.keys())[list(key.values()).index('i')],'i')
    text = text.replace(list(key.keys())[list(key.values()).index('o')],'o')
    text = text.replace(list(key.keys())[list(key.values()).index('u')],'u')
    vowels = 'aeiou'
    for i in range(len(text)):
        if text[i] == ' ':
            for x in vowels:
                if text[i+2] == x:
                    key[i+1] = 'j'
def BestV(text = cipherText1):
    arrLeft = []
    for x in alphabet:
        if x not in key:
            arrLeft += [searchText(x)]
    for x in arrLeft:
        if x[1] > freqTable['v'] - .003:
            key[x[0]] = 'v'
def BestZ(text = cipherText1):
    arrLeft = []
    temp = ['',1]
    for x in alphabet:
        if x not in key:
            arrLeft += [searchText(x)]
    for x in arrLeft:
        if temp[1] > x[1] and x[1] != 0:
            temp = x
    key[temp[0]] = 'z'

def GetKey(text = cipherText1):
    BestAorI(text)
    BestTHE(text)
    BestIS(text)
    BestAND(text)
    BestDO(text)
    BestOF(text)
    BestBE(text)
    BestTRY(text)
    BestMY(text)
    BestDoubles(text)
    BestING(text)
    BestUN(text)
    BestQU(text)
    BestX(text)
    BestK(text)
    BestW(text)
    BestV(text)
    BestJ(text)
    BestZ(text)

GetKey()
for x in cipherText1:
    try:
        plainText += key[x]
    except:
        plainText += x

print("Cipher Text: \n"+ cipherText1,
      "\n\nPlain Text: \n"+ plainText)
