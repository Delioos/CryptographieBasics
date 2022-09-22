## fonction permettant de dechiffer un message chiffré avec le chiffrement de César simple (26 lettres de l'alphabet)
## @param message le message à déchiffrer

def cesarDecrypt(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for key in range(len(alphabet)) :
        decryptedMessage = ""
        for letter in message :
            if letter in alphabet :
                decryptedMessage += alphabet[alphabet.index(letter) - key]
            else :
                decryptedMessage += letter
        print("Decrypted message with key %d : %s" % (key, decryptedMessage))

ex1 = "jwjs jsfqwbushcfwl"
#cesarDecrypt(ex1)

def vigenereDecrypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryptedMessage = ""
    for i in range(len(message)) :
        if message[i] in alphabet :
            ## vigenere crypting method
            decryptedMessage += alphabet[(alphabet.index(message[i]) - alphabet.index(key[i % len(key)])) % len(alphabet)]
        else :
            decryptedMessage += message[i]
    print("Decrypted message with key %s : %s" % (key, decryptedMessage))
    
ex2msg = "cvhnhliwmrkzs"
ex2Key = "oeuf"
vigenereDecrypt(ex2msg, ex2Key)

print("ex 4 ")

## mode 0 = chiffrement, mode 1 = dechiffrement
def affineDecrypt(message, a, b, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryptedMessage = ""
    tab = []
    for i in range(len(alphabet)-1) :
        key = i * a + (b % len(alphabet))
        tab.append([i,key])
    for letter in message :
        if letter in alphabet :
            if mode == 0 :
                decryptedMessage += alphabet[tab[alphabet.index(letter)][1]]
            else :
                decryptedMessage += alphabet[tab[alphabet.index(letter)][0]]
        else :
            decryptedMessage += letter
    print("Decrypted message with key %d, %d : %s" % (a, b, decryptedMessage))
    
ex4msg = "ihfr totjqrj"
affineDecrypt(ex4msg, 3, 7, 0)