s = input()
n = len(s)

tabla = [[0,0,0] for i in range(n+1)]

for i in range(n):
	a = int(s[i]);
	for k in range(3):
		tabla[i+1][(k + a) % 3] = tabla[i][k]
	tabla[i+1][a % 3] = tabla[i+1][a % 3] + 1

res = 0
for i in range(n+1):
	res = res + tabla[i][0]

print(res)