# https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    answer = []
    i = 2
    while n >= i:
        if(n % i == 0):
            if i not in answer:
                answer.append(i)
            n /= i
        else:
            i +=1
            
    return answer