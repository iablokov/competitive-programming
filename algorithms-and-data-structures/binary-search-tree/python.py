from typing import Optional, Iterable

class BSTNode:

    left  : Optional["BSTNode"]
    right : Optional["BSTNode"]
    val   : int

    def __init__(self):
        pass

    def insert(self, val: int) -> "BSTNode":
        pass

    def search(self, val: int) -> Optional["BSTNode"]:
        pass

    def delete(self, val: int) -> Optional["BSTNode"]:
        pass

    def balance(self) -> "BSTNode":
        pass

    def inorder(self) -> Iterable["BSTNode"]:
        # yield
        pass