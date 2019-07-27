def one_edit_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    found_diff = False
    index_one = 0
    index_two = 0
    if len(second) > len(first):
        str_one = first
        str_two = second
    else:
        str_two = first
        str_one = second

    while index_one < len(str_one) and index_two < len(str_two):
        if str_one[index_one] != str_two[index_two]:
            if found_diff:
                return False
            found_diff = True
            if len(str_one) == len(str_two):
                index_one += 1
        else:
            index_one +=1
        index_two +=1
    return True



x = "parka"
y = "para"

print "{} and {} are one edit awat {}".format(x, y, one_edit_away(x, y))
