def checkPalindrome(s):
	return s == s[::-1]
s=input()
if(checkPalindrome(s)):
	print("This is a palindrome!!!")
else:
	print("This is not a palindrome...")