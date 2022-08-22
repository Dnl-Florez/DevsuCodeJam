'''
a1 - a2 - a3 - a4 - a5 - a6 - a7 - a8 - a9 - a10 - a11 - a12 - a13 - a14 - a15 - a16 - a17
 7 -  6 -  8 -  4 -  9 -  2 - 10 -  0 - 11 -  -2 -  12 -  -4 -  13 -  -6 -  14 -  -8 -  15
+6        +5        +4        +3        +2          +1           0          -1          -2

a(n) = -(n - 8) <- n par
a(n) = n + ((13 - n) // 2) <- n impar
'''

def Serie(x, y):
    if (x == 0 or x < 0 or x > 255 or y == 0 or y < 0 or y > 255):
        return -1
    else:
        if (x % 2 == 0):
            x = -1 * (x - 8)
        else:
            x = x + ((13 - x) // 2)

        if (y % 2 == 0):
            y = -1 * (y - 8)
        else:
            y = y +((13 - y) // 2)
    return x + y

def main():
    x = int(input())
    y = int(input())
    print(Serie(x, y))

main()