# cerner_2^5_2018
# checks if a string is a palindrome or not

def reverse(str):
    return str[::-1]

def isPalindrome(str): 
	rev = reverse(str) 

	if (str == rev): 
		return True
	return False

eg = "madam"
isPal = isPalindrome(eg) 

if isPal == 1: 
	print("Is a Palindrome") 
else: 
	print("Not a Palindrome") 
