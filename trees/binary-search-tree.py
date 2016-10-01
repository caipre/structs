class BinarySearchTree(object):
    def __init__(self, key=None, val=None, parent=None, left=None, right=None):
        self.size_ = 1 if key else 0

        self.key = key
        self.val = val

        self.root = self
        self.parent = parent
        self.left = left
        self.right = right

    def is_ordered(self):
        if self.left:
            if not self.left.key < self.key: return False
            if not self.left.is_ordered(): return False
        if self.right:
            if not self.right.key > self.key: return False
            if not self.right.is_ordered(): return False
        return True

    def size(self):
        return self.size_

    def min(self):
        if not self.key:
            return None
        tree = self
        while tree.left:
            tree = tree.left
        return tree

    def max(self):
        if not self.key:
            return None
        tree = self
        while tree.right:
            tree = tree.right
        return tree

    def insert(self, key, val):
        if not self.key:
            # special case for first root
            self.key = key
            self.val = val
        elif key == self.key:
            return
        elif key < self.key:
            if not self.left:
                self.left = BinarySearchTree(key, val, parent=self)
            else:
                self.left.insert(key, val)
        else:
            if not self.right:
                self.right = BinarySearchTree(key, val, parent=self)
            else:
                self.right.insert(key, val)

        self.size_ += 1

    def delete(self, key):
        def stitch(parent, key, tree):
            if key < parent.key:
                parent.left = tree
            else:
                parent.right = tree
            tree.parent = parent

        if not self.key:
            raise KeyError
        if key == self.key:
            if not self.parent:
                # root, special case
                return NotImplemented
            if self.left and self.right:
                if self.key < self.parent.key:
                    min = self.right.min()
                    self.key, self.val = min.key, min.val
                    self.right.delete(min.key)
                else:
                    max = self.left.max()
                    self.key, self.val = max.key, max.val
                    self.left.delete(max.key)
            else:
                stitch(self.parent, self.key, self.left or self.right)
                self.parent.size_ -= 1
        elif key < self.key:
            if not self.left:
                raise KeyError
            self.left.delete(key)
        else:
            if not self.right:
                raise KeyError
            self.right.delete(key)

    def search(self, key):
        if not self.key:
            return None

        if key == self.key:
            return self
        elif key < self.key:
            if not self.left:
                return None
            else:
                return self.left.search(key)
        else:
            if not self.right:
                return None
            else:
                return self.right.search(key)

    def get(self, key):
        if not self.key:
            raise KeyError

        tree = self.search(key)
        if not tree:
            raise KeyError
        return tree.val

    def display(self):
        def treestr(tree):
            return tree.key if tree else ''

        queue = [self]
        while queue:
            tree = queue[0]
            if tree.left: queue.append(tree.left)
            if tree.right: queue.append(tree.right)
            print(tree.key, 'left:', treestr(tree.left), 'right:', treestr(tree.right))
            queue = queue[1:]
        print()



bst = BinarySearchTree()
bst.insert(2, "2")
bst.insert(1, "1")
bst.insert(3, "3")
assert bst.is_ordered()

assert bst.get(1) == "1"
assert bst.get(2) == "2"
assert bst.get(3) == "3"

assert bst.search(1) == bst.left
assert bst.search(2) == bst.root
assert bst.search(3) == bst.right

assert bst.root.size() == 3
assert bst.left.size() == 1
assert bst.right.size() == 1

assert bst.min().val == "1"
assert bst.max().val == "3"

bst.delete(1)
assert bst.left is None
assert bst.root.size() == 2
assert bst.search(1) is None
assert bst.is_ordered()

bst.delete(3)
assert bst.right is None
assert bst.root.size() == 1
assert bst.search(3) is None
assert bst.is_ordered()

#bst.delete(2)
#assert bst.root is None
#assert bst.size() == 0
#assert bst.search(2) is None

bst.insert(1, "1")
bst.insert(0, "0")
bst.insert(1.5, "1.5")
bst.delete(1)
assert bst.is_ordered()

assert bst.root.left.val == "1.5"
