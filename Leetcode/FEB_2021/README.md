# LeetCode 2월 문제 풀이 목록
- [0201 num_one_bits.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0201-number-of-1-bits)
- [0202 trim_bin_tree.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0202-trim-a-binary-search-tree)
- [0203 linked_list_cycle.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0203-linked-list-cycle)
- [0204 longest_harmonious_subseq.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0204-longest-harmonious-subsequence)
- [0205 simplify_path.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0205-simplify-path)
- [0206 bintree_rightside.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0206-binary-tree-right-side-view)
- [0207 shortest_to_character.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0207-shortest-distance-to-a-character)
- [0208 peeking_iterator.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0208-peeking-iterator)
- [0209 greater_tree.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0209-convert-bst-to-greater-tree)
- [0210 copy_rand_list.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0210-copy-list-with-random-pointer)
- [0211 valid_anagram.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0211-valid-anagram)
- [0212 steps_to_zero.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0212-number-of-steps-to-reduce-a-number-to-zero)
- [0213 shortest_clear.py]https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0213-shortest-path-in-binary-matrix)
- [0214 bipartite_graph.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0214-is-graph-bipartite)
- [0215 k_weakest_rows.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0215-the-k-weakest-rows-in-a-matrix)
- [0216 letter_case_permut.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0216-letter-case-permutation)
- [0217]()
- [0218 arithmetic_slices.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0218-arithmetic-slices)
- [0219 make_valid_parentheses.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0219-mimimum-remove-to-make-valid-parentheses)
- [0220 roman_to_int.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0220-roman-to-integer)
- [0221 broken_calculator.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0221-broken-calculator)
- [0222 longest_word.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0222-longest-word-dictionary-through-deleting)
- [0223 search_2d_mat.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0223-search-2d-matrix-ii)
- [0224 parentheses_score.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0224-score-of-parentheses)
- [0225 unsorted_subarray.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021#0225-score-of-parentheses)
- [0226 validate_stack.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021/#0226-validate-stack-sequences)
- [0227 divide_integers.py](https://github.com/Yuuraa/Pyhton-Algorithm/tree/main/Leetcode/FEB_2021/#0227-divide-two-integers)
- [0228 max_freq_stack.py](https://github.com/Yuuraa/Python-Algorithm/tree/main/Leetcode/FEB_2021/#0228-maximum-frequency-stack)


### 0201 Number of 1 Bits 
- 문제: 숫자가 주어졌을 때, 해당 숫자의 binary 표현(2의 보수 표현)에서 1의 갯수를 셈
- 나의 풀이: 파이썬의 라이브러리를 사용함
- 다른 사람의 풀이: 
    1. bit 을 움직여가면서 & 연산을 했고, 0이 아니라면 count를 증가시키는 방법
    2. n & (n-1)을 하면서 n이 0이 아닐 동안 진행하는 방법
- 아쉬운 점: 입력값이 특이하다 보니 직접 테스트 해볼 수 없었다

### 0202 Trim a Binary Search Tree
- 문제: Tree와 low, high 값이 주어졌을 때, 트리의 노드 중 값이 low와 high 사이에 들어 있지 않은 것을 빼야 한다
- 나의 풀이: dfs를 이용해 curr과 left와 right를 업데이트 해주었다
- 아쉬운 점: Binary search tree이기 때문에, 값들이 root를 기준으로 왼쪽은 더 작은 값들, 오른 쪽은 더 큰 값들이 있을 것이라는 걸 계산하지 못했다. 조건이 이렇게 안주겠거니 하는 생각은 있었지만.. 이를 적절히 활용하지 못했음

### 0203 Linked List Cycle
- 문제: 리스트 내에 사이클이 존재하는지 판별하는 문제이다.
- 나의 풀이: 노드의 갯수가 10^4개로 한정되어 있었기 때문에, 만약 현재 노드가 None이 아니고 next를 넘긴 횟수가 10^4 이하일 동안 계속 curr.next를 해주어 다음 노드로 넘어갔다. 사이클이 없다면 curr = None인 상태에서 끝나게 되므로 마지막에 curr != None을 리턴하여 사이클이 있다면 True를 반환하게 했다. 날로 먹기다.
- 다른 사람의 풀이: fast와 slow를 두고 두 개가 일치하게 되는 때가 있는지를 보았다. 언젠가는 겹치는 때가 생기는 것 같다 (이게 문제가 원한 풀이)

### 0204 Longest Harmonious Subsequence
- 문제: 리스트 내의 subsequence중 최댓값과 최솟값의 차가 정확히 1이 되는 subsequence의 길이를 찾아야 한다.
- 나의 풀이: 일단 list 내에 있는 모든 숫자들의 수를 세고, n이 있고 만약 n + 1 도 리스트 내에 있는 경우 n의 갯수와 n + 1의 갯수의 합의 최댓값을 답으로 한다. 좀 날로 먹은 것 같다
- 다른 사람의 풀이: 똑같이 풀었는데, 훨씬 멋지게 풀었다


### 0205 Simplify Path
- 쉘에 경로에 대한 문자열이 들어왔을 때, 이를 단순화 하는 과정이다.
- 나의 풀이: 정규표현식을 사용해 //가 두개 이상인 경우를 처리했고, 맨 오른쪽의 "/"를 없앴다. 쌓이는 경로들을 스택으로 처리했다. ..이 들어오면 스택에서 pop해주는 식이었다. 마지막에는 맨 앞에 "/"를 추가하고 파일 명 사이에 "/"를 두면서 하나의 문자열로 합쳤다.
- 다른 사람의 풀이: 생각해보니 "/"로 split할 것이므로 굳이 두 개짜리를 처리해주지 않아도 됐다... 하지만 아이디어는 똑같다!

### 0206 Binary Tree Right Side View
- 문제: 이진 트리를 오른쪽에서 본 값을 높이 별로 리스트에 담는 문제다
- 나의 풀이: 탐색을 하면서 왼쪽 먼저 탐색하게 하되, 이진 트리 내의 높이 별로 리스트를 만들고 트리 노드의 값을 담았다. 이후 각 리스트의 맨 마지막 원소가 해당 높이에서 가장 오른쪽에 있는 원소가 된다. DFS로 들어갔다
- 다른 사람의 풀이: 나처럼 dfs로 들어갔는데, 오히려 오른쪽 먼저 보게 해서 해당 높이에서 본 값이 없으면 이걸 맨 오른쪽 값이라고 쳤다! 이게 더 나은 듯 하다

### 0207 Shortest Distance to a Character
- 문제: 문장과 타깃 문자 c가 주어졌을 때, 문자열 내의 각 위치의 문자들로부터 c까지의 최소 거리를 구해 리스트로 반환한다.
- 나의 풀이: 우선 c의 모든 위치들에 대한 배열을 만들었고, 문자열을 돌며 만약 문자가 c와 일치하면 0, 아니라면 c 위치 리스트와 문자의 위치 사이 차의 최솟값을 구했다. 최솟값을 구할 때 c의 인덱스들 내에서 이진 탐색을 수행해 가장 가까운 양 옆의 두 index들과 현재 문자의 위치를 비교했다.
- 다른 풀이: O(N)으로 풀었다. 사실 나도 O(N)이기는 하지만, 좀 덜 효율적인 것 같다. 방법은 앞에서 뒤로 보면서 그 방향에서의 최소 거리를 처리한 후, 뒤에서 앞으로 보며 최소 거리를 다시 업데이트 하는 방식이다. 훨씬 효율적이다!


### 0208 Peeking Iterator
- 문제: 다음에 나올 요소를 미리 보기 할 수 있는 iterator를 만든다. 미리보기 하는 것은 iterator 그 자체의 next에는 영향을 주지 않는다. 미리 정의된 Iterator class가 있는 재미있는 구현 문제였다
- 나의 풀이: peeking하고 있는 지 여부와 curr_val을 내부에 저장해두었다

### 0209 Convert BST to Greater Tree
- 문제: BST를 순회하면서, 해당 노드의 값 이상의 값들을 모두 해당 노드의 값에 더해주는 문제이다
- 나의 풀이: 노드를 방문하는 규칙으로 inorder를 반대로 한, 즉 오른쪽 -> 노드 -> 왼쪽 순으로 방문하는 DFS 코드를 작성했다. 노드의 오른쪽에는 무조건 해당 노드보다 큰 값들이 존재하기 때문에, 해당 노드들을 순회하면서 모든 값을 합친 값을 내보내야 하고, 노드의 왼쪽에는 해당 노드의 값이 합쳐진 값을 더해주어야 하기 때문이다. 처음에는 스택 형태로 짰다가, visited를 처리해 줄 방식이 떠오르지 않아 재귀함수로 수정했다.
- 다른 사람의 풀이: 똑같은 방식으로 했는데, self.totalval을 두어 계산을 보다 쉽게 했다


### 0210 Copy List with Random Pointer
- 문제: 각 노드 별로 next와 random 포인터를 갖고 있는 노드들로 이루어진 링크드 리스트를 복제해 내는 문제다
- 나의 풀이: 원본 링크드 리스트에서 노드와 랜덤 노드, 등 복제가 이루어진 노드들의 원본을 저장하는 리스트와 복제본을 저장하는 리스트 두 개의 리스트를 갖고 있었다. 원본 리스트에서 점차 next로 넘어가는데, 각 노드 별로 이미 해당 노드가 리스트에 있다면 new_node에서 원본 노드를 담은 것과 동일한 위치의 노드를 현재 노드의 복사본인 의미로 curr_new로 설정했다. 없다면 양쪽 리스트에 모두 노드들을 새롭게 추가했다. 즉, 두 개의 노드 리스트를 쓰므로 공간복잡도와 시간복잡도 모두 O(n)을 따른다.


### 0211 Valid Anagram
- 문제: 문자열 s와 t가 주어졌을 때, t가 s의 anagram인지를 확인한다(구성 문자가 같은 문자열)
- 나의 풀이: Counter를 활용했다. 무척 간단한 문제였다
- 다른 사람의 풀이: 정렬 후 같은지를 비교했다


### 0212 Number of Steps to Reduce a Number to Zero
- 문제: 홀수에는 -1, 짝수에는 /2 연산을 하면 주어진 수를 0까지 만드는 데 몇 번의 연산이 필요한지 묻는 문제
- 나의 풀이: 2로 나누는 횟수는 이진수 표현을 했을 때 자릿수와, 중간에 홀수가 되는 횟수는 이진수 표현을 했을 때 1의 수와 관련 되었다고 생각했다. 두 수를 더하면 정답에 1이 더해진 수가 나오기 떄문에 -1 해주었다 (조금 날로 먹기?)


### 0213 Shortest Path in Binary Matrix
- 문제: 0으로 이루어진 칸만 밟으며 맨 끝깐카지 도달하는 경로의 최소 길이를 묻는 문제
- 나의 풀이: DFS로 시도했지만 시간 초과가 남
- 남의 풀이: BFS로 깔끔하게 풀었음

### 0214 Is Graph Bipartite?
- 문제:
- 나의 풀이:

### 0215 The K Weakest Rows in a Matrix
- 문제: 0, 1로 구성된 행렬이 주어졋을 때, 0의 수가 가장 적으면서, index가 더 작은 것이 약한 row이다. k번째로 약한 row를 반환하면 된다
- 나의 풀이: row개의 (row_id, soldier_num) 으로 이루어진 배열을 하나 만들고, 이를 -soldier_num과 row_id 순으로 정렬해 k개의 값에 대해 row_id를 담은 배열을 반환했다
- 남의 풀이: 한 줄로 만들었다

### 0216 Letter Case Permutation
- 문제: 문자열이 주어졌을 때, 각 단어를 모두 lowercase 혹은 uppercase로 바꿔 다른 문자열을 만들어 낸다
- 나의 풀이: isalpaha() 함수와 combinations를 사용해 풀었다. 알파벳인 원소들의 index를 기억해두고, s를 전부 소문자로 바꾼 뒤 알파벳 index들의 0개 ~ alphabet 갯수 개 만큼의 조합을 구해 전부 upper()로 바꾸는 연산을 통해 새로운 문자열을 만들었다.
- 다른 사람의 풀이: 백트래킹을 이용하는 방법으로는 dfs를 통해 해당 문자 인덱스가 알파벳이라면, lower()를 취한 뒤 append해주거나, 아니라면 upper()를 취한 뒤 문자열을 만들 것 같다.
    One-line 풀이로 product 기능을 사용했다.


### 0218 Arithmetic Slices
- 문제: 값의 차가 동일한 연속된 시퀀스의 갯수를 구함
- 나의 풀이: 리스트 내 인접 요소들 사이 차를 담은 배열을 만들고, 동일한 값이 반복되는 길이가 n이라면 해당 n에서는 n*(n-1)//2 개의 시퀀스가 나올 수 있음을 이용함

### 0219 Mimimum Remove to Make Valid Parentheses
- 문제: 괄호를 포함한 문장이 주어졌을 떄, 잘못된 parenthesis 사용을 없애기 위해 몇 번의 remove 작업이 필요한지 묻는 문제이다
- 나의 풀이: 문자열을 돌며 parenthesis들을 저장하는 stack을 만들고, 정상적인 값들은 버렸다. 정상적이지 않아 스택에 남게 되는 (parentesis, idx) 조합에서 idx들을 뽑고, 해당 idx의 문자들을 포함하지 않는 새로운 문자열을 만들어 valid하게 만들었다
- 다른 사람의 풀이: parenthesis 별로 +, -를 더하고 빼면서 연산을 수행했다. 메모리 측면에서 훨씬 효율적인 것 같다

### 0220 Roman to Integer
- 문제: 로만 표기법의 숫자 문자열이 들어왔을 때, 아웃풋으로 정수를 낸다
- 나의 풀이: 뒤부터 보면서, 만약 이전에 나왔던 숫자보다 자신의 값이 더 작다면 숫자 값을 빼주고, 아니라면 더해주었다
- 다른 사람의 풀이: 더 짧게 풀었지만 동일하다

### 0221 Broken Calculator
- 문제: 계산기가 고장이 났는데, 전시된 숫자에 두 배를 곱하거나, 1을 빼는 작업밖에 할 수 없다. calcualtor가 숫자 X를 보여주고 있을 때, Y를 만들기 위한 최소 연산의 수를 구해라
- 나의 풀이: 처음에는 DFS로 파고 들어가는 연산을 했다. 1 -> 1000000으로 가는 과제에서 Maximum recursion error가 났고, 배열로 바꾸어 전체에 연산을 하게 해보았지만 그래도 시간 초과가 났다. 당연한 결과였다... 다시 고민해보니, y에서 거꾸로 가는 편이 훨씬 쉬울 것 같았다. y가 작아질수록, -1 연산을 사용해 차를 줄이는 수가 적어질 것이었기 때문이다. 결국 -1 연산을 해줘야 하는 때는 x가 y보다 커졌을 때 뿐인데.. 이런 식으로 생각하다가 y가 x보다 클 동안 2의 배수면 나누기 2, 아니면 + 1 연산을 하고 마지막에 x와의 차를 연산 횟수와 더해주자 풀 수 있었다. 무작정 구현하려고 하지 말고 어떻게 문제에 접근해야 풀 수 있을지를 고민해 봐야겠다
- 복잡도: Time: O(logY) Space: O(1)
- 다른 사람의 풀이: y -> x 로 푸는 것은 접근이 같으며, 재귀 함수 형식으로 푸셨는데 어차피 이 방식이라면 for문으로 해결하는 것이 훨씬 효율적이었을 것 같다. 사고적인 증명이 좀 더 잘 되어있어서 접근법이 옳다는 걸 증명해 주었다

### 0222 Longest Word Dictionary through Deleting
- 문제: 하나의 string, s와 여러 개 string들의 배열, d가 주어졌을 때 s의 문자 몇 개를 삭제하면 만들 수 있는 d 내의 문자열 중 가장 길이가 길고, 사전적으로 앞인 값을 반환하시오
- 나의 풀이: 일단 가장 길고, 그 중 가장 사전적으로 앞선 순으로 확인하며 subsequence가 맞는 것이 나오면 바로 값을 반환함
- 다른 사람의 풀이: 동일하지만, 우선 모든 것들에 대해 subsequence가 되는지를 구한 뒤 그 중 길이가 최대가 되고 사전적으로 앞인 것을 반환함


### 0223 Search 2D Matrix II
- 문제: 열 별로, 행 별로 정렬이 된 2차원 행렬과 찾고자 하는 숫자 target이 주어졌을 때, target이 행렬 내 있는지 효율적으로 찾기를 묻는 문제이다
- 나의 풀이: 나는 리스트 안의 원소를 찾는 연산이 O(1)이라고 알고 있었기 때문에 각 열을 돌면서 첫번째 값이 target 값보다 크면 더 이상 찾아보지 않는 식으로 구현했다. 날로 먹기..
- 다른 사람의 풀이: 0, max_len - 1 좌표에서 시작해 x와 y 한 칸씩을 움직이며 값을 조정했다. O(m + n)이 걸린다고 했는데, 나의 것이 날로 먹기이기는 해도 더 낫지 않나 싶었다.

### 0224 Score of Parentheses
- 문제: parentheses가 주어졌을 때, (sub parentheses) 의 형태는 sub parentheses의 점수 * 2배의 점수를 얻을 수 있고, (subparenthesis) 개당 1점을 얻는다
- 나의 풀이: 스택을 두고, 몇 개의 왼쪽 것이 쌓였는지, 그리고 몇 개가 한 묶음으로 묶이는 지를 l_count와 r_count로 구했다. 더 간단한 방법이 있을 것 같았는데 떠올리지 못했다 ㅠ 처음에는 같은 차원? 곱하기? 단계에 있는 것끼리는 먼저 더하고 그 뒤 곱하려고 했는데, 그냥 다 따로 2배를 곱하는 식으로 각자 더했다
- 다른 사람의 풀이: 훨씬 간단하게 풀었다. 묶음이 있는지, 없는지를 확인하고 ()가 딱 나오는 부분에서 1이 더해지고 여기에 값들이 곱해지는 것이라는 점에서 착안했다. 나와 아이디어 자체는 많이 다르지 않았는데 훨씬 깔끔한 구현 방식을 택했다

### 0225 Shortest Unsorted Continuous Subarray
- 문제: 배열이 주어졌을 때, 배열을 오름차순으로 정렬되게 만들기 위해 정렬해야 할 연속된 subarray의 최단 길이를 구한다
- 나의 풀이: 일단 각 연속된 값들 사이의 차를 구해 num_diffs 배열에 저장하고, 여기서 음수 값은 정렬되지 않은 부분이므로 해당 index들을 저장해 두었다가 가장 이른 곳 ~ 가장 늦게 나온 음수값의 인덱스 차를 이용해 첫 번째 길이를 구했다. 해당 subarray 내에서 최솟값과 최댓값을 찾고 subarray의 시작 전에 최솟값보다 큰 값이 있거나, 끝 뒤에 최댓값보다 작은 값이 있다면 sorting 해줘야 하는 subarray에 추가해 주었다. 좀 지저분하게 푼 점이 아쉽다
- 다른 사람의 풀이: 


### 0226 Validate Stack Sequences
- 문제: 값들이 스택에 push 된 순서와 pop 된 순서가 주어졌을 때, 해당 순서로 값들이 push 된 스택이 주어진 순서대로 pop 되는 것이 가능한지를 반환하는 문제이다.
- 나의 풀이: 실제로 시뮬레이션 해보면서 풀기로 했다. 스택에 차례로 쌓고, 만약 popped에서 요구하는 값이 스택의 마지막 값과 다르거나 스택이 비어 있다면 Pushed에서 popped의 요구사항과 같아질 때까지 다시 넣는데, 만약 pushed의 길이를 넘어서서도 요구하면 이는 이 전에 나온 값을 요구하는 것과 같으므로 False를 반환함
- 다른 사람의 풀이: 거의 동일하게 풀었다

### 0227 Divide Two Integers
- 문제: 두 정수 dividend와 divisor가 주어졌을 때, dividend를 divisor로 나눈 값을, 소숫점 자리를 제거하고 반환하는 문제
- 나의 풀이: dividend와 divisor가 나누어 떨어질 때에는 "//" 값을 그래도 반환했다. 나누어떨어지지 않을 경우 "//" 연산을 이용해 몫만 남기고 음수이면 +1 해주었다.
- 다른 사람의 풀이: **Bitwise operation**을 이용해 풀었다. 문제의 의도였던 듯 하다!!


### 0228 Maximum Frequency Stack
- 문제: Maximum Frequency Stack을 구현해, 가장 빈번한 값을 반환하거나 빈도가 같은 값들 중 가장 마지막에 들어온 값을 반환하다
- 나의 풀이: max를 사용해 풀어 보았으나 시간 초과가 났다
- 다른 사람의 풀이: freq를 기준으로 딕셔너리를 만들었다
