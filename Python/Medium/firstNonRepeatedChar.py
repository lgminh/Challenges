from string  import  ascii_lowercase
def firstNonRepeatedChar(s):
    x = {}

    for i in ascii_lowercase:
        x[i] = []

    for idx, c in enumerate(s):
        x[c].append(idx)

    for k,v in x.items():
        if len(v) != 1:
            del x[k]

    print min(x.values())

    for k,v in x.items():
        if min(x.values())[0] == v[0]:
            return k


if __name__ == '__main__':
    print firstNonRepeatedChar('sdadsaasuwqf')