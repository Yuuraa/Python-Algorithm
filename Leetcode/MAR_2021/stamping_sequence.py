def modes_to_stamp(stamp, target):
    moves = []
    last_splits = target.split(stamp)
    move_lasts = []
    idx = 0
    for last_split in last_splits:
        idx += len(last_split)
        move_lasts.append(idx)
        idx += len(stamp)
    move_lasts.pop() # 스탬프의 모양이 온전한, 마지막에 찍은 것들 모음

# 아이디어:
# 만약 잘린 것들이라고 해도, 여러 개가 겹쳐 있다면 맨 앞이나 맨 끝의 글자를 결국 포함할 수밖에 없음
# 따라서 i, j 두 개의 인덱스를 보고 잘린 부분과 stamp를 동시 비교하며 살피면 어디가 먼저 찍힌 것인지도 알 수 있을 것
# 그렇게 처리 하는 함수를 만들면 됨
# 이후 moves 에다가 append 하고 move_lasts를 마지막에 붙이면 될 것 같다


