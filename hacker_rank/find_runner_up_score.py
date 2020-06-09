"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(arr)

    max_score = max(lst)
    runner_up_score = 0
    lst = [x for x in lst if x < max_score]
    print(max(lst))
