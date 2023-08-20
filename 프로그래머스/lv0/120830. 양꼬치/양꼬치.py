def solution(n, k):
    yakitor_price = 12000
    drink_price = 2000
    free_drinks = n // 10 
    
    answer =   n * yakitor_price + drink_price * k - drink_price * free_drinks
    return answer