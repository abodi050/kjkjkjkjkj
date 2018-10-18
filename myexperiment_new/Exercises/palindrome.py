def palindrome(word):
	word=word.replace(" ","")
	if word[:]==word[::-1]:
		return True
	else:
		return False

print(palindrome("madam"))
print(palindrome("nurses run"))