def one_edit_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    found_diff = False
    min_len = min (len(first), len(second))

    while i < len(first) and j < len(second):
        if first[i] != second[i]:
            if found_diff:
                return False
            found_diff = True
	else:
		i = i+1
		j = j+1
	
    return True



x = "para"
y = "ara"

print "{} and {} are one edit awat {}".format(x, y, one_edit_away(x, y))
