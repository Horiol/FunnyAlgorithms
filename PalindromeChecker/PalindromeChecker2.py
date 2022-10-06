def PalindromeCheck(s):
	return s == s[::-1]
s=input()
if(PalindromeCheck(s)):
	print("It is a palindrome!!")
else:
	print("It is not a palindrome..")