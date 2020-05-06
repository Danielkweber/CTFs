#The challenge asks for implementation of a simple ceasar cypher known as rot13 
#which rotates every letter 13 places forward.

#The given flag is cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

alpha = "abcdefghijklmnopqrstuvwxyz"
def rot13(char):
    return alpha[(alpha.find(char) + 13) % len(alpha)]

encrypted_string = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

decrypted_string = list()
for char in encrypted_string:
    if char in alpha:
        decrypted_string.append(rot13(char))
    else:
        decrypted_string.append(char)
print(''.join(decrypted_string))
#The flag was picoCTF{not_too_bad_of_a_problem}