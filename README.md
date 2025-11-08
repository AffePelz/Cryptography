# Cryptography
This is one of my first project I wanted to try, after working with a simple RSA encryption algorithm as part of my workshop and assignment. The simplest example is when the message $M$ is just an integer and we can use the RSA algorithm for encrypting the message $M$ to get a ciphertext $C$. We can also decrypt the ciphertext $C$ to get the original message $M$. Each party has a public key and a private key. If person A wants to send a message to person B, then person A has to use person B's public key to encrypt the message $M$ to a ciphertext $C$ to person B. Then, person B uses their private key to decrypt the ciphertext $C$ and read the original message $M$ and vice versa. The image below shows an illustration of how RSA cryptography works and mathematically wanted to explain how the private and private keys can be generated.
![This is how person A and person B send messages to each other](https://raw.githubusercontent.com/AffePelz/Cryptography/refs/heads/main/RSA_illustration.png)
### **How each party generate their private and public key?**
1. Choose two prime numbers $p$ and $q$.
2. Calculate $n = pq$ and Euler's totient function $\phi(n) = (p-1)(q-1)$.
3. Choose an integer $e$ and $d$ such that $ed = 1 (mod \phi(n))$.
4. We have our public key $(n,e)$ and private key $d$.
## **Assignment 1**
For my first assignment, I need to implement the RSA algorithm in Python. The message $M$ will be a `.txt` file (which is called `plaintext.txt`), and not an integer. In this assignment, we want to encrypt the `plaintext.txt` to get a ciphertext $C$ (which is called `ciphertext.txt`). We also want to decrypt the ciphertext $C$ to obtain the original message $M$ using our private key $d$. Additionally, we want to hide any information about our private key. If the private key has been compromised, then the hacker can easily obtain the original message.
## **Assignment 2**
The next assignment will be implementing a digital signature. This is to make sure to confirm the integrity of the message. More details will come later.
