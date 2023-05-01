from heapq import heappop, heappush

def solution(program):
    answer = [0 for _ in range(11)]
    H = []
    program.sort(key=lambda x:(x[1], x[0]))
    heappush(H, (program[0][0], program[0][1], program[0][2]))
    idx = 1
    time = program[0][1]
    while True:
        score, start, end = heappop(H)
        if idx != 1:
            answer[score] += (time-start)
        time += end
        if idx > len(program)-1 and not H:
            break
        while True:
            if idx <= len(program)-1 and program[idx][1] <= time:
                heappush(H, (program[idx][0], program[idx][1], program[idx][2]))
                idx += 1
            else:
                break
        if idx <= len(program)-1 and not H:
            heappush(H, (program[idx][0], program[idx][1], program[idx][2]))
            time = program[idx][1]
            idx += 1
            continue
    answer[0] = time
    return answer

# solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]])
# solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]])
solution([[1, 1, 2], [2, 4, 2], [3, 7, 1]])