# LeetCode 4월 문제 풀이 목록
- [0401 linked_palindrome.py]()
- [0402 ones_and_zeros.py]()
- [0403 longest_parenthesis.py]()
- [0404 circular_queue.py]()
- [0405 global_local_inversions.py]()


### 0401 Palindrome Linked List
- 문제: 링크드 리스트가 주어졌을때, 그 값들이 palindromic 한지 참 거짓을 반환하는 문제
- 나의 풀이: O(n) 공간 복잡도, O(n) 시간 복잡도. 값들을 배열에 저장해두고 left, right 포인터로 양 끝부터 보며 값이 같은지 다른지를 보았다
- 다른 사람의 풀이:


### 0402 Ones and Zeros
- 문제: 



### 0403 Longest Valid Parenthesis
 - 문제: "("와 ")"로 이루어진 문자열 s 가 주어졌을 때, s 내에서 가장 긴 길이의 유효한 Parenthesis를 구하는 문제
 - 나의 풀이: 
 - 다른 사람의 풀이: DP 문제로 풀었고, dp를 위해 따로 저장하지 않고 함수를 사용하였으나 lru_cache를 통해 자동으로 캐싱이 이뤄지게 만들어 배열을 이용하지 않고도 시간 효율을 냈다

### 0404 Design Circular Queue
- 문제: Circular Queue 클래스를 구현하는 문제
- 나의 풀이: val들을 담는 고정 길이의 배열과 그 배열의 길이를 나타내는 max_len, circular queue의 시작점을 알리는 head, 길이를 나타내는 length를 변수로 가진 클래스를 구현했다

### 0405 Global and Local Inversions
- 문제: 0 ~ N-1 사이의 순열인 A가 있을 때 global한 inversion의 갯수와(i< j 에 대해 i와 j 비교) local한 inversion의 갯수(i와 i+1 비교)가 같은지 여부를 반환한다
- 나의 풀이: O(N)의 시간이 걸리도록 local inversion의 수와 global inversion의 수를 셌다.