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
- [0313 bintree_with_factors.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/MAR_2021#0313-binary-trees-with-factors)
- [0314 swap_nodes.py]()
- [0315 encode_and_decode.py]()
- [0316 stock_with_fee.py]()
- [0317 random_points_circle.py]()
- [0318 .py]()
- [0319 keys_and_rooms.py]()
- [0320 underground_system.py]()
- [0321 reordered_pow2.py]()
- [0322 vowel_spellchecker.py]()
- [0323 3sum_with_mult.py]()
- [0324 advantage_shuffle.py]()
- [0325 water_flow.py]()

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
- [코드 링크](https://github.com/Yuuraa/Python-Algorithm/blob/main/Leetcode/MAR_2021/bintree_with_factors.py)

### 0314 Swapping Nodes in a Linked List
- 문제: 링크드 리스트의 헤드와 k가 주어졌을 때, 첫번째부터 k번째 노드와, 마지막부터 k 번째 노드의 노드들을 바꾼 값을 출력하는 문제이다.
- 나의 풀이: 노드들을 리스트 형태로 저장해둔 뒤, 뒤에서 k번째 노드와 앞에서 k번째 노드가 연속된 경우와 그렇지 않은 경우를 분리해 스왑했다
- 다른 사람의 풀이: 링크드 리스트의 특징을 이용해 경우를 나누지 않고도 스왑했다

### 0315 Encode and Decode TinyURL
- 문제: URL을 입력하면, 작은 짧은 URL로 만들어 주어야 하는 알고리즘이다. URL을 인코딩하고 디코딩할 수 있게 만들기만 하면 된다
- 나의 풀이: Base62 인코딩 방식을 사용했다. URL 압축에 많이 사용되는 방식으로, 주어진 url에 고유한 숫자를 부여한 뒤, 그 숫자를 base62 방식으로 인코딩하되, 각 0~61 값마다 그에 해당하는 캐릭터를 대신 넣어 인코딩 된 것을 만든다
- 다른 사람의 풀이: 동일하게 풀었다

### 0316 Best Time to Buy and Sell Stock with Transaction Fee
- 문제: 주식을 사고 판다. 사고 나서 팔기 전에 또 사기를 할 수 없다. transaction fee가 있는 상황에서, 낼 수 있는 수익의 최댓값은 무엇일까?
- 나의 풀이: 풀지 못했다 ㅠ 시간 초과가 떴다
- 다른 사람의 풀이: dp와 sp 두개의 배열을 이용해 최댓값을 다이나믹 프로그래밍으로 풀었다

### 0317 Generate Random Point in a Circle
- 문제: 반지름과 원의 중심이 주어졌을 때, 원 내에서(boundary 포함) 균일하게 랜덤한 점을 뽑는 함수를 구하는 문제이다.
- 나의 풀이: 

### 0319 Keys and Rooms
- 문제: 각 방마다 방 안에 들어 있는 다른 방의 열쇠가 있다. 0번 방에서 시작하며 열쇠가 있는 방들을 방문, 새로운 열쇠를 얻는 과정을 반복했을 때, 모든 방을 방문할 수 있는지 푸는 문제
- 나의 풀이: 결국 방 내에 열쇠가 있는 것은 연결되어 있는 것이고, 그래프 문제를 풀 때처럼 DFS/BFS로 인접한 곳을 방문하며 풀면 된다고 생각했다. 나의 경우 DFS를 채택했다.
- 다른 사람의 풀이: 동일하게 풀었다

### 0320 Design Underground System
- 문제: UndergroundSystem class를 구현하는 문제. Station에 체크인하고, 체크아웃, 평균 체크인~체크아웃 시간 계산 등의 연산이 있다.
- 나의 풀이: 내부적인 dictionary를 만들어 각 사용자 id 별로 출발 지점과 출발 시각을 저장하고, 또다른 내부 딕셔너리에는 시작장소+끝장소 문자열의 합으로 이뤄진 키를 갖는 딕셔너리에 걸린 시간들을 배열로 저장해 두었다. 이 정보는 checkOut 마다 갱신하도록 했다.
- 다른 사람의 풀이: Counter를 이용했다.

### 0321 Reordered Power of 2
- 문제: 숫자 n이 주어졌을 때, digit들의 순서를 바꾸되, 맨 앞에 0이되지 않게 하면서 2의 제곱수를 만들 수 있는지 묻는 문제이다
- 나의 풀이: n의 digit들을 이용해 만들 수 있는 가장 큰 수까지, 2의 제곱 수의 크기를 늘려가면서 2의 제곱수에 들어 있는 digit들과 n에 들어 있는 digit들의 배열을 비교해 일치하면 참을 반환하고, 일치하는 것이 나오지 않았다면 거짓을 반환했다
- 다른 사람의 풀이: Counter를 이용해 str(N)에서 나온 digit들과 2의 제곱수에서 나온 digit들을 "any"를 이용해 비교했다. 사실 순서는 비교에 필요하지 않은 조건이니, Counter로 푸는 것이 더 합리적이고 깔끔해 보였다. 또한, 숫자에 제한을 걸지 않고 그냥 모든 0 ~ 30 까지의 제곱수를 모두 비교했다

### 0322 Vowel Spellchecker
- 문제: wordlist가 주어졌을 때, spellchecker를 이용해 올바른 단어로 만들려고 한다. 철자 오류는 대소문자 오류 또는 vowel error(a, e, i, o, u 중 잘못 사용하는 경우) 등이 있다.
- 나의 풀이: 문제를 조금 잘못 이해해서 가장 차이가 적은 단어를 예측하게끔 만들었었는데, 요구 사항과 맞지 않았다
- 다른 사람의 풀이: solve라는 함수를 짰고, 각 query에 대한 결과를 반환해주는 함수였는데 인상적이게도 map을 사용해 정답을 도출했다

### 0323 3Sum With Multiplicity
- 문제: array와 타겟 숫자가 주어졌을 때, 인덱스 i, j, k 로 이루어진 튜플의 갯수를 구하는 문제. i < j < k 이고, arr[i] + arr[j] + arr[k] == target 을 만족하면 된다. 정답값이 매우 커질 수 있으므로 mod 10^9 + 7 해준 값을 반환한다
- 나의 풀이: 일단 i, j, k 가 모두 다르기 때문에 순서를 고려하지 않고 숫자들을 Counter로 만든 뒤 활용하면 된다고 생각했다. 순서를 고려하며 순차적으로 풀 수도 있겠지만 그럴 경우 O(n^3) 이므로 시간 초과가 나게 된다고 생각했다. 카운터를 이용해 값을 센 뒤, 중복된 숫자가 3개 사용될 경우, 2개 사용될 경우, 모두 다른 것을 사용할 경우 세 가지 경우의 수로 고려해 문제를 풀었다.
- 다른 사람의 풀이: 

### 0324 Advantage Shuffle
- 문제: 동일한 크기의 배열 A와 B가 주어졌을 때, A[i] > B[i] 인 것이 A의 B에 대한 advantage 라고 한다. Advantage가 최대가 되는 A의 permutation을 반환하는 문제이다.
- 나의 풀이: 일단 A는 현재 순서를 보존하지 않아도 되므로 정렬하고, B는 인덱스를 포함하며 정렬했다. 가장 많은 advantage를 얻으려면 작은 값부터 순차적으로 매칭해 나가면 된다고 생각했고, 매칭 된 것들은 매칭된 B의 원래 인덱스에 배치했다. 매칭된 인덱스는 저장해 두었다가 매칭 완료 이후 남은 것들을 B에서 매칭되지 않은 자리로 돌려보냈다. 시간 복잡도는 O(nlogn)으로, 정렬시 발생한 것이고 이후 작업에서는 O(n)의 시간이 걸릴 것으로 예상된다. 공간 복잡도의 경우 O(n)으로 꽤 많은 공간을 잡아 먹은 것 같다
- 다른 사람의 풀이: a와 b를 모두 정렬한다는 점에서는 동일했지만, 인덱스를 저장하는 행위를 하지 않고 append를 해나가면서 진행했다.

### 0325 Pacific Atlantic Water Flow
- 문제: 맨 왼쪽과 맨 위의 pacific ocean과 맨 아래와 맨 오른쪽의 atlantic ocean이 있다. 해류는 자신보다 낮거나 같은 파도 높이를 가진 방향으로 흐를 수 있고, 해류들의 높이가 주어졌을 때 pacific ocean과 atlantic ocean으로 모두 흐를 수 있는 해류들의 위치를 반호나한다
- 나의 풀이: Flowed라는 0으로 초기화된 배열을 만든다. Pacific ocean부터 출발해서, BFS로 여기로 도달할 수 있는 해류에 대해서는 flowed 배열의 값을 1 더하고, Atlantic ocean에 대해서도 동일한 과정을 진행한다. flowed에서 값이 2가 되는 곳이 양쪽 바다로 모두 흐를 수 있는 해류이므로 해당 위치들을 배열로 반환한다
- 다른 사람의 풀이: 거의 동일하게 풀었다. DFS로 하는 접근법도 있었다.  