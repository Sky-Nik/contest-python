n, m = map(int, input().split())

pc = [(0, 0) for _ in range(n)]

party_votes = [0 for _ in range(m)]

for i in range(n):
    p, c = map(int, input().split())
    pc[i] = (p - 1, c)
    party_votes[p - 1] += 1

pc.sort(key=lambda x: x[1])

min_cost = 10**20

for votes in range(n + 1):
    _party_votes = party_votes[:]
    dangerous = list(map(lambda party: _party_votes[party] >= votes, range(0, m)))
    used = list(map(lambda i: pc[i][0] == 0, range(n)))
    cur_cost = 0
    for i in range(n):
        if dangerous[pc[i][0]] and pc[i][0] != 0:
            cur_cost += pc[i][1]
            _party_votes[0] += 1
            _party_votes[pc[i][0]] -= 1
            dangerous[pc[i][0]] = _party_votes[pc[i][0]] >= votes
            used[i] = True
    for i in range(n):
        if _party_votes[0] >= votes:
            break
        if not used[i]:
            _party_votes[0] += 1
            cur_cost += pc[i][1]
    min_cost = min(min_cost, cur_cost)

print(min_cost)
