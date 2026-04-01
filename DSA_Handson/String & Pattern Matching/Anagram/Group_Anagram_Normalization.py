words = ["café", "face", "écaf", "Paris", "pairs"]
def remove_accent(word):
    mapping = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'á': 'a', 'à': 'a', 'â': 'a', 'ä': 'a',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c', 'ñ': 'n'
    }
    res=""
    for c in word:
        if c in mapping:
            res+=mapping[c]
        else:
            res+=c
    return res
groups={}
for word in words:
    w=word.lower()
    w=remove_accent(w)
    key="".join(sorted(w))
    if key not in groups:
        groups[key]=[]
    groups[key].append(word)
for ans in groups.values():
    print(ans)
