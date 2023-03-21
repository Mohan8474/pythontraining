
dict1 = {}
def addw(key):
    if key in dict1:
        dict1[key] += 1
    else:
        dict1[key] = 1

    return

def vieww():
    return dict1.keys()

def wordscount(word):
    if not dict1:
        return "No words added yet"
    else:
        for word, count in dict1.items():
            return word, count

def wordsandcount(count):
    filtered_words = [word for word, word_count in dict1.items() if word_count == count]
    if not filtered_words:
        return "No words found with that count"
    else:
        for word in filtered_words:
            return word



