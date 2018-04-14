'''
		Input format:
			n = '1546287'
			threshold = 10  "value to be compared"
		Output format:
			: 6
	Explanation:
		1.sum = 1+5+4+6 > threshold = 16
			reduced_string = '16'287
		2. sum = 2+8+7 > 16 (new threshold)
		   reduced_string = 1617 , threshold = 17
		3. sum = 1+6+1+7 = 15 < 17
		 so reduced_string = 1+5 = 6
'''
#input string ex: '123456'
n = input()
#threshold value input
threshold = int(input())
#this method give you the red_string and new threshold value
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

# it will give you two digit reduced_string
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
# converting out to string
new_out = str(out)
#checking the length of string
if len(new_out) > 1:
	sum = sum_str(new_out)
	print(sum)
else:
	print(new_out)
