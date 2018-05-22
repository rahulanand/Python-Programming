'''
	Selection Sort Implementation
	Rahul
'''
def find_selection_sort(li):
	new_li = []
	n = len(li)
	for i in range(0, n):
		new_li.append(min(li))
		ind = li.index(min(li))
		del li[ind]

	return new_li

if __name__ == '__main__':
	#x = [23,11,45,24,56,10]
	x = list(map(int, input().split()))
	print(find_selection_sort(x))