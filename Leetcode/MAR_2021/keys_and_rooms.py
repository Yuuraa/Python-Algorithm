def can_visit_all_rooms(rooms):
    n = len(rooms)
    visited = [False for _ in range(n)]

    key_gained = [0]
    visited[0] = True

    while key_gained:
        curr_room = key_gained.pop()
        for new_key in rooms[curr_room]:
            if not visited[new_key]:
                key_gained.append(new_key)
                visited[new_key] = True

    return False not in visited

if __name__ == "__main__":
    assert(print(can_visit_all_rooms([[1,3],[3,0,1],[2],[0]])) == False)
    assert(print(can_visit_all_rooms([[1],[2],[3],[]])) == True)