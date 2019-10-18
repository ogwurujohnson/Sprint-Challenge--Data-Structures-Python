class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Check new node val  < current nodes val
        if value < self.value:
            # if no left child place new node
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise repeat process
                self.left.insert(value)
            # check new node val >= current nodes val
        if value >= self.value:
            # if no right child place new node
            if not self.right:
                self.right = BinarySearchTree(value)
            # otherwise repeat process
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)