def divisor(n):
    divisor_list=[]
    for i in range(1, n+1):
        if n % i ==0:
            divisor_list.append(i)
    return divisor_list

def solution(n):
    return len([num for num in range(1,n+1) if len([i for i in range(1, n+1) if num % i == 0]) >= 3]) 