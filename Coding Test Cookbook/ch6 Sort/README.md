# Sort Algorithm
### Concepts
데이터를 특정한 기준에 따라 순서대로 나열 -> 이진 탐색 가능해진다.

정렬 라이브러리로 풀 수 있는 문제, 알고리즘의 원리에 대해 물어보는 문제, 더 빠른 정렬이 필요한 문제 3 가지 유형으로 나뉜다.

**파이썬 정렬 라이브러리** 
- 시간 복잡도: 최악의 경우에도 O(NlogN) 보장
- ```sorted(list)```: 정렬된 list 반환함. list 자체에는 변화가 일어나지 않음. 
- ```list.sort()``` : list를 정렬함. 반환값 없음
- ```key``` 매개변수: 하나의 함수가 들어가야 하고, 정렬 기준으로 사용함. 람다 함수를 사용할 수도 있음

**선택 정렬**

매번 가장 작은 원소를 선택한다.
가장 작은 데이터 선택, 맨 앞의 데이터와 바꾸고 그 다음 작은 데이터 선택, 두 번째와 바꾼다.
- 시간 복잡도: O(N^2)

**삽입 정렬**

데이터를 확인하며, 각 데이터를 적절한 위치에 삽입한다. 특정 데이터가 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
- 시간 복잡도: O(N^2), 최선의 경우 O(N) 동작(리스트가 거의 정렬돼 있는 경우 빠름)
- 궁금한 점: 삽입 정렬 시 이진 탐색을 쓸 수 있을까?

**퀵 정렬**

피벗 사용, 큰 숫자와 작은 숫자 교환시 기준을 정함. 왼쪽부터 피벗보다 큰 데이터를 찾고, 오른쪽부터 피벗보다 작은 데이터를 찾은 후 큰 데이터와 작은 데이터의 위치 교환해줌. -> 피벗에 대해 정렬 수행됨
- 궁금한 점: 피벗을 고르는 기준. 여기에선 맨 첫번째 요소를 사용함
- 시간 복잡도: 평균 O(NlogN), 최악의 경우 O(N^2)(리스트가 거의 정렬돼 있는 경우 느림)

**계수 정렬**

데이터 크기 범위가 제한돼 정수 형태로 표현할 수 있을 때만 사용 가능. 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하므로 가장 큰 데이터와 너무 작은 데이터의 차이가 크면 안됨. 앞선 비교 기반, 위치를 바꾸는 정렬(in-sort)이 아니라 새로운 리스트 선언하고, 요소의 갯수를 세서 정렬
- 시간 복잡도: O(N + K). 데이터의 범위만 한정되어 있다면 효과적으로 사용 가능
- Radix Sort(기수 정렬)와 유사한 방식으로, 기수 정렬이 처리할 수 있는 정수의 크기가 더 크다.


**병합 정렬 (추가)**




### 예시 문제들
0. 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬 0_selection_sort.py, 0_insertion_sort.py, 0_quick_sort.py, 0_count_sort.py
1. 위에서 아래로 1_up_down.py
2. 성적이 낮은 순서로 학생 출력하기 2_student_by_score.py
3. 두 배열의 원소 교체 3_replace_element.py


### 0_selection_sort.py
- 배운점: swap 하는 방식!!


### 1_up_down.py
- 배운점: print(end=" ") 인자를 줄 수 있는 점

### 2_student_by_score.py
- lambda student: int(student[1])

### 3_replace_element.py
- 아이디어: 리스트 A는 오름차순, B는 내림차순으로 정렬
    정렬된 A, B의 왼쪽부터 최대 K개 까지 요소들을 비교하며 A의 값이 B의 값보다 작을 경우 A의 값을 B의 값으로 교체