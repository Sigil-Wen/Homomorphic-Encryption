 # BUILD AN HOMOMORPHIC ENCRYPTION SCHEME FROM SCRATCH WITH PYTHON

 I find it interesting just how much simpler it is to do addition than multiplication in HE

 Original post: https://blog.openmined.org/build-an-homomorphic-encryption-scheme-from-scratch-with-python/#buildanhomomorphicencryptionscheme 

 % python3 main.py

[+] Ciphertext ct1(73):

         ct1_0: [14719  3492 24403 24872 25968 11663 28877 13952 15731 25088 15027 29383
 17578 19070 32335  4775]
         ct1_1: [29104 20624 13063  6072 24867 10998  4512  2856  7119 19677 21591 16414
   731 23973 17249 18170]

[+] Ciphertext ct3(73):

         ct3_0: [15615  3492 24403 24872 25968 11663 28877 13952 15731 25088 15027 29383
 17578 19070 32335  4775]
         ct3_1: [29104 20624 13063  6072 24867 10998  4512  2856  7119 19677 21591 16414
   731 23973 17249 18170]

It seems like addition is significantly easier than multiplication which makes sense

[+] Ciphertext ct2(20):

         ct1_0: [ 7930 15315 11997 23103 12634 13246 31835 26559 21953  7353  8841 24366
 12765  9990 14293  4253]
         ct1_1: [28157  2158 21947  7530 23084 22977   161  7238  3094 32667 14197  7654
 19217 25215 24228  8345]



[+] Ciphertext ct4(20):

         ct4_0: [ 6882 11039 27217 17211 30402   694 28103  1723 11461  3997 11437 23526
 31057 17182  5929 21265]
         ct4_1: [ 9713 10790 11431  4882 17116 16581   805  3422 15470 32263  5449  5502
 30549 27771 22836  8957]

[+] Decrypted ct3(ct1 + 7): 80
[+] Decrypted ct4(ct2 * 5): 100
(base) sigilwen@MacBook-Pro-87 HE % 