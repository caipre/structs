class Color(object):
    Black = 'black'
    Red = 'red'

class RedBlackTree(object):
    """Implementation of a Left-Leaning Red/Black Tree
    """

    def __init__(self, key=None, val=None, color=Color.Red, null=False):
        self.key = key
        self.val = val
        self.color = color
        self.left = None if null else RedBlackTree(color=Color.Black, null=True)
        self.right = None if null else RedBlackTree(color=Color.Black, null=True)
        self.is_null = null

    # public api
    #

    def put(self, key, val):
        if self.is_null:      return RedBlackTree(key, val)
        elif not self.key:    self.assign(key, val, Color.Black)
        elif key == self.key: self.assign(key, val)
        elif key < self.key:  self.left = self.left.put(key, val)
        else:                 self.right = self.right.put(key, val)

        return self.rebalance()

    def get(self, key):
        node = self.find(key)
        if node is None:
            raise KeyError
        return node.val

    def rm(self, key):
        pass

    def show(self):
        def nodestr(node):
            return node.key if node.key else '-'
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.is_null: continue
            print('node:', node.key, '->', node.val, '\n',
                  ' colr:', node.color, '\n',
                  ' left:', nodestr(node.left), '\n',
                  ' rght:', nodestr(node.right), '\n')
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    # private
    #

    def assign(self, key, val, color=None):
        self.key = key
        self.val = val
        if color: self.color = color
        return self

    def swap(self, other):
        self.key, other.key = other.key, self.key
        self.val, other.val = other.val, self.val

    def find(self, key):
        if self.is_null:      return None
        elif key == self.key: return self
        elif key < self.key:  return self.left.find(key)
        else:                 return self.right.find(key)

    def is_red(self):
        return self.color == Color.Red

    def is_black(self):
        return self.color == Color.Black

    def rebalance(self):
        node = self
        if self.left.is_black() and self.right.is_red():
            node = self.rotate_left()
        if self.left.is_red() and self.left.left.is_red():
            node = self.rotate_right()
        if self.left.is_red() and self.right.is_red():
            node = self.flip_colors()
        return node

    #      Y             X
    #    X   g   -->   a   Y
    #   a b      <--      b g

    def rotate_left(self):
        right = self.right
        self.right = right.left
        right.left = self
        right.color = self.color
        self.color = Color.Red
        return right

    def rotate_right(self):
        left = self.left
        self.left = left.right
        left.right = self
        left.color = self.color
        self.color = Color.Red
        return left

    def flip_colors(self):
        self.color = Color.Red
        self.left.color = Color.Black
        self.right.color = Color.Black
        return self

rbt = RedBlackTree()
rbt = rbt.put('S', 'one')
rbt = rbt.put('E', 'two')
rbt = rbt.put('A', 'three')
rbt = rbt.put('R', 'four')
rbt = rbt.put('C', 'five')
rbt = rbt.put('H', 'six')
rbt = rbt.put('X', 'seven')
rbt = rbt.put('M', 'eight')
rbt = rbt.put('P', 'nine')
rbt = rbt.put('L', 'ten')

assert rbt.get('S') == 'one'
assert rbt.get('E') == 'two'
assert rbt.get('A') == 'three'
assert rbt.get('R') == 'four'
assert rbt.get('C') == 'five'
assert rbt.get('H') == 'six'


