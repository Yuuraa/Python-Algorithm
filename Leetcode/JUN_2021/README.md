# Leetcode 2021 6월 문제 풀이 목록
- [0622 num_matching_subseqs.py]()
- [0623 reversed_linked_list_2.py]()

### 0622 Number of Matching Subsequences
문자열 s와 다른 문자열들의 배열 w가 주어졌을 때, w 내에서 s의 subsequence인 문자열들의 수를 세는 문제.

처음에는 LCS(Longest Common Subsequence) 푸는 방식으로 접근했는데, 시간 초과가 났고 LCS의 길이가 중요한 것이 아니라, 문자열 그 자체가 subsequence인지 아닌지를 판단하는 문제이기 때문에 다른 풀이를 해야 했다. 
- 시간 초과가 난 이유는 DP 문제이지만 한 쌍의 문자열을 비교할 때마다 O(mn)의 시간을 써야 하고 (m, n은 두 문자열 길이), 이걸 w내 단어의 수 k만큼 반복하면 O(mnk)가 되기 때문이다.
- s의 길이는 최대 50000, 단어의 길이가 50, 갯수가 최대 5000개이므로 최대 125*10^8까지 복잡해진다
다음 풀이에서는 w내 비교할 문자열을 stack으로 보고, s와 비교 문자열을 뒤부터 순회하며 겹치는 element가 있다면 stack에서 element를 빼고, 아니라면 s의 앞 문자를 비교한다. 만약 subsequence의 조건을 만족하면 도중에 그만두고, 아닌 경우 s를 맨 처음까지 확인한다. 
- 따라서 한 쌍의 문자열을 비교할 때 O(m)의 시간을 소요하게 된다 (m은 s의 길이)
w내 겹치는 문자열에 대해서는 Counter를 사용해 반복 계산이 없도록 했다

### 0623 Reversed Linked List II
