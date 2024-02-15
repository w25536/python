def solution(score):
    answer = []

    averages = [(s[0] + s[1]) / 2 for s in score]

    indexed_averages = list(enumerate(averages))

    sorted_averages = sorted(indexed_averages, key=lambda x: -x[1])
    
    ranks = [0] * len(score)
    current_rank = 1
    for i, (index, _) in enumerate(sorted_averages):
        if i > 0 and sorted_averages[i][1] == sorted_averages[i - 1][1]:
            
            ranks[sorted_averages[i][0]] = ranks[sorted_averages[i-1][0]]
        else:
            ranks[index] = current_rank
        current_rank += 1
    
    return ranks