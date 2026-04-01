def is_anagram(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in t:
        if ch in freq:
            freq[ch] -= 1
        else:
            return False
    for val in freq.values():
        if val != 0:
            return False
    return True
print(is_anagram("listen", "silent"))