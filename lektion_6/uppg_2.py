def smooth_a(a, n):
    r = []
    for i in range(len(a)):
        tot = 0
        tot += min(0, i - n)*a[0]*(-1)
        tot += max(0, i + n - (len(a)-1))*a[len(a)-1]
        tot += sum(a[max(0, i-n):min(len(a), i+n+1)])
        r.append(tot)
    return [r_i/(2*n+1) for r_i in r]


def round_list(a_list, ndigits):
    return [round(a_i, ndigits) for a_i in a_list]

if __name__ == "__main__":
    x = [1, 2, 6, 4, 5, 0, 1, 2]
    print('smooth_a(x, 1) rounded: ', round_list(smooth_a(x, 1), 2))
