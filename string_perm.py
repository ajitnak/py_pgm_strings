def is_perm(str_one, str_two):
    if len(str_one) != len(str_two):
        return False;
    if sorted(str_one) == sorted(str_two):
        return True
    return False

x = "abcdefghijklmnooqrstuvwxyz"
y = "zyxwvutsrqabcdefghijklmnoo"
print "stings is_perm = {}".format(is_perm(x,y))
