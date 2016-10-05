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

    def add(self, key, val):
        if self.is_null:      return RedBlackTree(key, val)
        elif not self.key:    self.assign(key, val, Color.Black)
        elif key == self.key: self.assign(key, val)
        elif key < self.key:  self.left = self.left.add(key, val)
        else:                 self.right = self.right.add(key, val)

        self.rebalance()
        return self

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
        if key == self.key:
            return self
        elif key < self.key:
            return self.left.find(key)
        else:
            return self.right.find(key)

    def is_red(self):
        return self.color == Color.Red

    def is_black(self):
        return self.color == Color.Black

    def rebalance(self):
        if self.left.is_black() and self.right.is_red():
            self.rotate_left()
        if self.left.is_red() and self.left.left.is_red():
            self.rotate_right()
        if self.left.is_red() and self.right.is_red():
            self.flip_colors()

    #      Y             X
    #    X   g   -->   a   Y
    #   a b      <--      b g

    def rotate_left(self):
        alpha = self.left
        beta = self.right.left
        right = self.right
        gamma = self.right.right

        self.left = right
        self.right = gamma
        right.left = alpha
        right.right = beta
        self.swap(right)


    def rotate_right(self):
        alpha = self.left.left
        beta = self.left.right
        left = self.left
        gamma = self.right

        self.left = alpha
        self.right = left
        left.left = beta
        left.right = gamma
        self.swap(left)

    def flip_colors(self):
        self.color = Color.Red
        self.left.color = Color.Black
        self.right.color = Color.Black

rbt = RedBlackTree()
rbt.add('S', 'one')
rbt.add('E', 'two')
rbt.add('A', 'three')
rbt.add('R', 'four')
rbt.add('C', 'five')
rbt.add('H', 'six')
rbt.add('X', 'seven')
rbt.add('M', 'eight')
rbt.add('P', 'nine')
rbt.add('L', 'ten')

assert rbt.get('S') == 'one'
assert rbt.get('E') == 'two'
assert rbt.get('A') == 'three'
assert rbt.get('R') == 'four'
assert rbt.get('C') == 'five'
assert rbt.get('H') == 'six'


