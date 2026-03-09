def compressedString(word):
    res = ""
    count = 0
    prev = word[0]
    for ch in word:
        if ch == prev and count < 9:
            count += 1
        else:
            res += prev + str(count)
            prev = ch
            count = 1
    res += prev + str(count)
    return res
word = input("Enter the string:")
ans = compressedString(word)
print(ans)