import math

def gegenwahrscheinlichkeit(n,k):
    # 1-((1/n)^k * Prod(n-k+1 to n)
    seq = range(n-k+1, n+1)
    return 1-(((1/n)**k) * math.prod(seq))


if __name__ == '__main__':
    print(gegenwahrscheinlichkeit(676, 36))


