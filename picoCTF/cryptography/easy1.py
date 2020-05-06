#We are given the encrypted flag UFJKXQZQUNB and a key SOLVECRYPTO
#We are also given a cipher table to use to decrypt the message
#Quick inspection of the table reveals that the cipher takes the letter
#of the encrypted string and rotates it by the int value of the key
#letter (given by position in alphabet)

encrypted_message = "UFJKXQZQUNB"
key = "SOLVECRYPTO"
def cipher_table(encrypt_letter, key_letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypt_index = alphabet.find(encrypt_letter)
    key_index = alphabet.find(key_letter)
    return alphabet[(encrypt_index - key_index) % 26]

flag = list()
for i in range(len(encrypted_message)):
    flag.append(cipher_table(encrypted_message[i], key[i]))
print(''.join(flag))
#flag was picoCTF{CRYPTOISFUN}