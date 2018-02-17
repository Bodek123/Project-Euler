#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:23:58 2018

@author: michal
"""
#Found the palindrom 906609, which is made from 913*993
#
#


arr=[]
allPalindromes= []




#can use union and check the same values

def isPalindrome(value):
    
    if str(value) == str(value)[::-1]:   
#       print(str(value) +" to palindrom")
       palindrome = value          
       return palindrome



for i in range (100000, 1000000):
    if str(isPalindrome(i)).isdigit()==True:
        allPalindromes.append(isPalindrome(i))
    

print(allPalindromes)
#print(len(allPalindromes))
rang= range(len(allPalindromes)-150, len(allPalindromes),1)
print(rang)
#
#print("-"*20)



for i in rang:
#    print(allPalindromes[i])
    arr = []
    print("Obliczenia dla: " + str(allPalindromes[i]))
    for number in range(10000,1,-1):
        if allPalindromes[i] % number == 0 and number<10000:
            if 100<number<1000:
                arr.append(number)
            print(number)
    if len(arr)>1:
        print("Obliczenia dla: " + str(allPalindromes[i]))
        
        print("Wartosc z mnozenia dla {}, to {}".format(allPalindromes[i],arr[0]*arr[1]))
        print("-"*20)
        if arr[0]*arr[1] == allPalindromes[i]:
            print("Wartosc z mnozenia dla {}, to {}".format(allPalindromes[i],arr[0]*arr[1]))
            print("Answer is: " + (str(allPalindromes[i]))+ " dla liczb: "+ str(arr[0]) + " i " +str(arr[1]))

#            
            if 1000>arr[0]>100 and 1000>arr[1]>100:
                  print("Wartosc z mnozenia dla {}, to {}".format(allPalindromes[i],arr[0]*arr[1]))
                  print("Answer is: " + (str(allPalindromes[i]))+ " dla liczb: "+ str(arr[0]) + " i " +str(arr[1]))
                  Answer = str(allPalindromes[i])
print("Answer is: {}".format(Answer))       
a = input("Press key")