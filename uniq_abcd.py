import string

def isUniqueChars(mystr):
    lstr = mystr.lower()
    if len(lstr) > 26:
        return False;

    checker = 0
    for c in lstr:
        val = ord(c) - ord('a')
        print "val = {}".format(val)
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

print "str {} is unique {}".format("abcdfghijklmnABCD", isUniqueChars("abcdfghijklmnABCD"))
