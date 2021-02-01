# Binary Search Algorithm
**탐색 범위가 2000만 넘는다면 이진 탐색으로 접근해 볼 것!**

**입력 데이터 많은 경우 input()보다는 sys 라이브러리의 readline()을 활용할 것**
```python
    import sys
    input_data = sys.stdlin.readline().rstrip()
```

### Concepts
탐색: 리스트 안의 특정 데이터를 찾는 과정
순차 탐색: 앞에서부터 데이터를 하나씩 차례대로 확인하며 탐색. 최악의 경우O(N) 시간복잡도

**이진 탐색**
- 정렬된 데이터에서 사용 가능
- 시작점, 끝점, 중간 점을 이용하여, 찾으려는 데이터와 중간점의 데이터를 반복적으로 비교해 원하는 데이터를 찾음
- 시간 복잡도: O(logN)

**트리 자료구조**
데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있다.
큰 데이터를 처리하는 소프트웨어는 대부분 트리 자료구조로 데이터를 저장, 이진 탐색 기법을 이용해 빠른 탐색 가능

**이진 탐색 트리 (구현 추가)**
왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드




### 예시 문제들
0. 이진 탐색, 이진 탐색 트리 구현 0_binary_search.py, 0_binary_search_tree.py
1. 부품 찾기 1_find_component.py
2. 떡볶이 떡 만들기 2_make_tteokbokki.py


### 0_binary_search.py
- 아쉬운 점: mid + 1, right와 left, mid - 1 로 업데이트 해야 한다는 점을 바로 파악하지 못해서 maximum recursion error가 발생하게 했다.

### 1_find_component.py
이진 탐색을 활용해도 되지만, set과 membership을 활용하면 훨씬 간단히 풀 수 있는 문제이다.

## 2_make_tteokbokki.py
Parametric search 유형. 최적화 문제를 결정 문제로 바꾸어 해결한다

원하는 조건을 만족하는 가장 알맞은 값을 찾는다

- 아이디어: 절단기의 길이는 최소 0, 최대가 떡의 최대 길이이다. 해당 범위 내에서 적당한 절단기의 길이를 이진 탐색으로 찾는다.