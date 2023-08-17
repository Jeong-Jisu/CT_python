'''
문제) https://leetcode.com/problems/two-sum/submissions/

1) 문제 이해하기

정수가 저장된 배열 nums 이 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target이 될 때, 해당 인덱스를 리턴하고
 불가능하면 [-1,1]를 반환하세요. 같은 원소를 두 번 사용할 수 없습니다.


2) 접근 방법
-메모리  사용
  시간복잡도를 줄이기 위해 메모리를 사용하는 방법을 채택
  대표적으로 해시테이블

3) 코드설계
dict 객체 (memo)를 하나 선언한다.
for 문을 통해 find를 정의하고 만약 find가 memo안에 없으면 memo의 인덱스는 nums의 숫자로, value는 nums의 인덱스로 채워서 저장하고
만약 find가 memo에 있을 경우 memo[find], i(index)를 반환한다.

총 O(n) 시간 복잡도 소요
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
    memo = {}  # 딕셔너리 선언

    for i, v in enumerate(nums):
        find = target - v

        if find in memo:  # 이 부분이 중요하다. in nums가 아니라 in memo를 함으로 O(n) -> O(1)로 변경된다.
            return [memo[find], i]
        else:
            memo[v] = i

    return [-1, 1]