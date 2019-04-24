def areFollowingPattern(strings, patterns):
    check_pattern = {}
    check_string  = {}
    for idx, pattern in enumerate(patterns):

        if pattern not in check_pattern:
            check_pattern[pattern] = strings[idx]
            if strings[idx] in check_string:
                if check_string[strings[idx]] != pattern:
                    return False
            if strings[idx] not in check_string:
                check_string[strings[idx]] = pattern
        if pattern in check_pattern:
            if check_pattern[pattern] != strings[idx]:
                return False


    return True

if __name__ == '__main__':
    strings = ["cat",
 "dog",
 "doggy"]
    patterns = ["a",
 "b",
 "b"]
    strings = ["aaa",
               "aaa",
               "aaa"]
    patterns = ["aaa",
                "bbb",
                "aaa"]
    print(areFollowingPattern(strings, patterns))

