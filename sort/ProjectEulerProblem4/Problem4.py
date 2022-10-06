largestPalindrome = 0
largestI = 0
largestJ = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        result = int(i * j)
        print(f"({str(i)}) * ({str(j)}) = {result}" + "\n")
        strResult = str(result)
        reverseResult = strResult[::-1]
        if strResult == reverseResult:
            print(f"Palindrome found! {result}" + "\n")
            if result > largestPalindrome:
                largestI = i
                largestJ = j
                largestPalindrome = result
print(
    f"The largest palindrome from 2 three-digit numbers is: ({str(largestI)}) * ({str(largestJ)}) = {str(largestPalindrome)}"
)
