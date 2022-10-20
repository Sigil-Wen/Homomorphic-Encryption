# analyzing results

# Scheme's parameters
    # polynomial modulus degree
    n = 2 ** 2
    # ciphertext modulus
    q = 2 ** 14
    # plaintext modulus
    t = 2
    # base for relin_v1
    T = int(np.sqrt(q)) 
    #modulusswitching modulus
    p = q ** 3

    # polynomial modulus
    poly_mod = np.array([1] + [0] * (n - 1) + [1]) = [1 0 0 0 1]
[+] Ciphertext ct1([1, 0, 1, 1]):

         ct1_0: [16357  7851  4343  4196]
         ct1_1: [12297  4079 11931  8083]

[+] Ciphertext ct2([1, 1, 0, 1]):

         ct1_0: [ 634 3995 3368 9342]
         ct1_1: [ 3617 12445  8249 11617]

[+] Decrypted ct3=(ct1 + [0, 1, 1, 0]): [1 1 0 1]
[+] Decrypted ct4=(ct2 * [0, 1, 0, 0]): [1 1 1]
[+] Decrypted ct5=(ct1 + [0, 1, 1, 0] + [0, 1, 0, 0] * ct2): [0 0 1 1]
[+] pt1 + [0, 1, 1, 0] + [0, 1, 0, 0] * pt2): [0 0 1 1]
[+] Decrypted ct6=(ct1 * ct2): [0 0 0 1]
[+] Decrypted ct7=(ct1 * ct2): [0 0 0 1]
[+] pt1 * pt2: [0 0 0 1]