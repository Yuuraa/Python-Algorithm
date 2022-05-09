import sys


class Set:
    def __init__(self) -> None:
        self.items = set([])
    
    def check(self, x):
        print(int(x in self.items))

    def add(self, x):
        self.items.add(x)

    def remove(self, x):
        self.items -= set([x])  

    def toggle(self, x):
        if x in self.items: self.remove(x)
        else: self.add(x)
    
    def all(self):
        self.items = set([i for i in range(1, 21)])
    
    def empty(self):
        self.items = set([])


def main():
    n_ops = int(sys.stdin.readline())
    set_obj = Set()
    for _ in range(n_ops):
        op_str = sys.stdin.readline().strip("\n")
        
        if op_str in ["all", "empty"]:
            getattr(set_obj, op_str)()
        else:
            op, val = op_str.split()
            getattr(set_obj, op)(int(val))


main()