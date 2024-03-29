# 7월 리트코드 챌린지
### 문제 목록
1. Gray Code 
2. Find K Closest Elements
3. Max Sum of Rectangle No Larger Than K
4. Count Vowels Permutation
5. Reshape the Matrix
6. Reduce Array Size to The Half
7. Kth Smallest Element in a Sorted Matrix
8. Maximum Length of Repeated Subarray
9. Longest Increasing Subsequence
10. Decode Ways II
11. Find Median from Data Stream
12. Isomorphic Strings
13. Find Peak Element
14. Custom Sort String
15. Valid Triangle Number
16. 
17. 
18. Reverse Nodes in k-Group
19. Lowest Common Ancestor of a Binary Search Tree
20. Shuffle an Array
21. Push Dominoes
22. Partition Array into Disjoint Intervals
23. Binary Tree Pruning


### 0701 Gray Code
- 문제: n이 주어졌을 때, n개 bit으로 만들 수 있는 graycode를 찾는 문제
- 풀이: n을 구하기 전, n-1번째 gray code를 구하는 방식. 초기값은 0으로, bottom-up 방식으로 구현했다
    - n-1번째의 gray code의 마지막에 1을 붙인 것을 추가하다가, 끝에서 n-1번째 gray code를 역방향으로 돌며 마지막은 2로 끝이 난다
    - 가능한 이유: 모든 gray code가 0에서 시작하기 때문에, 이전 단계 첫 번째인 n-1개 0으로 이루어진 코드의 마지막에 1을 추가하면 0과 한 비트만 차이가 난다
    - 이전 단계 코드에 1을 끝에 붙이는 방식을 이어가면, 이전 단계에서 이미 1 bit씩 차이가 나도록 구해 두었기 때문에 정상적으로 동작한다
    - 이전 단계 코드를 모드 순회한 뒤 역순으로 0을 붙이기 시작하면, 끝에 1을 붙인 방식과 맨 끝 bit 차이만 나고, 이후에도 이전 단계에서 구한 대로 1 bit씩 차이가 난다
    - 모든 gray code의 마지막 숫자는 0과 1 bit 만 차이가 나도록 만들어졌기 때문에, 그 끝에 0을 붙여도 0과 1 bit만 차이가 난다
    - 이진수 표기 된 code의 마지막에 0을 붙이는 것은 숫자에 두배를 곱하는 것이고, 1을 붙이는 것은 두 배를 곱한 것에 1을 더한 것으로 이전 코드의 정수값으로부터 현재 코드의 정수값 배열을 계산할 수 있다

### 0702 Find K Closest Elements
- 문제: 정렬된 배열 arr와 숫자 x, 반환할 숫자의 갯수 k가 주어졌을 때, x와 가장 가까운 k개의 숫자들을 크기 순으로 정렬해 반환하는 문제. x 값과의 절대값 차가 작을수록, 숫자의 크기가 작을수록 가깝다
- 풀이:
    - 실제로 구하는 방법: 전체 배열을 순회하며 절댓값 차를 구하고, 가까운 순서대로 정렬한 뒤, k개의 element들을 정렬해 반환한다
        - 시간 복잡도가 O(nlogn)이 된다. 정렬을 다시 해야 하기 때문이다! 하지만 정렬된 배열을 입력으로 받으므로 이는 비효율적이다
    - 두 개의 포인터를 이용하는 방법: 배열의 첫 부분과 끝 부분에 포인터를 두고, x와의 값 차를 비교하며 만약 앞부분 포인터의 절댓값 차가 더 크다면 앞 포인터를 한 칸 뒤로 옮기고, 아니라면 뒤 포인터를 한 칸 앞으로 옮기며 k개의 원소 만이 사이에 남을 때까지 반복한다
        - 정렬된 배열에서 절댓값 차는 한 지점을 기준으로 왼쪽으로 갈 수록 연속적으로 감소, 오른쪽으로 갈 수록 증가한다. 따라서 두 개의 포인터를 두어 차가 더 큰 것을 제거해 나가면 k개의 closest element를 구할 수 있다
        - 시간 복잡도는 k가 1일 경우 최대 n-1 개의 비교를 하기 때문에 O(n)이 된다

### 0703 Max Sum of Rectangle No Larger Than K
- 문제: m x n 행렬과 정수 k가 주어졌을 때, 직사각형 submatrix의 원소의 합 중 k 이하의 최댓값을 구한다

### 0704 Count Vowels Permutation
- 문제: 숫자 n 이 주어졌을 때, a, e, i, o, u로 만들 수 있는 n 길이의 문자열의 수를 구하는 문제. 단, a -> e, e -> a, i, i -> a, e, o, u, o -> i, u, u -> a 로 각 문자 뒤에 올 수 있는 문자들이 정해져 있다. 숫자가 너무 클 수 있으므로 10^9 + 7에 대한 나머지를 반환한다
- 풀이:
    - 문자열 길이를 1에서 시작해, 길이를 1씩 증가시킨다. 기존에 있는 문자들의 뒤에 올 수 있는 문자들을 붙이면 된다. 가짓수가 너무 많아질 수 있으므로 매 회 modulo 연산을 해준다
    - 시간 복잡도: O(n). 생성할 문자열의 길이 동안 5개의 문자 종류에 대해 갯수를 새롭게 구하는 연산이다

### 0705 Reshape the Matrix
- 문제: m*n 행렬을 주어진 r, c 크기로 바꾸되, 원본 데이터와 그 row-traversing 순서를 유지하는 reshape 함수를 구현한다. Reshape 형태가 legal 하다면, 즉 원본 행렬과 동일한 갯수의 원소를 갖는 행렬이어야만 하고, 아닌 경우 원본 행렬을 변화시키지 않는다
- 풀이:
    - r * c가 기존 m * n과 같은 값을 갖는지 확인한 뒤, 기존 행렬 내 모든 원소르르 row-traversing 순으로 순회하며 새로운 r, c에 맞추어 배열을 만든다
    - 시간 복잡도: O(m*n)

### 0706 Reduce Array Size to The Half
- 문제: 리스트 arr가 주어졌을 때, arr의 크기를 절반 이하로 줄이기 위해 제거해야하는 element set의 최소 갯수를 구한다
- 풀이:
    - Counter로 arr 내에서 element들의 등장 횟수를 잰다. 가장 많이 등장하는 element부터 순차적으로 등장 횟수를 추가하고, 그 합이 arr의 크기 절반 이하가 되면 지금까지 지운 element의 종류수를 반환한다

### 0707 Kth Smallest Element in a Sorted Matrix
- 문제: n x n 행렬 matrix가 주어졌을 때, 그 안에서 k 번째로 작은 원소를 반환한다.
- 풀이:
    - row-wise, column-wise로 정렬된 것이 주어지므로 이분탐색에 활용할 수는 없을지 고민했지만, 왼쪽 아래와 우측 상단의 것에서 더 작은 원소가 등장할 수도 있어서 관두었다...
    - 그냥 전체 matrix를 정렬한 후 k 번째 element를 반환하도록 했다

### 0708 Maximum Length of Repeated Subarray
- 문제: 두 개의 정수로 이루어진 배열이 주어졌을 때, 두 배열에 모두 등장하는 subarray의 최고 길이를 구하는 문제이다
- 풀이: subarray 문제는 Longest Common Substring 문제와 동일하게 풀면 될 것이라고 생각했다
    - DP로 지금까지 나온 common substring의 길이를 저장한다. 두 개의 배열에 대해 각자 index를 두고 순회하며, 배열에서 i, j에서의 값이 같을 때에는 i-1, j-1까지의 substring 길이에 +1을 해주고, 아니라면 0을 설정해준다. 이 과정에서 최대 길이는 계속 업데이트 해준다
    - 시간 복잡도: 두 개의 배열에 대해 끝까지 순회하기 때문에, 각 길이를 m, n이라고 하면 O(m*n) 시간 복잡도가 걸린다

### 0709 Longest Increasing Subsequence
- 문제: nums라는 배열이 가장 긴 증가하는 부분수열의 길이를 찾는 문제
- 풀이: 
    - LIS 문제는 대표적인 다이나믹 프로그래밍 문제이다. DP 배열의 i 번째에는 nums[i]를 포함하는 그 때까지의 longest increasing subsequence의 길이가 담겨 있다. 이는 i 이전까지의 DP, nums를 확인하면서 i 번째 원소보다 작은 원소의 DP 값에 1을 더한 것의 최댓값을 구하며 DP를 업데이트 한다. 마지막에 남은 DP 값들 중 최댓값을 반환하면 LIS를 구할 수 있다
    - 시간 복잡도: O(n^2)

### 0710 Decode Ways II
- 문제: 영어 -> 숫자로 인코딩 된 문자열이 주어졌을 때, 가능한 디코딩의 경우의 수를 반환하는 문제. A -> 1, .., Z -> 26으로 인코딩되며, *은 1 ~ 9 사이 모든 수를 나타낼 수 있다
- 풀이:
    - 0이 등장하면, 0 바로 앞의 숫자까지 묶어 10 또는 20 또는 *0중의 하나일 것으로 취급하면 된다. 0 앞에 문자가 없거나, 1,2, * 중 하나가 아닐 경우에는 적절하게 인코딩 된 것이 아니므로 0을 반환한다
    - 즉, 0을 기준으로 분리하며 만약 *0의 형태인 경우, 10과 20 두 가지가 가능하므로 2를 결과에 곱해준다. 이를 mult_factor로 저장한다
    - 0의 등장을 기준으로 분리한 substring들에 대해, 뒤부터 디코딩을 시작한다. DP로 디코딩 경우의 수 값을 저장해둔다. 만약 문자열의 i 번째가 1, 2 또는 * 이라면 i+1번째 것과 함께 11 등의 숫자로 디코딩 될 수도 있고, 1 1 등으로 따로 디코딩 될 수도 있다. 이 경우를 고려해 함께 디코딩이 가능한 경우 - i와 i+1을 함께 고려해 경우의 수를 세고 DP[i+1]과 DP[i+2] 번째의 디코딩 경우의 수를 사용해 DP[i] 번째의 경우의 수를 구한다

### 0711 Find Median from Data Stream
- 문제: 내부적으로 정렬된 정수 배열을 갖고 있으면서, 그 배열의 중앙값을 반환하거나 배열에 값을 추가할 수 있도록 하는 MedianFinder 객체를 만든다.
- 풀이:
    - 정렬된 정수 배열을 갖고 있기 위해 bisect라이브러리를 사용했다. 정수 배열의 길이 또한 갖고 있다가 Median 값을 찾을 때 사용했다
    - 원소 추가 시 시간 복잡도: O(n^2). bisect의 insort 알고리즘은 O(n)의 시간이 걸린다. 적절한 위치를 찾기까지 O(logn), 삽입시 O(n)이 걸리고, 이 과정을 n차례 반복하기 때문에 O(n^2)의 시간 복잡도가 된다
    - 중앙값을 구할 때 시간 복잡도: O(1)
- 다른 사람의 풀이:
    - 두 개의 heap을 사용했다. 작은 쪽과 큰 쪽으로 나누었고, 작은 쪽은 음의 부호를 붙여 가장 작은 값을 가장 큰 값으로 만들고, 큰 쪽은 원래 순서를 사용했다. add_num 함수를 사용해 숫자를 추가할 때마다 작은 쪽과 큰 쪽의 길이를 맞춰 주었다. 각 heap의 맨 첫 번째 원소 = root를 활용하여 small 측에서 가장 작은 값 = 중앙값 이상의 값 중 최솟값과 large측에서 가장 큰 값 = 중앙값 이하의 값 중 최댓값을 사용해 실제 중앙값을 구한다
    - 원소 추가시 시간 복잡도: O(nlogn). 한 원소를 추가할 때 O(logn)의 시간이 걸리며 이를 n 차례 이상 하므로 O(nlogn)이 된다.
    - 중앙값을 구할 때 시간 복잡도: O(1)
- 추가 문제: 만약 모든 숫자들이 0 ~ 100사이에 있다면, 어떻게 문제를 효율적으로 풀 수 있을까?
- 추가 문제2: 만약 숫자들의 99%가 0 ~ 100사이에 있다면, 어떻게 문제를 효율적으로 풀 수 있을까?

### 0712 Isomorphic Strings
- 문제: s 내의 문자들을 대체해서 t 를 만들 수 있을 때, s와 t가 isomorphic string이라고 합니다. s와 t가 주어졌을 때, isomorphic string인지 구하는 문제입니다
- 풀이:
    - s -> t, t -> s 변환 매핑을 구해두고, 매핑에 맞지 않는 문자가 나오면 False를 반환합니다


### 0713 Find Peak Element
- 문제: 정수의 배열 nums가 주어졌을 때, peak element의 인덱스를 반환한다. Peak element란 이웃들 보다 값이 큰 원소를 말한다. 알고리즘은 시간 복잡도가 O(log n)을 넘지 않도록 해야 한다
- 풀이:
    - 이진 탐색으로 문제를 풀 수 있다


### 0714 Custom Sort String
- 문제: order와 문자열이 주어졌을 때, order 주어진 순서에 맞도록 주어진 문자열을 변형한다
- 풀이:
    - 주어진 순서에 맞게 바꿔야 하는 문자열들을 따로 빼어 정렬하고, 문자열을 순회하며 순서에 따라 바꿔야 하는 문자열들을 정렬한다
    - 시간 복잡도: O(n). n 은 주어진 문자열의 길이


### 0715 Valid Triangle Number
- 문제: 숫자들의 배열 nums가 주어졌을 때, 삼각형의 변을 이룰 수 있는 nums 내 숫자 3개 조합의 수를 구한다
- 풀이:
    - nums를 정렬한다
    - 정렬된 nums 배열 중에서, 각 인덱스 위치마다 그 이전까지 두 개의 포인터를 두고, 합을 했을 때 현재 인덱스 위치의 값보다 크다면 삼각형을 만들 수 있으므로 갯수를 추가한다


### 0718 Reverse Nodes in k-Group
- 문제: 링크드리스트와 숫자 k 가 주어졌을 때, k 길이 만큼의 부분 리스트들을 처음부터 순차적으로 뒤집는다. 만약 링크드리스트의 길이가 k 의 배수가 아니라면, 나머지는 뒤집지 않고 그대로 반환한다. 추가 공간은 O(1) 만큼 사용한다
- 풀이:
    - prev 포인터, s 포인터, k 개 뒤인 e 포인터를 두고 그 만큼을 뒤집은 뒤, prev 포인터가 가리킨 노드의 다음 노드를  e 포인터로 변경한다. 이 과정을 k개짜리 노드 부분 연결 리스트들에 대해 모두 수행한다
    - 시간 복잡도: O(n)

### 0719 Lowest Common Ancestor of a Binary Search Tree
- 문제: 이진 탐색 트리와 두 노드 p, q 가 주어졌을 때, 트리 내 p, q의 lowest common ancestor를 찾는 문제다
- 풀이: 
    - 이진 탐색 트리이기 때문에, 공유되는 root가 있다면 그 root에서 갈라진 부분 트리에 있거나, p와 q 중 한 노드가 그 공통 ancestor인 경우가 된다. 따라서, 일단 더 작은 값을 가진 node를 p로 설정한 뒤 root와 p, q의 값을 비교했다. root의 값으로 p와 q의 값이 갈라지면, 해당 root가 공통 ancestor이다. 아니라면 p와 q 모두 root보다 값이 작거나 크므로 그에 따라 root 왼쪽 또는 오른쪽 자식 노드를 새로운 root로 삼으며 반복한다.
    - 시간 복잡도: O(logn). 최악의 경우 트리의 leaf node 직전까지 순회하게 되며, 이진 분류 트리이기 때문에 트리의 최고 깊이는 logn이다

### 0720 Shuffle an Array
- 문제: 배열 nums가 주어졌을 때, 배열을 shuffle 하거나 원래 상태로 되돌려놓는 함수를 작성하는 문제
- 풀이:
    - random.shuffle을 이용해 배열을 섞어냈다

### 0721 Push Dominoes
- 문제: 도미노에 왼쪽으로 힘을 가할지, 오른쪽으로 힘을 가할지 혹은 힘을 가하지 않을지 여부가 담긴 dominoes 배열이 들어오면, 각 도미노가 어느 방향으로 쓰러질지를 반환한다
- 풀이:
    - 도미노에 가해진 힘의 쌍은 크게 4가지가 존재하는데, L 뒤에 L, L 뒤에 R, R뒤에 L, L 뒤에 R이 있다. 오른쪽으로 힘을 가한 도미노 뒤에 왼쪽으로 힘을 가한 도미노가 오는 경우만 주의하여 처리하면 된다. 마지막으로 L 힘을 가한 도미노 위치와 R 힘을 가한 도미노 위치를 기억해 두었다가, L 또는 R 이 나왔을 때 가장 최근에 가한 힘의 종류에 따라 도미노가 다르게 쓰러짐을 이용하면 된다
    - 시간 복잡도: O(n)

### 0722 Partition Array into Disjoint Intervals
- 문제: 배열 nums가 주어졌을 때, left와 right 부분 배열로 나누어 left에 있는 모든 요소들이 right에 있는 모든 요소들보다 작거나 같도록 나누는 문제이다. left의 갯수를 최소한으로 만들 때의 갯수를 구한다
- 풀이:
    - left에 있는 모든 원소들은 right에 있는 모든 요소들보다 값이 작거나 같아야 한다. 따라서, 왼쪽부터 값을 순차적으로 확인하며 지금까지의 left의 범위, 지금까지 left 범위 내 포함된 원소의 최댓값, 현재 확인중인 값 까지의 최댓값을 모두 가지고 있는다.
    - 현재 확인한 원소가 지금까지 정해진 left의 범위 내 최댓값보다 작은 값이면, 이 값은 right에 들어갈 수 없으므로, 현재 확인한 원소까지 left에 포함되어야 한다.
        - 이 상황에서는left 범위를 수정하고, 현재까지 확인중인 값까지의 최댓값을 left 범위 내 최댓값으로 설정하는 작업을 한다
    - 그렇지 않다면, 확인중인 인덱스 값만 변경하고, 현재까지 확인중인 값 까지의 최댓값을 업데이트한다 (바뀌지 않을 수도 있다)

### 0723 Binary Tree Pruning
- 문제: 0, 1로 이루어진 트리가 있을 때, 1을 포함하지 않는 subtree를 제거하는 문제이다
- 나의 풀이: 
    - DFS로 트리를 깊이 있게 들어가며, 참 또는 거짓을 반환하고 왼쪽과 오른쪽 subtree를 관리하는 check_prune 함수를 구현했다. 
    - 참을 반환하면 1을 포함하는 subtree의 루트인 것이고, 거짓이면 1을 포함하지 않는 것이다. 
    - 1. 해당 함수에서는, 현재 node의 포인터가 주어졌을 때 자식 노드들을 check_prune으로 확인하며, 거짓을 반환하면 해당 자식 노드에 대한 포인터를 None으로 바꿔 가지치기 한다.
    - 2. 그 후, 자신의 값이 1이면 참을 반환하고, 0이면 자식 노드중에 1을 포함하는 것이 있다면 참, 아니라면 거짓을 반환한다
    - 이를 통해 자식 노드에 대해 이를 호출하면, 거짓을 반환하면 해당 subtree에는 1이 존재하지 않음을 알 수 있다
    - 이 과정을 반복하고, 마지막 root Node까지 확인하는 방법으로 check_prune(root)를 호출하고 해당 반환값을 확인해 거짓이 나오면 결과적으로 트리 자체를 삭제한다


### 0724 Word Ladder II
- 문제: beginWord에서 endWord까지, 한 문자씩 만을 바꾸면서 sequence를 만들 수 있다. 주어진 wordList안의 단어들을 사용해서 sequence를 만들고, 그 때 단어들을 최소한으로 사용하는 sequence들을 모두 반환한다
- 나의 풀이:
    - 

### 0726 Convert Sorted Array to Binary Search Tree
- 문제: 정렬된 배열을 height-balanced BST로 변환하는 문제이다. height-balanced란, 모든 노드에서의 subtree의 깊이가 1 이상 차이나지 않는 것을 말한다
- 나의 풀이:
    - 배열의 가운데 값을 root로 한 subtree를 만들며 이어 붙이면 된다


### 0727 3Sum Closest
- 문제: 숫자들의 배열 nums와 목표 target이 주어졌을 때, nums 내에서 3 개의 숫자를 더해 만들 수 있는 target과 가장 가까운 숫자를 골느다
- 나의 풀이:
    - i를 점차 len(nums) - 2까지 증가시키며, i 뒤의 배열에서 two-pointer를 이용해 가장 합이 target과 가까운 것을 구해 나갔다. 순회를 마치고 최종적으로 가장 가까운 값을 반환한다~