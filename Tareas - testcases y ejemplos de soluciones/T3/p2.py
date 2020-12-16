def mu(x):
    if muarr[x] > -2:
        return muarr[x]
    elif x == 1:
        muarr[x] = 1
        return 1
    elif (x // sieve[x]) % sieve[x] == 0:
        muarr[x] = 0;
        return 0;
    else:
        val = -mu(x // sieve[x])
        muarr[x] = val
        return val;

N = 200000
sieve = [0] * (N+1)
for i in range(2, N+1):
    if sieve[i] == 0:
        sieve[i] = i
        for j in range(i*i, N, i):
            sieve[j] = i
muarr = [-2] * (N+1)
 
data_in = input().strip().split(" ")

if data_in[0] == "1":
    n = int(data_in[1]) 
    print(mu(n))
else:
    n = int(data_in[1])
    m = int(data_in[2])
    tot = 0
    for i in range(1, n+1):
        tot += mu(i) * (n // i) * (m // i)
    print(tot)
