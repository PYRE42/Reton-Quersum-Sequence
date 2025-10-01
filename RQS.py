N = 10

def quersum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

for i in range(0, 7):
    N = quersum(int(N))
    N = str(N) + str(N)
    print(N)

