import  sys
def cutRod(p, n):
    if n <= 0:
        return  0
    q =-sys.maxint - 1
    for i in range(0, n):

        q = max(q, p[i] + cutRod(p, n-i-1))
    return  q

def memorized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n==0:
        q = 0
    else:
        q = -sys.maxint-1
        for i in range(0,n):
            q = max(q, p[i] + memorized_cut_rod_aux(p, n-i-1, r))
    r[n] = q
    return  q

def memorized_cut_rod(p, n):
    r = [0]*(n+1) # set zero to array element
    for i in range(0, n+1):
        r[i] = -sys.maxint-1
    return  memorized_cut_rod_aux(p, n, r)

def bottom_up_cut_rod(p, n):
    r = [0] * (n+1)
    for j in range(1,n+1):
        q = -sys.maxint-1
        for i in range(j):
            q = max(q, p[i]+r[j-i-1])
        r[j] = q
    return  r[n]

def extended_bottom_up_cut_rod(p,n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    for j in range(1, n+1):
        q = -sys.maxint-1
        for i in range(j):
            if q < p[i] + r[j-i-1]:
                q = p[i] + r[j-i-1]
                s[j-1] = i+1
        r[j] = q
    return r,s


def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print s[n-1]
        n = n - s[n-1]


if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print "maximum obtainable value is %d" % cutRod(arr, 3)
    print "maximum obtainable value is %d" % memorized_cut_rod(arr, 3)
    print "maximum obtainable value is %d" % bottom_up_cut_rod(arr, 3)
    print  print_cut_rod_solution(arr,7)

