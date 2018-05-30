
def solve(num_ppl, num_queries):
    groups = [set([x]) for x in range(num_ppl+1)]
    group_sizes = dict()
    group_sizes[1] = num_ppl
    num_groups = num_ppl
    groups_changed = True
            
    for _ in range(num_queries):
        query = [int(x) for x in input().split()]
        
        if query[0] == 1:
            g1,g2 = groups[query[1]], groups[query[2]]
            if g1 != g2:
                for size in [len(g1),len(g2)]:
                    group_sizes[size] -= 1
                    if group_sizes[size] == 0:
                        del group_sizes[size]
                if len(g1) < len(g2):
                    g1,g2 = g2,g1
                for person in list(g2):
                    g1.add(person)
                    groups[person] = g1
                if len(g1) in group_sizes:
                    group_sizes[len(g1)] += 1
                else:
                    group_sizes[len(g1)] = 1
                num_groups -= 1
                groups_changed = True
                    
        if query[0] == 2:
            c = query[1]
            if c == 0:
                print((num_groups * (num_groups-1)) // 2)
                continue
            if groups_changed:
                sizes = sorted(group_sizes)
                groups_changed = False
            answer, small_teams = 0,0
            j = 0
            for i,x in enumerate(sizes):
                while j <= i and x - sizes[j] >= c:
                    small_teams += group_sizes[sizes[j]]
                    j += 1
                answer += group_sizes[x] * small_teams
            print(answer)


num_ppl, num_queries = [int(x) for x in input().split()]
solve(num_ppl, num_queries)

