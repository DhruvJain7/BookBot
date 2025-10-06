def count_character(c):
    dictionary = {}
    lower = c.lower()
    for w in lower:
        if w in dictionary:
            dictionary[w] +=1
        else:
            dictionary[w] = 1
    return dictionary
def count_words(c):
    l =c.split()
    num_words = len(l)
    return num_words
def list_dict(d):
    l = []
    for i in d:
        num= d[i]
        char = i
        tmp = {}
        tmp["char"] = i
        tmp["num"] = num
        l.append(tmp)
    def sort_on(items):
        return items["num"]
    l.sort(reverse=True,key = sort_on)
    return l

    
