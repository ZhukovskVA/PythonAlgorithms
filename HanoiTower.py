def hanoi_solver(n):
    steps_number = (2 ** n) - 1
    rods = [[], [], []]
    ans = ''
    for i in range(n, 0, -1):
        rods[0].append(i)
    ans += str(rods[0]) + ' ' + str(rods[1]) + ' ' + str(rods[2])
    ans += '\n'
    step = 0
    while step <= steps_number and len(rods[2]) < n:
        if n % 2 != 0:
            rng_i = [2, 1, 0]
            rng_j = []
            for i in rng_i:
                if i >= 1:
                    rng_j.append(i-1)
                else:
                    rng_j.append(2)
        else:
            rng_i = [1, 2, 0]
            rng_j = []
            for i in rng_i:
                if i < 2:
                    rng_j.append(i+1)
                else:
                    rng_j.append(0)
        for i,j in zip(rng_i, rng_j):
            k = 3 - (i + j)
            rods[i].append(rods[k].pop())
            ans += str(rods[0]) + ' ' + str(rods[1]) + ' ' + str(rods[2])
            ans += '\n'
            if len(rods[2]) == n:
                break
            step += 1
            if not rods[k]:
                rods[k].append(rods[j].pop())
            elif not rods[j]:
                rods[j].append(rods[k].pop())
            else:
                if rods[k][len(rods[k]) - 1] < rods[j][len(rods[j]) - 1]:
                    rods[j].append(rods[k].pop())
                else:
                    rods[k].append(rods[j].pop())
            ans += str(rods[0]) + ' ' + str(rods[1]) + ' ' + str(rods[2])
            ans += '\n'
            step += 1

    return ans.strip()




