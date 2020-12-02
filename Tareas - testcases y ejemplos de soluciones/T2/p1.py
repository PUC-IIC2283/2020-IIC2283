import cmath

def fft(arr, n):
    if(n == 2):
        return [arr[0] + arr[1], arr[0] - arr[1]]
    else:
        arr1 = [arr[2*i] for i in range(n//2)]
        arr2 = [arr[2*i+1] for i in range(n//2)]
        res1 = fft(arr1, n//2)
        res2 = fft(arr2, n//2)
        om = cmath.exp(complex(0, 2*cmath.pi/n))
        a = 1
        res = [0 for i in range(n)]
        for k in range(n//2):
            res[k] = res1[k] + a * res2[k]
            res[n//2 + k] = res1[k] - a * res2[k]
            a *= om
        return res

ina = list(map(int, input().split()))
n = ina[0]
inb = list(map(int, input().split()))
m = inb[0]

bign = 1
while bign <= n+m:
    bign *= 2

A = [0 for i in range(bign)]
for i in range(n+1):
    A[i] = ina[i+1]

B = [0 for i in range(bign)]
for i in range(m+1):
    B[i] = inb[i+1]

fA = fft(A, bign)
fB = fft(B, bign)

C = [fA[0]*fB[0]] + [fA[bign-i]*fB[bign-i] for i in range(1,bign)]

anscomp = fft(C, bign)

ans = [int(round(anscomp[i].real/bign)) for i in range(n+m+1)]

print(n+m, *ans, sep=" ")