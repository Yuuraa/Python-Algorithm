# LeetCode 1월 문제 풀이 목록
- 0120 valid_parenthesis.py
- 0121 most_competitive_subseq.py
- 0122 valid_parenthesis.py
- 0123 sort_matrix_diag.py
- 0124 merge_sorted_lists.py
- 0125 check_k_places_away.py
- 0126 min_effort_path.py
- 0127 concat_binaries.py
- 0128 smallest_numeric_string.py


### 0120 Valid Parenthesis
- 아이디어
    스택에 쌓아 두고, 가장 오른쪽에 있는, 즉 가장 마지막에 있는 element와 매칭이 된다면 매칭된 스택의 마지막 원소를 지운다. 이렇게 하면 valid parenthesis만 있는 string의 경우 스택이 비게 된다.
    ex) stack의 마지막에 '{' 가 있었는데 '}'가 다음으로 들어왔다면 매칭되므로, 스택에서 '{'를 지운다

- 구현
    closing parenthesis마다 매칭되는 opening parenthesis를 스택으로 저장했다.
- 다른 사람의 풀이
    오히려 opening에 매칭이 되게 하자 코드가 훨씬 짧아졌다
    같은 insight인데도 조금의 다른 구현 방식 때문에도 코드의 가독성이 차이가 날 수 있다

### 0121 Find the Most Competitive Subsequence
- 아이디어
    내가 생각했던 아이디어는, 일단 주어진 리스트에서, 이전 단계에서 선택된 숫자 뒤면서, 그 뒤에 k - 1 개 이상의 원소가 있는 위치 중 가장 최솟값인 것들이 정답 시퀀스에 차례로 들어가면 된다고 생각했다. 생각이 틀린 것은 아니었지만 접근법이 달랐다. 나의 경우에는 각 경우마다 left와 right(limit)를 업데이트 해가며 min과 min값의 index를 찾는 연산이 필요했으므로 시간이 오래 걸렸다. 거의 O(mnlog(n)) 정도가 걸렸을 것으로 보인다 (m은 k, n은 리스트의 길이).
    다른 사람은 거의 O(n)의 시간으로 했는데, 직접 스택을 쌓아가면서 보다 큰 원소는 스택에서 제외하되, 그 제외하는 횟수를 제한하는 방식이었다.
- 구현
    left, right를 업데이트 하고 min, index로 찾는 식의 구현 -> 시간 초과
    =>
    다른 사람의 구현 참고 -> stack에 쌓으면서 pop횟수에 제한을 두고, 자신보다 더 큰 것이 앞에 있다면 pop해줌 차례로

### 0122 Determine if Two Strings Are Close
- 아이디어:
    각 문자들 끼리 위치 바꾸기 및 서로 바꾸기가 가능하다고 했으므로 문자열을 구성하는 문자들의 종류가 같고, 문자들의 갯수들이 같다면 즉, a 1개 b 2개 = b 1개 a 2개 (1개, 2개로 이뤄짐) 두 개의 string이 close라고 판별했다.
- 다른 사람의 구현에서는 one liner로 했다
- 흥미로웠던 점:
    Counter()로 각 리스트를 센 뒤 Counter.values()를 바로 비교하면 내용물이 똑같아도 같지 않다고 나왔다. 나는 따로 list를 만들어 주어 해결했다. 다른 사람의 경우 values()에 대한 카운터를 만들고 그 카운터가 같은지를 비교해서 한 줄로 끝냈다.

### 0123 Sort the Matrix Diagonally
- 아이디어:
    대각선이 시작되는 곳은 matrix[i][0] 이거나 matrix[0][j] 이기 때문에, 해당 부분을 돌며 (m + n 회) 대각선의 값을 만들었다.
    대각선은 x, y를 min(m - i, n) 혹은 min(m, n - j) 만큼을 돌며 리스트로 저장했다. 이후 리스트를 소트한 후 값을 matrix에 대입해 주면서 각 대각선을 정렬했다.
- 더 좋은 아이디어는?
    각 대각선은 모두 unique한 j - i 값을 갖는다. 대각선 내에선 해당 값이 동일하므로 dict 타입으로 값을 저장 후 정렬한 뒤 matrix에 대입해주면 된다.

### 0124 Merge k Sorted Lists
- 문제: k개의 정렬된 linked list를 한 개의 정렬된 linked list로 합친 후 반환한다
- 아이디어:
    모든 linked list를 돌면서 val을 갖고 와 하나의 리스트에 담고, 정렬한 뒤 새로운 링크드 리스트를 이 값들을 이용해 만들었다.
    상당히 비효율적일 수도 있기는 하다. 공간을 많이 차지하고, 미리 정렬된 링크드 리스트가 들어온다는 문제 조건의 장점을 이용하지 못했다..
- 다른 사람의 구현: 

    이 사람도 공간을 많이 차지한 것은 동일하지만, 값을 넣을 때 정렬되어 들어갈 수 있도록 heapq를 이용했다!!

### 0125 Check If All 1's Are at Least Length K Places Away
- 문제: 0과 1로 이루어진 배열과 k 가 들어왔을 때, 1 사이가 최소 k개 이상 씩 떨어져 있는지를 확인하는 문제이다.
- 아이디어: nums의 길이가 10^5까지였기 때문에, O(nlogn) 이하로 푸는 것이 좋겠다고 생각했다. 선형으로 한 개씩 보면서 distance를 업데이트 하고, 1이 나왔을 때 distance가 k보다 작거나 같다면 False를 리턴하면서 끝내게 했다

### 0126 Path With Minimum Effort
- 문제: 처음 -> (0,0) -> (m-1, n-1) 끝까지 가는 길에서 한 칸 한 칸 사이의 값의 차의 최댓값이 최소가 되는 path의 값을 찾는다
- 아이디어: DFS로 구현하여서, 재귀함수 형태로 호출했다. global variable로 해당 최솟값을 업데이트 해주었는데, 이렇게 하니 리트코드에서는 테스트가 제대로 되지 않는다는 문제가 있었다. 리스트 형태로 저장하자 시간 초과 에러가 났다.
- 다른 사람의 아이디어: DFS로 구현하는데, threshold를 두어서 해당 threshold를 binary search로 만족하면 더 작은 값, 만족하지 않으면 더 큰 값을 찾아보게 했다

### 0127 Concatenation of Consecutive Binary Numbers
- 문제: binary로 만든 후 n 개까지 해당 표현을 붙여서, 최종 결과값이 얼마인지를 구함
- 아이디어: binary 연산을 사용해야 겠다고 생각했다. 나는 뒤에서부터 붙이면서, binstring의 길이를 보고 이를 각각의 숫자에 곱해준 후 (<< 연산을 사용하는 것까지 잘 생각했음!) result에 더하는 연산을 생각했는데, 시간 초과가 났다..
- 다른 사람의 아이디어: 좀 더 점화식처럼 생각해서, 매 번 늘어나는 길이를 바로 구할 수 있음을 이용했다. 
- 소감: 뭔가 오토마타 이론이 생각나는 문제였다... 점화식 생각에 좀 약한 것 같으니 보완이 필요하다.

### 0128 Smallest String With A Given Numeric Value
- 문제: a~z 각 1~26의 numeric 값을 가짐

### 0129 Vertical Order Traversal of a Binary Tree
- 문제: 이진 트리가 주어졌을 때, 탐색을 거치면서 같은 x 값을 가진 것끼리 묶되, 그 안에서는 1) y값 (깊이) 가 이른 것 먼저, 2) 같은 x, y라면 노드의 값이 작은 것 먼저 순서로 가진 리스트를 반환하면 된다
- 아이디어: 쭉 순회하면서, 같은 x 값 별로 dict를 만들고 그 안에 (val, y) 로 이루어진 튜플을 넣었다. 이후 리스트로 뽑으면서 y와 val로 정렬하고, 이를 answer에 넣었다