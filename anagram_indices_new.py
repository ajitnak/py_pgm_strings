from collections import defaultdict

def del_zero_count(dict, c):
	if not dict[c]:
		del dict[c]

def get_anagrams(word, str):
	result = []
	dict = defaultdict(int)

	if len(word) > len (str):
		return result

	for c in word:
		dict[c] += 1
	wl = len(word)

	for c in str[:wl]:
		dict[c] -= 1
		del_zero_count(dict, c)

	if not dict:
		result.append(0)

	print "result=",result

	for i in range(wl, len(str)):
		start_char, end_char = str[i - wl], str[i]
		dict[start_char] += 1
		del_zero_count(dict, start_char)
		dict[end_char] -= 1
		del_zero_count(dict, end_char)

		print dict	
		#if all(val==0 for val in dict.values()):
		if not dict:
			result.append(i- wl + 1)
	return result
		
		


	
print get_anagrams("ABCD", "BACDGABCDA")
#print get_anagrams("AABA", "AAABABAA")
