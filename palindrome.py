##Programmer: Joselyne Guillen
##File Name: palindrome.py 
##Date: 4/25/21
##Version: 1.6
##Explanation of Program: 
##This program has the user enter a word,
##phrase, or sentence and checks to see
##if the user's input is a palindrome.
##A palindrome reads the same forwards
##and backwards.
def isPalindrome(s,f,l): #isPalindrome function with 3 parameters for the string, starting point of string, and ending point of string respectively
    if (len(s) < 2): #if string only has one letter or zero letters, it is a palindrome
        return True
    if (s[f] != s[l]): #if the first letter doesn't match the last letter in string/substring, it isn't a palindrome
        return False
    if (f == l): #base case: when the positions are equal(first and last), end recursion
        return True
    else:
        return isPalindrome(s,f+1,l-1) #recursive call; check substring to see if it is a palindrome
        
def main(): #main function
    my_string = input('Please enter a word, phrase, or sentence to see if it is a palindrome\n') #asks user to enter a word, phrase, or sentence
    my_string = my_string.replace(" ","") #strips user input of spaces
    my_string = my_string.replace(",", "") #strips user input of commas
    my_string = my_string.lower() #converts any uppercase letters in user input to lowercase
    length = len(my_string) #gets length of user string
    if(isPalindrome(my_string,0,length-1)): #if isPalindrome returns true, print a message saying it is a palindrome
        print('It is a palindrome')
    else:
        print('It is not a palindrome') #if isPalindrome returns false, print a message saying it is not a palindrome
    
main()#main function call
