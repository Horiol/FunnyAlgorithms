def check_palin(string):
    n = len(string)
    return all(string[i] == string[n-i-1] for i in range(n // 2))

def main():
    print("Input the String: ")
    string = input()

    if(check_palin(string)):
        print("String is a Palindrome")
    else:
        print("String is not a Palindrome")
        
if __name__ == '__main__':
    main()
    
