import random

def arrayGame(arr):
    x = arr
    move = {0:"Aideen", 1: "Yara"}
    score = { "Aideen": 0, "Yara":0 }
    idx = 0

    while len(x) > 0:
        if idx % 2 == 0:
            score[move[idx % 2]] += max(x)
        else:
            score[move]
        x = x[len(x) - x[::-1].index(max(x)) - 1+1:]
        idx += 1

    if score[move[0]] == score[move[1]]:
        return "Draw"

    return "Aideen: {}".format(score[move[0]]) if score[move[0]] > score[move[1]] else "Yara: {}".format(score[move[1]])

def test(A):
    p = A.pop()

    while A:

        p = max(p, A.pop()-p)
        print p
    return ("Draw", "Aydeen: " + `p`, "Yara: " + `-p`)[cmp(p, 0)]

if __name__ == '__main__':
    # print arrayGame([random.randint(-10,10) for i in xrange(10)])
    # print arrayGame([random.randint(-10, 10) for i in xrange(10)])
    # print arrayGame([random.randint(-10, 10) for i in xrange(10)])

    print test([random.randint(-10,10) for i in xrange(6)])

    #arrayGame([-1,-2,-3,-4,-5])


