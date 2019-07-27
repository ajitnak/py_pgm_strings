def str_swap(s):
	s = list(s)
	end_idx = len(s)-1
	for i in range(len(s)/2):
		temp = s[i]
		s[i] = s[end_idx-i]
		s[end_idx - i] = temp
	return ''.join(s)

print str_swap("1234567")
print str_swap("123456")
