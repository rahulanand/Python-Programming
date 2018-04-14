#input string ex: '123456'
n = input()
#threshold value input
threshold = int(input())

def find_sum(n, threshold):
	sum = 0
	red_string = ''
	for i in n:
		sum += int(i)
		if sum > threshold:
		 	red_string = red_string + str(sum)
		 	threshold = sum
		 	sum = 0
	return red_string, threshold

def find_reduced_string(n, threshold):
	x = sum_str(n)
	if x > threshold:
		new_str, sum = find_sum(n, threshold)
		y = find_reduced_string(new_str, sum)
		return y
	else:
		return x

def sum_str(st):
	sum = 0
	for i in st:
		sum += int(i)
	return sum


out = find_reduced_string(n, threshold)
if len(str(out)) > 1:
	sum = sum_str(out)
	print(sum)
else:
	print(out)