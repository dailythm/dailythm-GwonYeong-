# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score),m):
        if i+m > len(score):
            break
        answer += min(score[i:i+m]) * m
    return answer