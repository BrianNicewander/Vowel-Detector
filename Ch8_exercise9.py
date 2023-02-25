# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:07:01 2020

@author: stc130
"""
def main():
    userInput = input('Please enter in a sentence ')
    vowels = 0
    consonants = 0
    whitespace = 0
    
    
    for currentLetter in userInput:
        letter=[] 
        letter.append(currentLetter)
        if letter == ['a']:
            vowels += 1
        elif letter == ['A']:
            vowels +=1
        elif letter == ['e']:
            vowels +=1
        elif letter == ['E']:
            vowels +=1
        elif letter == ['i']:
            vowels +=1
        elif letter == ['I']:
            vowels +=1
        elif letter == ['o']:
            vowels +=1
        elif letter == ['O']:
            vowels +=1
        elif letter == ['u']:
            vowels +=1
        elif letter == ['U']:
            vowels +=1
        elif letter == [' ']:
            whitespace += 1
        else:
            consonants +=1
       
      
    print (userInput) 
    print ("has")
    print (vowels, 'vowels')
    print (consonants, 'consonants')
    print (whitespace, 'spaces')      
        
main()