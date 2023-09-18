'''
문제) https://leetcode.com/problems/top-k-frequent-elements/submissions/

1) 문제 이해하기

정수 배열 숫자와 정수 k가 주어지면 가장 빈도가 높은 k개의 원소를 반환한다. (어떤 순서로든 답을 반환할 수 있다.)

2) 접근 방법
- collections 라이브러리를 사용한다.
  리스트의 각 원소와 해당 빈도값을 찾기에 쉬운 라이브러리
  2-1) Counter() 함수로 각 원소의 빈도값을 찾는다.
  2-2) most_common() 함수로 원하는 빈도 값을 가지는 원소를 찾는다.

'''

from collections import Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
    a = Counter(nums)
    li = []

    for i in range(k):
        li.append(a.most_common(k)[i][0])
    return li