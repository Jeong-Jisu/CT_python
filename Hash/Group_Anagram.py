'''
문제) https://leetcode.com/problems/group-anagrams/

1) 문제 이해하기
문자열의 배열이 주어지면 아나그램을 함께 그룹화한다. (어떤 순서로든 답을 반환할 수 있다.)
* 애너그램(Anagram)은 다른 단어나 구의 글자들을 재배열하여 형성된 단어나 구로서, 일반적으로 모든 원래의 글자들을 정확히 한 번 사용합니다.

2) 접근 방법
-메모리  사용
  시간복잡도를 줄이기 위해 메모리를 사용하는 방법을 채택
  대표적으로 해시테이블

- 같은 애너그램 그룹화
  1) 각 단어들을 분해해서 될 수 있는 조합을 for문으로 모두 찾는다 -> 큰 시간복잡도를 가질 것이라 현실적으로 불가. (채택 불가)
  2) 각 단어의 알파벳을 리스트로 분해한 후 sort해서 뭉치고, dictionary를 사용하자. -> 1) 보다 훨씬 적은 시간복잡도 예상 (채택)
    2-1) 중복된 단어(대표단어)가 key에, 원 문자열이 values에 들어가도록 설계.

'''

def groupAnagrams(strs: list[str]) -> list[list[str]]:

    note = {}

    for word in strs:
        uniq_word = ''.join(sorted(list(word)))
        if uniq_word in note:
            note[uniq_word].append(word)
        else:
            note[uniq_word] = [word]
    return list(note.values())