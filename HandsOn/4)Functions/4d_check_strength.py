def check_strength(pw:str,min_len=8)->dict:
    length_ok = len(pw) >= min_len
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True
    score = sum([
        length_ok,
        has_upper,
        has_lower,
        has_digit,
        has_special
    ])
    return {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "score": score
    }
pw=input("Enter your password:")
res=check_strength(pw)
print(res)