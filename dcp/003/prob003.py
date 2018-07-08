
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val # assume string
        self.left = left
        self.right = right

def serialize(n):
    if n is None:
        return "None"
    escaped_val = (n.val or "").replace("'", "\\'")
    return f"Node('{escaped_val}', {serialize(n.left)}, {serialize(n.right)})"

def deserialize(str):
    return eval(str)