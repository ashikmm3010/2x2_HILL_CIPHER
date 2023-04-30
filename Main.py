
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:10:58 2023

@author: treewalker && Wanderlust
"""

from Functions import *

global key
global l
l = 0
global K_INV

# chr 63 == ? reserved for space
# chr 64 == @ reserved for blank character (odd no of char in text)
def encrypt(text, key):
    
    global l

    
    T = text_to_num(text)

    K = key_to_num(key)
    
    C = Matrix_Multiply(K, T)

    cipher = num_to_text(C)
    
    return(cipher)


def decrypt(cipher, key):
    
    global K_INV
    
    C = text_to_num(cipher)
    K = key_to_num(key)
    
    T = Matrix_Multiply(K_INV, C)
    
    T = Float_to_Int(T)
    
    text = num_to_text(T)
    
    return(text)


#MAIN CODE
print("2x2 HILL CIPHER\n\n"+
      "Enter a Key Containing Four Alphabets\n" +
      "Return 1 to use the default key - DDCF\n"+
      "Note: All keys are not invertible!!\n")

while True:
    
    key  = input("\nENTER THE KEY : ")
    if key == "1":
        key = "DDCF" #Defualt Key. Note : Some keys are not invertible
    #checking for inverse of key
    K = key_to_num(key)
    K_INV, status = Mat_Inverse(K)
    if status == 0:
        break

    text = input("ENTER THE TEXT: ")
    
    text = text.replace(" ", "?")
    
    l = len(text)
    
    if l%2 == 1:
        text += "@"
        l += 1 
    cipher = ""
    i=0
    for a in range(len(text)//2):
        cipher += encrypt(text[i:i+2], key)
        i+=2
    print("ENCRYPTED TEXT: ", cipher)
    
    text = ""
    i=0
    for a in range(len(cipher)//2):
        text += decrypt(cipher[i:i+2], key)
        i+=2
        
    text = text.replace("?", " ")
    text = text.replace("@", "")
    print("DECRYPTED CIPHER: ", text + "\n")