# LeetCode 1월 문제 풀이 목록
- 0120 valid_parenthesis.py


### 0120 Valid Parenthesis
- 아이디어
    스택에 쌓아 두고, 가장 오른쪽에 있는, 즉 가장 마지막에 있는 element와 매칭이 된다면 매칭된 스택의 마지막 원소를 지운다. 이렇게 하면 valid parenthesis만 있는 string의 경우 스택이 비게 된다.
    ex) stack의 마지막에 '{' 가 있었는데 '}'가 다음으로 들어왔다면 매칭되므로, 스택에서 '{'를 지운다

- 구현
    closing parenthesis마다 매칭되는 opening parenthesis를 스택으로 저장했다.
- 다른 사람의 풀이
    오히려 opening에 매칭이 되게 하자 코드가 훨씬 짧아졌다
    같은 insight인데도 조금의 다른 구현 방식 때문에도 코드의 가독성이 차이가 날 수 있다

