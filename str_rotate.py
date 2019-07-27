import string
def is_string_rotated(orig, rotated):
    #ajitnayak <=>tnayakaji
    if len(orig) > 0 and len(orig) != len(rotated):
        return False

    combo = orig + orig
    if string.find(combo, rotated) != -1:
        return True
    return False

x = "ajitnayak"
y = "tnayakaji"

print "{} and {} are string rotatations : {}".format(x, y, is_string_rotated(x, y))
