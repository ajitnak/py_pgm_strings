def str_urlify(url_str, true_len):
    url_list = list(url_str)
    num_ws = 0
    for i in range(true_len):
        if url_str[i] == " ":
            num_ws += 1

    index  = true_len + 2 *num_ws
    if true_len < len(url_str):
        url_list[true_len] = "\0"

    print "strarting index: {}".format(index)
    for i in reversed(range(true_len)):
        if url_list[i] == " ":
            url_list[index-1] = '0'
            url_list[index-2] = '2'
            url_list[index-3] = '%'
            index -= 3
            print"char {}{}{} at index {}".format(url_list[index], url_list[index+1],url_list[index+2],index) 
        else:
            url_list[index -1] = url_list[i]
            index -= 1
            print"char {} at index {}".format(url_list[index], index) 

    return ''.join(url_list)

x = "Mr John Smith       "
print "stings is_perm = {}".format(str_urlify(x, 13))
