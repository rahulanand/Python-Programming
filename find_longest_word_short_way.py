#find the length of longest word from a file

file_obj = open('word.txt', 'r')

file_op = file_obj.read()

words = file_op.split('\n')

#sorting the words using length parameter
sort_word = sorted(words, key=len)

longest_word = sort_word[-1]

print(longest_word)