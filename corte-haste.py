import time
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q


def cut_rod_pd(p, n, r):
    if n in r.keys():
        return r[n]
    if n==0:
        return n
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + cut_rod_pd(p, n-i, r))
    r[n] = q
    return q

def main():
    ini1 = time.time()
    print "cut_rod: ", cut_rod(p, 10)
    fim1 = time.time()
    ini2 = time.time()
    print "cut_rod_pd: ", cut_rod_pd(p, 10, {})
    fim2 = time.time()
    print "tempo cut_rod: ", (fim1-ini1)
    print "tempo cut_rod_pd: ", (fim2 - ini2)


if __name__ == '__main__':
    main()