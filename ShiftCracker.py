cipherText2 = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit ghlxiwiwtxgqadds"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
freqTable = {'a':0.0817,'b':0.0150,'c':0.0278,'d':0.0425,'e':0.1270,'f':0.0223,
            'g':0.0202,'h':0.0609,'i':0.0697,'j':0.0015,'k':0.0077,'l':0.0403,
            'm':0.0241,'n':0.0675,'o':0.0751,'p':0.0193,'q':0.0010,'r':0.0599,
            's':0.0633,'t':0.0906,'u':0.0276,'v':0.0098,'w':0.0236,'x':0.0015,
            'y':0.0197,'z':0.0007}

plainText2 = ''
arr = []
common = ''
temp = 0
for x in alphabet:
	arr +=[searchText(x, cipherText2)]
for x in arr:
    if temp < x[1]:
        temp = x[1]
        common = x[0]
shift = (alphabet.index(common) - alphabet.index('e'))%len(alphabet)
for x in cipherText2:
    if(x != ' '):
        plainText2 += alphabet[alphabet.index(x)-shift]

print("\n\nCipher Text2: \n" + cipherText2,"\nPlain Text2: \n"+ plainText2) 
