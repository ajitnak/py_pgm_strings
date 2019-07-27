def ident_char_count(str_one, str_two):
    if len(str_one) != len(str_two):
        return False

    char_count = [0]*128
    for c in str_one:
        char_count[ord(c)] += 1

    for c in str_two:
        char_count[ord(c)] -= 1
        if char_count[ord(c)] < 0:
            return False

    return True

x = "abcdefghijklmnooqrstuvwxyz"
y = "zyxwvutsrqabcdefghijklmooo"
print "stings is_perm = {}".format(ident_char_count(x,y))
