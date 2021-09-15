def smooth_a(a, n):
    r = []
    for i in range(len(a)):
        tot = 0
        tot += min(0, i - n)*a[0]*(-1)  # mult index 0 i - n ant ggr om < 0
        tot += max(0, i + n - (len(a)-1))*a[len(a)-1]   # -"- för över maxindex
        tot += sum(a[max(0, i-n):min(len(a), i+n+1)])
        r.append(tot)
    return [r_i/(2*n+1) for r_i in r]


def smooth_b(a, n):
    r = []
    for i in range(len(a)):
        tot = 0
        tot += sum(a[max(0, i-n):min(len(a), i+n+1)])
        r.append(tot/len(a[max(0, i-n):min(len(a), i+n+1)]))
    return r


x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
print('smooth_b(x, 1): ', smooth_b(x, 1))
print('smooth_b(x, 2): ', smooth_b(x, 2))
