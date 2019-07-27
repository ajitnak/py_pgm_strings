def str_compression(strx):
    if count_compr_len(strx) >= len(strx):
        return strx
    cc = 0
    compr_list = []
    for i in range(len(strx)):
        cc += 1
        if (i+1 == len(strx)) or (strx[i] != strx[i+1]):
            compr_list.append(strx[i])
            compr_list.append(`cc`)
            cc=0
    return ''.join(compr_list)

    
def count_compr_len(strx):
    cc = 0
    cmpr_len = 0
    for i in range(len(strx)):
        cc += 1
        if (i+1 == len(strx)) or (strx[i] != strx[i+1]):
            cmpr_len += 1+len(`cc`)
            print "cl = {} cc={} i={} chars= {}".format(cmpr_len, cc, i, strx[i])
            cc = 0
    print "cmpr_len = {}".format(cmpr_len)
    return cmpr_len

x = "aaaaaaaaaaaakaaaa"
print "original={},  compressed={}".format(x, str_compression(x))

