def solution(num_list):
    even_sum = 0
    odd_sum = 0
    answer = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0 :
            even_sum += num_list[i]
        else: 
            odd_sum += num_list[i]
    
    print(even_sum)
    
    if(even_sum > odd_sum):
        answer = even_sum
    else:
        answer = odd_sum
    
    return answer 