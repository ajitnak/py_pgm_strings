import string

def isUniqueChars(mystr):
    if len(mystr) > 128:
        return False;

    char_set = [False] * 128
    for c in mystr:
        print "index: {}".format(ord(c))
        if char_set[ord(c)]:
            return False
        char_set[ord(c)] = True
    return True

y = "abcdefghijklmnopql_$"

print "str {} is unique {}".format("abcdfghijklmnABCD_$&$", isUniqueChars("abcdfghijklmnABCD_$&$"))
print "str {} is unique {}".format(y, isUniqueChars(y))
    
