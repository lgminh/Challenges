table_result = {1: [1, 0], 2: [1, 1]}
f_table = {1: 1, 2: 2}
smallest_l = []
biggest_r = []

def robot2(l, r):
    def cal(n, prev_n):
        if n in table_result and prev_n not in table_result:
            if prev_n % 2 == 0:
                table_result[prev_n] = [table_result[n][0], table_result[n][1] + 1]
            else:
                table_result[prev_n] = [table_result[n][0] + 1, table_result[n][1]]
            f_table[prev_n] = table_result[prev_n][0]*table_result[prev_n][1]

        elif prev_n not in table_result:
            cal(n / 2, n) if n % 2 == 0 else cal(n - 1, n)
            table_result[prev_n] = [table_result[n][0], table_result[n][1] + 1] if prev_n % 2 == 0 \
                else [table_result[n][0] + 1, table_result[n][1]]

    if smallest_l == []:
        smallest_l.append(l)
        biggest_r.append(r)

        for n in xrange(l, r + 1):
            cal(n / 2, n) if n % 2 == 0 else cal(n - 1, n)
            f_table[n] = table_result[n][0]*table_result[n][1]

        return sum([f_table[i] for i in xrange(l, r + 1)])
    elif l >= min(smallest_l) and r <= max(biggest_r):
            #return f_table[r] - f_table[l]
        return sum([f_table[i] for i in xrange(l, r + 1)])
    else:
        if l not in smallest_l and r not in biggest_r:
            for n in xrange(l, r + 1):
                cal(n / 2, n) if n % 2 == 0 else cal(n - 1, n)
                f_table[n] = table_result[n][0] * table_result[n][1]
        else:
            if l in smallest_l and r not in biggest_r:
                for n in xrange(l, min(smallest_l)):
                    cal(n / 2, n) if n % 2 == 0 else cal(n - 1, n)
                    f_table[n] = table_result[n][0]*table_result[n][1]

            for n in xrange(r + 1, max(biggest_r) + 1):
                cal(n / 2, n) if n % 2 == 0 else cal(n - 1, n)
                f_table[n] = table_result[n][0] * table_result[n][1]

        return sum([f_table[i] for i in xrange(l, r + 1)])
        #return f_table[r] - f_table[l]

if __name__ == '__main__':
    import time
    t = time.time()

    print robot2(3, 5) == 8
    print robot2(9, 10) == 12
    print robot2(6, 8) == 13
    print robot2(1, 100) == 1593
    print robot2(100, 200) == 2801
    print robot2(239, 344) == 3601
    print robot2(1, 10**6) == 178377796
    print robot2(30, 1048575) == 189792020
    print robot2(1016, 1047552) == 189459234
    print robot2(126, 1048575) == 189789966
    print str(float(time.time() - t)) +  " s"