def is_pali_comb(pali_str):
    bv = 0
    a_val = ord('a')
    for c in pali_str.lower():
        bv = toggle(bv, ord(c) - a_val)
	print bv

    print "bv: {}".format(bv)
    if bv & (bv-1) == 0:
        return True

    return False

def toggle(bv, bit):
    #print "toggele {} bit in {}".format(bit, bv)
    if bit < 0:
        return
    mask  = 1 << bit
    if bv & mask == 0:
        bv |= mask
    else:
        bv &= ~mask
    return bv

x = "TactCax"        

print "{} is palindrome comb0 {}".format(x, is_pali_comb(x))
