#We are given a flag "zolppfkdqeboryfzlktjxksyyl" and told to decrypt it. Our only hint is that
#the name of the challenge is ceasar. I attempt to solve by trying various 
#ceasar cyphers and investigating the output.

encrypted_str = "zolppfkdqeboryfzlktjxksyyl"
def ceasar(char, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[(alphabet.find(char) + offset) % 26]

for i in range(26):
    decrypted = list()
    for char in encrypted_str:
        decrypted.append(ceasar(char, i))
    print(''.join(decrypted) + "    " + str(i), '\n')

#Only sensible decrypted text was given by offset 3. Flag was
#picoCTF{crossingtherubiconwmanvbbo}
