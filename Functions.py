#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 22:21:17 2023

@author: treewalker
"""
import numpy as np


# print(int(ord('z'))-97) #for converting letters to numbers for small letters 65 for cap
# The ord() function takes a string that represents 1 Unicode character and returns an integer representing the Unicode code point of the given character.

###############ENCRYPT####################

def text_to_num(text):
    text = text.upper()
    T = [0, 0]
    for i in range(2):
        T[i] = ord(text[i])-63
    return T

def key_to_num(key):
    key = key.upper()
    K = [[0, 0], [0, 0]]
    i = 0
    for r in range(2):
        for c in range(2):
            K[r][c] = ord(key[i])-63
            i += 1
    return(K)

def Mod_26_Text(array):
    global l
    for r in range(2):
        while array[r] > 27 or array[r] < 0:
            array[r] = array[r] % 28
    return(array)

def Mod_26_Key(array):
    global l
    for r in range(2):
        for c in range(2):
            while array[r][c] > 27 or array[r][c] < 0:
                array[r][c] = array[r][c] % 28
    return(array)
    
def Matrix_Multiply(Mat_A, Mat_B):
    C = [0,0]
    for i in range(len(Mat_A[0])):
        for j in range(len(Mat_B)):
            C[i] += Mat_A[i][j] * Mat_B[j]
    C = Mod_26_Text(C)
    return(C)

def num_to_text(num):
    cipher = ""
    for i in range(len(num)):
        cipher += chr(num[i] + 63)
    return(cipher)

###############DECRYPT####################

def Mat_Inverse(array):
    status = 1
    K = [[0,0], [0,0]]
    K = np.linalg.inv(array) * np.linalg.det(array)
    D = int(np.linalg.det(array))

    #Finding Modulo-Inverse of Determinant by Trial and Error
    Mod_Inverse=0
    Mod_Identity = 0
    while Mod_Identity!=1:
        Mod_Identity = (abs(D)*Mod_Inverse) % 28
        Mod_Inverse += 1
        if Mod_Inverse > 100*abs(D):
            print("INVERSE DONT EXIST FOR THE KEY : TRY ANOTHER  KEY")
            status = 0
            break
    K = Mod_26_Key(K)
    K = (Mod_Inverse - 1)*K         
    return(K, status)

def Float_to_Int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

