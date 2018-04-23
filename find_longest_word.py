#find the length of longest word from a file

file_obj = open('word.txt', 'r')

file_op = file_obj.read()

words = file_op.split('\n')

def find_longest_word(word_list):
	word_len = []
	for word in word_list:
		word_len.append((len(word), word))
	word_len.sort()
	return (word_len[-1][1])

longest_word = find_longest_word(words)
print(longest_word)