def minSubstringWithAllChars(s, t):
    if len(s) < 2:
        return t if t == s else ""
    if len(t) < 2:
        return t if t in s else ""

    check_list = {c: -1 for c in t}
    left_pointer = 0
    right_pointer = 1
    position = {
        'smallest_left': 0,
        'smallest_right': 0,
        'smallest_length': len(s)
    }
    while s[left_pointer] not in t:
        left_pointer += 1
        right_pointer += 1

    check_list[s[left_pointer]] = 1

    while left_pointer < len(s) - 1 and right_pointer <= len(s) -1 :
        if s[left_pointer] == s[right_pointer]:
            left_pointer += 1
            while True:
                # check duplicate character in subtring
                if left_pointer == len(s) - 1 or s[left_pointer] in t:
                    break
                if s[left_pointer] not in t or (s[left_pointer] == s[left_pointer + 1] and s[left_pointer] in t):
                    left_pointer += 1
        if s[right_pointer] in t:
            if check_list[s[right_pointer]] == -1:
                check_list[s[right_pointer]] = 1
        if -1 not in check_list.values():
            if position['smallest_length'] > right_pointer - left_pointer - 1:
                position['smallest_length'] = right_pointer - left_pointer - 1
                position['smallest_left'] = left_pointer
                position['smallest_right'] = right_pointer
            check_list = {c: -1 for c in t}
            left_pointer += 1
            while s[left_pointer] not in t:
                left_pointer += 1
            check_list[s[left_pointer]] = 1
            check_list[s[right_pointer]] = 1
        right_pointer += 1

    left = position['smallest_right'] - 1
    check_list = {c: -1 for c in t}
    check_list[s[position['smallest_right']]] = 1
    while left > position['smallest_left']:
        if -1 not in check_list.values():
            break
        if s[left] in t:
            check_list[s[left]] = 1
        left -= 1

    result = s[left: position['smallest_right'] + 1]
    if result.count(s[left]) > 1:
        left += 1

    return s[left: position['smallest_right'] + 1]



if __name__ == '__main__':
    print(minSubstringWithAllChars("adobecodebanc", "abc"))
    print(minSubstringWithAllChars("zqyvbfeiee", "ze"))
    print(minSubstringWithAllChars("abz", "abz"))
    print(minSubstringWithAllChars("abcdefghijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz"))
    print(minSubstringWithAllChars("tvdsxcqsnoeccaurocnk","acqt"))
    print(minSubstringWithAllChars("ywcjorwmhwjfowgkpjxkdmjlrljhgtejidsiiqpnmsspzfyeoj","wmlrjdsipzfoe"))
    print(minSubstringWithAllChars("udphrojoebzjmzncvnuotwrtqhupaopurxqnhckbvdchauolsywxcklualquqpyexmwxucwdzbfkvrjhjkxvlgcxdogfbibcjjbn",
                                   "abcdefghijklmnopqrstuvwxyz"))

#sywxcklualquqpyexmwxucwdzbfkvrjhjkxvlgcxdogfbi
#abcdefghijklmnopqrstuvwxyz







