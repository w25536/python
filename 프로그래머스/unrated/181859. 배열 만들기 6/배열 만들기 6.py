def solution(arr):
    stk = []
    
    for num in arr: 
        if not stk:
            stk.append(num)
        elif stk[-1] == num:
            stk.pop()
        else:
            stk.append(num)
    
    return stk if stk else [-1]


#Push - Add an element to the top of the stack.
#Pop - Remove and return the top element from the stack.
#Peek/Top - View the top element without removing it.
#isEmpty - Check if the stack is empty.