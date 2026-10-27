# Python program to check palindrome
import sys
string = sys.argv[1]

if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")