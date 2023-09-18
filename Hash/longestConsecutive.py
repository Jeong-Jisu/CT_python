
'''
문제) https://leetcode.com/problems/longest-consecutive-sequence/

1) 문제 이해하기
정수 숫자의 정렬되지 않은 배열이 있는 경우 가장 긴 연속 요소 시퀀스의 길이를 반환한다. (O(n) 시간에 실행되는 알고리즘을 작성해야 한다.)


2) 접근 방법
-메모리  사용
  시간복잡도를 줄이기 위해 메모리를 사용하는 방법을 채택
  대표적으로 해시테이블


3) 코드설계
- 연속되는 수의 시작점 찾기
  연속되는 수가 시작하는 지점을 찾기위해 k-1의 값을 조사한다. k-1이 note(dict)에 없을 경우 k가 시작점임을 알 수 있다.

- 가장 긴 연속되는 수 찾기
  전역변수로 sum과 temp_sum의 길이 비교를 통해 가장 긴 연속되는 수를 업데이트한다.
'''



def longestConsecutive(nums: list[int]) -> int:

    sum = 0
    note = {}

    for v in nums:
        note[v] = True

    for k, v in note.items():
        # 시작점 찾기
        if k - 1 not in note:

            # k 자신에 대한 갯수 추가 +1
            temp_sum = 1
            while k + 1 in note:
                # 1-> 2-> 3-> ...
                k = k + 1
                temp_sum += 1

            # 가장 긴 연속적인 값으로 update
            if temp_sum > sum:
                sum = temp_sum
    return sum

