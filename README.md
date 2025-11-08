# Cryptography
This is one of my first project I wanted to try, after working with a simple RSA encryption algorithm as part of my workshop and assignment. In my assignment and workshop (and probably seen a lot of examples of RSA algorithms), the message $M$ is suppose to be an integer and using the RSA algorithm for encrypting the message $M$ to get a ciphertext $C$ and decrypting the cipher text $C$ to get the original message $M$. The image below shows an illustration of how RSA cryptography works and mathematically wanted to explain how the private and private keys can be generated.
![This is how person A and person B send messages to each other](https://raw.githubusercontent.com/AffePelz/Cryptography/refs/heads/main/RSA_illustration.png)
**How each party generate their private and public key?**
1. Choose two prime numbers $p$ and $q$.
2. Calculate $n = pq$ and Euler's totient function $\phi(n) = (p-1)(q-1)$.
3. Choose an integer $e$ and $d$ such that $ed = 1 (mod \phi(n))$.
4. We have our public key $(n,e)$ and private key $d$.
## **Assignment 1**
Using the RSA algorithm, my first assignment was to take a message $M$ as a `.txt` file (we call it `plaintext.txt`) and encrypt the message $M$ to a ciphertext $C$ (which will be appended in `ciphertext.txt`) using the public key $(n,e)$. With the ciphertext $C$, we also want to decrypt the ciphertext $C$ to get the original message $M$ using our private key $d$. In this assignment, we assume that person A has used our public key to send us the ciphertext $C$. More advanced, we also need to hide any information of our private key. If the private key has been compromised, then the hacker can easily obtain the original message.
## **Assignment 2**
The next assignment will be implementing a digital signature. This is to make sure to confirm the integrity of the message. More details will come later.
