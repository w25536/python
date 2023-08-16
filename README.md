# python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)




vim _

// space를 tab으로
:%s/    /\t/g
 
// tab을 space로
:%s/\t/    /g


문자열 

```python
import re

def solution(myString, pat):
    return len(re.findall(f'(?={pat})', myString))
```
```python

def solution(myString, pat):
    index = myString.rfind(pat)
    return myString[:index + len(pat)]
```
```python

from collections import defaultdict

def solution(strArr):
    length_count = defaultdict(int)
    
    for s in strArr:
        length_count[len(s)] += 1
        
    return max(length_count.values())
```
defaultdict를 사용해 문자열의 길이를 키로 하고 그 길이를 가진 문자열의 개수를 값으로 하는 사전을 생성합니다

```python
import re

def solution(myStr):

    splits = re.split('[abc]', myStr)
    answer = [s for s in splits if s]

    return answer if answer else ['EMPTY']
```
