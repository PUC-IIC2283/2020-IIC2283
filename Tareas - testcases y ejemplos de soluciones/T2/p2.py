from heapq import heappush, heappop

def main():
    N, M, A, B = map(int, input().split())
    g = [[] for _ in range(N)]
    degree = [0 for _ in range(N)]
    erased = [False for _ in range(N)]
    while M > 0:
        M -= 1
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    h1 = []
    h2 = []
    for u in range(0, N):
        heappush(h1, (degree[u], u))
        heappush(h2, (-degree[u], u))
    count = N
    while True:
        dirty = False
        while len(h1) > 0:
            d, u = h1[0]
            if erased[u]:
                heappop(h1)
                continue
            if degree[u] != d:
                heappop(h1)
                continue
            if d >= A:
                break
            heappop(h1)
            count -= 1
            erased[u] = True
            dirty = True
            for v in g[u]:
                if not erased[v]:
                    degree[v] -= 1
                    heappush(h1, (degree[v], v))
                    heappush(h2, (-degree[v], v))
        while len(h2) > 0:
            d, u = h2[0]
            d = -d
            if erased[u]:
                heappop(h2)
                continue
            if degree[u] != d:
                heappop(h2)
                continue
            if count - d - 1 >= B:
                break
            heappop(h2)
            count -= 1
            erased[u] = True
            dirty = True
            for v in g[u]:
                if not erased[v]:
                    degree[v] -= 1
                    heappush(h1, (degree[v], v))
                    heappush(h2, (-degree[v], v))
        if not dirty:
            break
    print(count)

main()