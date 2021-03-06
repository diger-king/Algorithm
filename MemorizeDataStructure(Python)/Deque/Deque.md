# Deque

[DataStructure 1. Stack](https://diger-king.github.io/blog/Stack)

[DataStructure 2. Queue](https://diger-king.github.io/blog/Queue)

## Deque - 개념

![Image](https://miro.medium.com/max/1400/1*hCjc5SBvcu98wMkJYAD2xg.png)

기본 개념은 큐랑 똑같다.

그치만 삽입/삭제를 양방향으로 가능하다는 차별점이 있다.

Deque 는 Append, Pop 이 list 에 비해 압도적으로 빠르다.

### Append Time Complexity
List : O(n)
Deque : O(1)

### Pop Time Complexity
List : O(n)
Deque : O(1)

## Deque - 사용법

    from collections import deque

    deque = deque()

    ##############################################

    # Insertion Into Deque (Default = Right side)

    deque.append(1.1)
    deque.append(1)
    deque.append("1")

    ##############################################

    # Insertion Into Deque (Left side)
    deque.appendleft(1.1)
    deque.appendleft(1)
    deque.appendleft("1")

    ##############################################

    # Pop Deque (Default = Right side)
    deque.pop()

    ##############################################

    # Pop Deque (Left side)
    deque.popleft()

    ##############################################

    # Array To Deque (Default = Right side)
    deque.extend(list)
    
        ## print example
        list = ["11", 2.2, 33 , 44, 55]
        deque.extend(list)
        print(deque)
        -> deque(['11', 2.2, 33 , 44, 55])

    ##############################################

    # Array To Deque (Left Side)
    deque.extendleft(list)
    
        ## print example
        list = ["11", 2.2, 33 , 44, 55]
        deque.extendleft(list)
        print(deque)
        -> deque(['11', 2.2, 33 , 44, 55]]

    ##############################################

    # Remove Element
    deque.remove(item)

    ##############################################

    # Rotate Deque
    deque.rotate(num)
    
        ## num < 0
        해당 수 만큼 왼쪽으로 밀기

        ## num > 0
        해당 수 만큼 오른쪽으로 밀기

---

Push/Pop 연산이 빈번한 경우에는 Deque를 사용하자.