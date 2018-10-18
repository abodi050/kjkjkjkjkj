'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''
def paper_doll(word):
	final_word =" "
	for char in word:
		final_word =final_word+ char*3
	return final_word
print(paper_doll("hello"))