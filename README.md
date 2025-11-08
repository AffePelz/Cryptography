# Cryptography
This is one of my first project I wanted to try, after working with a simple RSA encryption algorithm as part of my workshop and assignment. In my assignment and workshop (and probably seen a lot of examples of RSA algorithms), the message _M_ is suppose to be an integer and using the RSA algorithm for encrypting the message _M_ to get a ciphertext _C_ and decrypting the cipher text _C_ to get the original message _M_. The image below shows an illustration of how RSA cryptography works and mathematically wanted to explain how the private and private keys can be generated.
![This is how person A and person B send messages to each other](https://raw.githubusercontent.com/AffePelz/Cryptography/refs/heads/main/RSA_illustration.png)
1. Choose two prime numbers $p$ and $q$.
2. Calculate $n = pq$ and Euler's totient function $\phi(n) = (p-1)(q-1)$.
## **Assignment 1**
Using the RSA algorithm, I wanted my message _M_ to be a `.txt` file. Using the RSA encryption algorithm on message _M_, we will get a cipher text in `.txt` file.  
