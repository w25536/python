def solution(my_string):
    return ''.join([my_string[x] for x in range(len(my_string)-1,-1,-1)])