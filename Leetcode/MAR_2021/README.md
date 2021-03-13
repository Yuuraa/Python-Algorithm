### 3월 문제 풀이 목록
- [0301_distribute_candies.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0301-distribute-candies)
- [0302_set_mismatch.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0302-set-mismatch)
- [0303 missing_nums.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0303-missing-number)
- [0304 intersect_linked_list.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0304-intersection-of-two-linked-lists)
- [0305 average_bintree.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0305-average-of-levels-in-binary-tree)
- [0306 short_encoding.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0306-short-encoding-of-words)
- [0307 design_hashmap.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0307-design-hashmap)
- [0308 remove_palindrome.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0308-remove-palindromic-subsequences)
- [0309 add_tree_row.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0309-add-one-row-to-tree)
- [0310 int_to_roman.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0310-integer-to-roman)
- [0311 coin_change.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0311-coin-change)
- [0312 has_all_bincode.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0312-check-if-a-strig-contains-all-binary-codes-of-size-k)
- [0313 bintree_with_factors.py]()

### 0301 Distribute Candies
- 문제: 전체 캔디 수의 절반 만을 먹을 수 있는 앨리스가, 먹을 수 있는 캔디 종류의 최댓값을 구하는 문제
- 나의 풀이: 간단히, 캔디 종류의 수와 n//2 중 더 적은 값이 먹을 수 있는 종류 수의 최댓값이라고 풀었다.
- 다른 사람의 풀이: 캔디 종류 수를 구할 때 set 대신 Counter를 사용했다
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/0301_distribute_candies.py)

### 0302 Set Mismatch
- 문제: 원래 배열에는 1 ~ n 의 숫자가 모두 포함되어 있다. 하지만, 한 숫자가 중복되어 원래 있어야 할 숫자를 대체하고 있다. 중복된 숫자와 손실된 숫자를 묶어 반환하는 문제
- 나의 풀이: 아주 간단한 문제라고 생각했다. Counter로 세서 1개가 넘어가는 것을 일단 duplicated로, set으로 1~n 사이 중 존재하지 않는 숫자를 구했다.
- 다른 사람의 풀이: 수학적으로 풀었다. 총합과 제곱 총합을 이용해 풀었다.
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/0302_set_mismatch.py)

### 0303 Missing Number
- 문제: 0 ~ n 사이의 숫자로 채워져야 하는 배열인데, 하나의 숫자가 제외된 배열이 주어졌을 때, 빠진 숫자가 무엇인지 맞추는 문제
- 나의 풀이: Bitwise exclusive or 연산을 사용하면 x ^ x = 0이고, 0 ^ x = x라는 특성을 이용해 0 ~ n사이 전체 숫자에 ^ 연산을 하고, 그 값에 주어진 배열 안에 있는 모든 원소들과 ^ 연산을 진행해 풀었다
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/missing_number.py)

### 0304 Intersection of Two Linked Lists
- 문제: 특정 지점부터 합쳐질 수도 있는 두 개의 Linked List가 주어졌을 때, 만약 두 Linked List가 합쳐진다면 합쳐지는 부분의 노드를 반환하는 문제. 공간복잡도 O(1), 시간복잡도 O(n)으로 풀어야 한다
- 나의 풀이: 일단 두 개의 linked list를 모두 끝까지 순회하면서 길이를 구하고, 더 긴 쪽은 차 만큼 next연산을 해 주어 남아 있는 길이를 맞춰 주었다. 이후 next연산을 하며 노드가 일치하는 곳이 발생하면 그 노드를 반환해 주었다. 끝까지 갔음에도 반환이 안된 경우 None 값을 반환했다.
- 다른 사람의 풀이: 천재적으로 푼 것 같다! ListA가 A + 공통, ListB가 B + 공통 부분이라고 할 때, 이 사람의 풀이대로 처음엔 listA의 포인터로 쓰던 것을 B의 포인터로, B의 포인터로 쓰던 것을 A의 포인터로 활용하게 되면 공통 부분까지 가는 데 A + 공통부분 + B 혹은, B + 공통부분 + A 만큼의 시간만 들게 된다. 만약 공통 부분이 없어서 None이더라도, 이는 동일하게 None으로 가기 때문에 두 포인터의 값이 같아진다
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/intersect_linked_list.py)

### 0305 Average of Levels in Binary Tree
- 문제: 트리의 각 층에서 값들의 평균을 내야 한다
- 나의 풀이: 트리를 순회하면서, 깊이에 따른 노드 리스트를 딕셔너리에 저장하고 깊이 별로 순회하며 평균을 낸 값을 정답 리스트로 만들었다
- 다른 사람의 풀이: 나의 경우 DFS 접근법 인데, BFS로 푼 분도 계셨다.
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/average_bintree.py)
### 0306 Short Encoding of Words
- 문제: 단어들의 배열이 주어졌을 때, 해당 단어들을 합쳐 인코딩 한 결과물의 최소 길이를 반환하는 문제. 단, 각 단어 별로 인코딩 된 문장에서의 시작 위치가 있어야 하고, 단어 별로 시작 위치부터 #이 나오기까지가 그 단어와 일치해야 함. ex) ["time", "me", "bell"] => "time#bell#", [0, 2, 5]
- 나의 풀이: 한 단어가 다른 단어의 뒷부분과 일치하면(끝부터), 들어가지는 단어는 직접 분리해 쓰지 않아도 된다고 생각했다. 그래서 인코딩 할 때 쓰일 단어들의 셋을 따로 만들었다.단어들을 뒤집어서 정렬하고, 앞에 나온 단어가 뒤에 나온 단어에 포함될 수 있는지를 확인했다. 만약 포함이 된다면 인코딩할 때 쓰일 단어 집합에서 뺐다. 어차피 길이를 구하는 것이기 때문에, 따로 다시 변환해주지 않았다. #을 기준으로 합쳐졌을 때 길이가 어떻게 되는지를 구했는데, 다시 생각해보니 그냥 쓰일 단어들의 수 + 쓰일 단어들의 길이 합으로 구했어도 될 것이다. 시간 복잡도는 정렬할 때 드는 O(nlogn) 일 것이다. (이후 비교 시에는 O(n)의 시간이 든다)
- 다른 사람의 풀이: **Trie solution**이 있었다. Trie란 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조이다. O(M*L) 시간이 든다(L은 단어의 최대 길이). 
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/short_encoding.py)

## 0307 Design HashMap
- 문제: 해쉬맵을 직접 클래스로 만들어 보는 문제
- 나의 풀이: key와 value에 대해 매칭되는 쌍끼리 같은 index를 갖도록 하고 각자 배열을 만들어 저장함
- 다른 사람의 풀이: (key, value) 쌍으로 이루어진 배열을 만듦
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/design_hashmap.py)
### 0308 Remove Palindromic Subsequences
- 문제: 문자 a와 b로 이루어진 문자열 s가 주어졌을 때, 한 번에 하나의 palindromic subsequence를 제거하면서 최종적으로 빈 문자열이 될 때까지 걸리는 최소 횟수를 구하는 문제
- 나의 풀이: 다른 사람들의 것과 동일한데, substring이었다면 어려운 문제였겠지만, subsequence이기 때문에 palindromic string이 아니라면 처음에 a를 모두 제거하고 뒤에 b를 모두 제거하면 된다. 빈 문장은 0, 길이가 1이거나 palindrome이면 1, 아니면 2를 반환하면 된다.
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/remove_palindrome.py)

### 0309 Add One Row to Tree
- 문제: TreeNode 자료형에 하나의 row를 추가해야 한다. Row에 새로 들어갈 값과, 몇 번째 row에 들어갈지 v, d 인자가 원본 TreeNode의 root와 함께 주어진다. 만약 d = 1이라면 맨 위에 추가하고 원본 root를 left child로 만든다. 이외의 경우에는, d 번째 층에 있는 모든 노드들에 대해 왼쪽과 오른쪽에 v 값을 가진 노드를 추가하고, 왼쪽 새 노드의 왼쪽 자식을 원본의 왼쪽 자식으로, 오른쪽 새 노드의 오른쪽 자식을 원본의 오른 쪽 자식 노드로 설정한 뒤 새로운 트리를 반환한다
- 나의 풀이: 정직하게 풀었고, DFS 형식으로 더 깊은 층으로 들어가면서 curr_depth 가 d-1과  일치한다면 TreeNode를 삽입했다. d = 1인 경우는 따로 처리해 주었다
- 다른 사람의 풀이: 전체 add_one_row 함수를 DFS 로 활용했다. 만약 d를 오히려 감소시켜주면서 깊이 들어갔다.
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/add_tree_row.py)

### 0310 Integer to Roman
- 문제: 정수 값이 들어오면, 이를 로마 문자 형태로 바꾼다
- 나의 풀이: 1, 10, 100, 1000으로 이루어진 ones와 5, 50, 500으로 이루어진 fives 배열을 만들고, 각 자리수를 뒤 부터 돌며 자리수에 맞게 로마형 값을 추가해 나갔다
- 다른 사람의 풀이: digit이라는 함수를 새로 추가해 간단하게 문자를 반환할 수 있게 했다
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/int_to_roman.py)

### 0311 Coin Change
- 문제: 해당 량의 돈을 얻기 위해, 사용할 수 있는 가장 적은 수의 동전을 사용해 값을 만드는 문제이다
- 나의 풀이: 처음에는 무조건 큰 동전들을 많이 사용하다가 불가능하면 수를 점점 줄여가며 거의 모든 경우의 수를 탐색하게끔 풀었다. 이 방법은 시간초과가 났고, 다시 생각해보니 동전의 가능한 갯수 가짓수가 각 동전 별로 10^4 까지 될 수 있기 때문에, DP 같은 방식을 적용해야 한다고 생각했다. 이미 탐색한 amount라면 해당 값을 반환하게 한 것이다. 길이가 예상되지 않기 때문에 dict 자료형으로 값을 저장해 두었다
- 다른 사람의 풀이: lru_cache 라는 것을 활용했다. @lru_cache는 functools에서 제공하는 데코레이터의 일종으로, 메모이제이션을 해서 인자로 넘겨준 maxsize갯수 만큼이 가장 최근 호출들을 저장해 둔다. Expensive, I/O bound한 함수들이 동일한 argument로 주기적으로 호출될 때 유용하게 사용할 수 있다고 한다. 이를 사용하니 따로 메모이제이션을 할 딕셔너리를 만들어주지 않고도 손쉽게 DP 구현이 가능했다.
    - 공식 도큐먼트는 [이곳](https://docs.python.org/3/library/functools.html)이다
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/coin_change.py)

### 0312 Check If a String Contains All Binary Codes of Size K
- 문제: binary string s 와 integer k가 주어졌을 때, k길이로 이루어진 모든 binary code가 모두 s의 substring이 될 수 있는지 여부를 반환한다
- 나의 풀이: O(N) 까지는 수용 가능한 길이의 s가 주어지므로, s를 한 번 순회하며 k 길이 만큼씩을 잘라 substring의 set에 추가했다. set의 원소의 수가 2**k와 같아지면 전부 표현 가능한 것이니 이를 반환하게 했다
- 다른 사람의 풀이: 해쉬를 이용했다. 이해할 수 없었따..ㅠㅠ
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/has_all_bincode.py)

### 0313 Binary Trees With Factors
- 문제: 숫자들의 배열이 주어졌을 때, 한 숫자를 한 번 이상 사용해 배열 내의 다른 숫자를 만들 수 있다면 이를 트리 형태로 나타낼 수 있다. Binary tree형태로 배열 내 두 개의 같거나 다른 숫자를 곱해 만들 수 있는 숫자들을 표현하는 것의 갯수를 구하시오
- 나의 풀이: 숫자들을 크기 순으로 정렬한 뒤, 자신보다 이전에 나왔던 숫자들 중 나누어 떨어지는 것이 있는지, 나누어 떨어진다면 그 몫도 숫자들에 들어가 있는지를 확인한다. 2, 5 -> 10 이라면 2, 5에서 한 번, 5, 2에서 한 번 더해주므로 각 나눠지는 숫자들의 경우의 수의 곱을 발견할 때마다 더해주며, dp로 저장해 두어 사용한다
- 다른 사람의 풀이: 동일한 방식으로 풀었는데, xrange라는 기능을 사용했다. 조사해보니, range는 리스트 타입을 반환하는 반면, xrange는 고정된 크기의 xrange 타입을 반환하는데, 이는 자신에 속한 데이터값을 한꺼번에 메모리에 로드하는 것이 아니라 해당 값에 접근할 때마다 그 값을 하나씩 로딩하는 방법이라고 한다. Generator의 yield를 사용했을 때와 비슷한 효과라고 생각하면 된다.