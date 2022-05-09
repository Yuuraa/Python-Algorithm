import sys


n_pokemon, n_q = map(int, sys.stdin.readline().split())
pokemon_list = {}

for i in range(n_pokemon):
    pokemon_list[str(i+1)] = sys.stdin.readline().rstrip("\n")
reverse_list = {v: k for k, v in pokemon_list.items()}

for _ in range(n_q):
    q = sys.stdin.readline()
    q = q.rstrip("\n")
    if q in pokemon_list:
        print(pokemon_list[q])
    else:
        print(reverse_list[q])
