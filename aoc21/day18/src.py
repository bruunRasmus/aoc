lines = open("input.txt").read().strip().splitlines()

def parseP(str):
    if str[0] not in ["[","]",","]:
        return Node(int(str[0]))
    elif str[0] == "[":
        opened  = 0
        for i in range(len(str)):
            c = str[i]
            opened += c == "["
            opened -= c == "]"
            if opened == 1 and c == ",":
                a = parseP(str[1:i])
                b = parseP(str[i+1:-1])
                T = add_trees(a,b)
                return T
            
class Node():
    def __init__(self,value = None):
        self.value = value
        self.a = None
        self.b = None
        self.parent = None
        
    def __str__(self):
        if self.value != None:
            return str(self.value)
        else:
            return f"[{self.a.__str__()},{self.b.__str__()}]"
    def update_value(self,v):
        self.value = v
    def update_a(self,child_a):
        self.a = child_a
        self.a.parent = self
    def update_b(self,child_b):
        self.b = child_b
        self.b.parent = self
        
def find_nb(node, rightmost=True):
    parent_attr = 'b' if rightmost else 'a'
    child_attr = 'a' if rightmost else 'b'
    try:
        while getattr(node.parent, parent_attr) is node:
            node = node.parent
        # step to sibling
        node = getattr(node.parent, parent_attr)
        # descend to the extreme child
        while getattr(node, child_attr):
            node = getattr(node, child_attr)
        return node
    except AttributeError:
        return None

def explode(T, level=1):
    if T.value is not None:
        return 0

    if level <= 4:
        return explode(T.a, level + 1) or explode(T.b, level + 1)

    lm = find_nb(T, rightmost=False)
    rm = find_nb(T, rightmost=True)
    if lm:
        lm.update_value(lm.value + T.a.value)
    if rm:
        rm.update_value(rm.value + T.b.value)

    T.update_value(0)
    T.a = None
    T.b = None
    return 1

def split(T):
    if T.value is not None and T.value >= 10:
        a = T.value // 2
        b = T.value - a
        T.update_a(Node(a))
        T.update_b(Node(b))
        T.update_value(None)
        return 1

    return (T.a and split(T.a)) or (T.b and split(T.b)) or 0
    
def add_trees(t1,t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t = Node()
    t.update_a(t1)
    t.update_b(t2)
    return t

def reduce(T):
    while True:
        if explode(T):
            continue
        if not split(T):
            break

def magnitude(T):
     if T.value is not None:
         return T.value
     else:
         return 3*magnitude(T.a) + 2*magnitude(T.b)

T1 = None
for l in lines:
    T2 = parseP(l)
    T1 = add_trees(T1,T2)
    reduce(T1)
  
print(magnitude(T1))
ans2 = 0
for l1 in lines:
    for l2 in lines:
        if l1 != l2:
            T1 = parseP(l1)
            T2 = parseP(l2)
            T = add_trees(T1,T2)
            reduce(T)
            magn = magnitude(T)
            if magn > ans2:
                ans2 = magn
            
print(ans2)