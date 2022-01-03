plaintext = input("Masukkan plaintext : ") #teks yang akan diubah
key = 0x4e #jika kode hexanya huruf besar maka plaintext yang diinputkan harus huruf kecil
ciphertext = " "

for i in plaintext :
    ciphertext += chr(ord(i)^key)
print("ciphertext ddari",plaintext,"adalah: ",ciphertext)
ciphertext
