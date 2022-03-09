import random

cipherText = 'bsaspp kkuosp'
Textkey = 'rsidpy dkawoa'

scheme = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
          'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,
          'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

#encrypts passed string using random key of same length
def encrypt(text = 'test'):
    key = ''
    string = ''
    while True:
        for i in range(len(text)):
            x = text[i]
            if x != ' ':
                charKey = (list(scheme.keys())[list(scheme.values()).index(random.randrange(26))])
                while charKey == x:
                    charKey = (list(scheme.keys())[list(scheme.values()).index(random.randrange(26))])
                key += charKey
                number = (scheme[x] + scheme[key[i]])%26
                string += (list(scheme.keys())[list(scheme.values()).index(number)])
            else:
                string += ' '
                key += ' '
        if string != text:
            break
    return string, key

#decrypts passed string using passed key
def decrypt(text, key = 'abcd'):
    string = ''
    for i in range(len(text)):
        x = text[i]
        if x != ' ':
            number = (scheme[x] - (scheme[key[i]]))%26
            string += (list(scheme.keys())[list(scheme.values()).index(number)])
        else:
            string += ' '
    return string    


print('Cipher Text: ' + cipherText,
      '\nKey: ' + Textkey,
      '\n\nPlain Text: ' + decrypt(cipherText, Textkey))
