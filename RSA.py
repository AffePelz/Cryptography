open("ciphertext.txt", "w").close()

with open("plaintext.txt", "r") as firstfile, open("ciphertext.txt", "a") as secondfile:
    for line in firstfile:
        secondfile.write(line)

def rsa_encrypt(text, e, n):
    encrypted = []
    for char in text:
        M = ord(char)
        C = pow(M, e, n)
        encrypted.append(C)
    return encrypted

# Key generator (my public key (n, e))
p = 999671
q = 999959
n = p*q
phi_n = (p-1)*(q-1)
e = 65537

# Private key
d = pow(e,-1,phi_n)

with open("ciphertext.txt", "r") as file:
    content = file.read()

encrypted_values = rsa_encrypt(content, e, n)
encrypted_string = " ".join(str(value) for value in encrypted_values)

open("ciphertext.txt", "w").close()

# Save encrypted string to a file
with open("ciphertext.txt", "w") as output_file:
    output_file.write(encrypted_string)

def rsa_decrypt(text, e=-1, n=phi_n):
    encrypted = []
    for char in text:
        M = char
        C = pow(M, e, n)
        encrypted.append(C)
    return encrypted

# Decrypt the encrypted string
encrypted_values = [int(c) for c in encrypted_string.split()]
decrypted_chars = [chr(pow(c, d, n)) for c in encrypted_values]

# Converting numbers into texts
original_message = "".join(decrypted_chars).split()
original_words =  " ".join(original_message)

print(original_words)
