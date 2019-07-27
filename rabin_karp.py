lass RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            #ord maps the character to a number
            #subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(word, text):
    if word == "" or text == "":
        return None

    if len(word) > len(text):
        return None

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))
    #word_hash.move_window()

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.move_window()
    return None

#print rabin_karp("a", "abcdefgh")
#print rabin_karp("d", "abcdefgh")
#print rabin_karp("cupcakes", "balloonsandcupcakes")
Complexity of Rabin-Karp
#Assume the text is length n and the length of the word is m. The best and average-case running time of Rabin-Karp is O(n+m).
#because the rolling hash step takes time and once the algorithm finds a potential match, it must verify each letter to make 
#sure that the match is true and not a result of a hashing collision, and therefore must check each of the  letters in the word.
#
#The worst-case running time of Rabin-Karp is O(nm). This would occur with an extremely awful hash function that resulted in a false 
#positive at each step. Since whenever the algorithm thinks it found a match, it must verify each of the  letters in the word, 
#if there is a collision at each step,  letters will be checked  times resulting in a running time of . This can be avoided with 
#a good choice of hash function.
#
#When searching for a single pattern to match in a text, the Knuth–Morris–Pratt algorithm will be a faster choice. For matching multiple patterns, the Rabin-Karp algorithm paired with a Bloom filter can efficiently find multiple patterns in a text.[4]

See Also
Aho–Corasick string matching algorithm

Hashing

Knuth–Morris–Pratt algorithm
