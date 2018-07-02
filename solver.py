WORDLIST_FILENAME = "words.txt"
def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME) as f:
        word_list = ''.join(f.readlines()).split()
    print("  ", len(word_list), "words loaded.")
    return word_list
def permutation(s):
    if len(s)==1:
        return s
    else:
        result=[]
        for i in range(0,len(s)):
            # return s+all('')
            p=permutation(s[:i]+s[i+1:])
            for word in p:
                result.append(s[i]+word)
        return result
def unique(words):
    return list(set(words))
word_list=load_words()
def word_finder(s):
    guesses=permutation(s)
    result=[]
    for word in guesses:
        if word in word_list:
            result.append(word)
    return result
print(unique(word_finder('treat')))