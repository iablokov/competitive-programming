from typing import Optional, Any, Callable
from operator import add

class SegmentTree:

    data    : list[int | float]
    op      : Callable
    default : Callable
    size    : int
    offset  : int

    def __init__(self, data: list[int | float], op: Callable, default: Callable):
        self.default = default
        self.op = op

        self.size = len(data)
        self.offset = 1 << (self.size-1).bit_length()
        self.data = [default() for _ in range(self.offset)] + data

        self._build_tree()

    def _build_tree(self):
        for i in reversed(range(1,self.offset)):
            l, r = 2*i, 2*i+1
            lval = self.data[l] if l < self.offset + self.size else self.default()
            rval = self.data[r] if r < self.offset + self.size else self.default()
            self.data[i] = self.op(lval, rval)
    
    def update(self, i: int, val: int | float):
        i += self.offset
        self.data[i] = val
        while i > 1:
            i //= 2
            l, r = 2*i, 2*i+1
            lval = self.data[l] if l < self.offset + self.size else self.default()
            rval = self.data[r] if r < self.offset + self.size else self.default()
            self.data[i] = self.op(lval, rval)

    def query_with(self, l: int, r: int, op: Callable, default: Callable) -> Any:
        if l < 0 or r > self.size : return None
        res = default()
        l += self.offset
        r += self.offset
        rr = self.offset + self.size
        while l < r:
            if l % 2 == 1: 
                res = op(res, self.data[l])
            if r % 2 == 1 and r < rr: 
                res = op(res, self.data[r-1])

            l = (l+1) // 2
            r = (r + int(r==rr)) // 2
            rr = (rr+1) // 2
        return res

    def query(self, l: int, r: int) -> Optional[Any]:
        return self.query_with(l, r, self.op, self.default)

data = [1, 2, 3, 4, 5, 6, 7]
st = SegmentTree(data, add, lambda : 0)
print(st.data)
#st.update(6,8)
#print(st.data)

q = st.query(1,4)
print(q)
