from homomorphicencryption import *

# Scheme's parameters
# polynomial modulus degree
n = 2**4
# ciphertext modulus
q = 2**15
# plaintext modulus
t = 2**8
# polynomial modulus
poly_mod = np.array([1] + [0] * (n - 1) + [1])

# key generation

pk, sk = keygen(n, q, poly_mod)

#print("Public key: ", pk)
#print("Secret key: ", sk)

# encryption
pt1, pt2 = 73, 20
cst1, cst2 = 69, 5 

# using the private key, polynomial modulus, cyphertext mudulus and plaintext modulus to encrypt the plaintext
# returns a tuple of two encrypted polynomials, ct0 for polyadd and ct1 for polymul??? This is the tuple for the ciphertext
ct1 = encrypt(pk, n, q, t, poly_mod, pt1)  
ct2 = encrypt(pk, n, q, t, poly_mod, pt2)

print("[+] Ciphertext ct1({}):".format(pt1))
print("")
print("\t ct1_0:", ct1[0])
print("\t ct1_1:", ct1[1])
print("")
print("[+] Ciphertext ct2({}):".format(pt2))
print("")
print("\t ct1_0:", ct2[0])
print("\t ct1_1:", ct2[1])
print("")

# Evaluation
ct3 = add_plain(ct1, cst1, q, t, poly_mod) # adds plaintext 69 to the encrypted plaintext 73 (cyphertext cst1)
ct4 = mul_plain(ct2, cst2, q, t, poly_mod) # multiplies plaintext 5 to the encrypted plaintext 20 (cyphertext cst2)

print("[+] Ciphertext ct3({}):".format(pt1))
print("")
print("\t ct3_0:", ct3[0])
print("\t ct3_1:", ct3[1])
print("")
print("[+] Ciphertext ct4({}):".format(pt2))
print("")
print("\t ct4_0:", ct4[0])
print("\t ct4_1:", ct4[1])
print("")


# Decryption
decrypted_ct3 = decrypt(sk, n, q, t, poly_mod, ct3)
decrypted_ct4 = decrypt(sk, n, q, t, poly_mod, ct4)

print("[+] Decrypted ct3(ct1 + {}): {}".format(cst1, decrypted_ct3))
print("[+] Decrypted ct4(ct2 * {}): {}".format(cst2, decrypted_ct4))