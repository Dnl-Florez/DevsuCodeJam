def PerfectBetween(x, y):
    for i in range(x, y+1):
        if PerfectNumber(i):
            return i
    return -1

def PerfectNumber(n):
    acum = 0
    for i in range(1, n):
        if (n % i == 0):
            acum += i
    if acum == n:
        return True
    else:
        return False

def main():
    x = int(input())
    y = int(input())
    print(PerfectBetween(x, y))

main()