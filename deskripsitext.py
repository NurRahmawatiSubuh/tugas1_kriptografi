ciphertext = input("Masukkan Ciphertext : ") 
key = 0x4e
plaintext = " "

for i in ciphertext :
    plaintext += chr(ord(i)^key)
print("plaintext ddari",ciphertext,"adalah: ",plaintext)
plaintext
