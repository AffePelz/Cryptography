# Cryptography
After working with cryptography (in mathematics and cyber security), it got me inspired to make my own project about cryptography. Working with assignments, workshops and reading through different sources, shows that the simplest example is when the message $M$ is just an integer. That way, we can easily use mathematical algorithms for encrypting the message $M$ to get a ciphertext $C$. We can also decrypt the ciphertext $C$ to get the original message $M$. In cryptography, we have a cryptographic kes, which is used for encrypting and decrypting messages. 

# RSA Cryptosystem
Each party has a public key and a private key. If person A wants to send a message to person B, then person A has to use person B's public key to encrypt the message $M$ to a ciphertext $C$ to person B. Then, person B uses their private key to decrypt the ciphertext $C$ and read the original message $M$ and vice versa. The image below shows an illustration of how RSA cryptography works and mathematically wanted to explain how the private and private keys can be generated.
![This is how person A and person B send messages to each other](https://raw.githubusercontent.com/AffePelz/Cryptography/refs/heads/main/RSA_illustration.png)
### **How each party generate their private and public key?**
1. Choose two prime numbers $p$ and $q$.
2. Calculate $n = pq$ and Euler's totient function $\phi(n) = (p-1)(q-1)$.
3. Choose an integer $e$ and $d$ such that $ed = 1 (mod \phi(n))$.
4. We have our public key $(n,e)$ and private key $d$.
## **Assignment 1**
My first assignment will be implementing the RSA algorithm in Python. The message $M$ will be a `.txt` file (which is called `plaintext.txt`), and not an integer. The code will encrypt the `plaintext.txt` to get a ciphertext $C$ (which is called `ciphertext.txt`) and also decrypt the ciphertext $C$ to obtain the original message $M$ using our private key $d$. Additionally, we want to hide any information about our private key. If the private key has been compromised, then the hacker can easily obtain the original message.
## **Assignment 2**
The second assignment will involve digital signature. More details will come later.
