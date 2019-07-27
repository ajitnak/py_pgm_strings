def idToShortURL(n):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    shortURL = ''
    while n>0:
        shortURL = chars[n%62-1] + shortURL
        n = n/62
    return shortURL

def shortURLToId(surl):
    urlId = 0
    for i in range(len(surl)):
        if 'a' <= surl[i] and surl[i] <= 'z':
            urlId = urlId * 62  + ord(surl[i]) - ord('a')+1
        if 'A' <= surl[i] and surl[i] <= 'Z':
            urlId = urlId * 62  + ord(surl[i]) - ord('A') + 27
        if '0' <= surl[i] and surl[i] <= '9':
            urlId = urlId * 62  + ord(surl[i]) - ord('0') + 53

    return urlId

origId = 755790923455
surl = idToShortURL(origId)

print "id/shorturl : {} => {}".format(origId, surl)
print "shorturl=>id : {} => {}".format(surl, shortURLToId(surl))

id = shortURLToId("abcd")
print id
url=idToShortURL(id)
print url
