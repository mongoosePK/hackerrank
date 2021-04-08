# day25RunningTimeAndComplexity.py
# william pulkownik
# borrowed from wikipedia because I wasn't interested in developing my own primality algorithm

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("Not Prime")
    if n <= 3 and n > 1:
        print(f"Prime")
    if n % 2 == 0 or n % 3 == 0:
        print("Not Prime")
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            print("Not Prime")
            i += 6
        else:
            print("Prime")

