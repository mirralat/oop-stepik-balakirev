class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, object):
        self.__left = object

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, object):
        self.__right = object


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        height = root
        while height:
            if x[height.indx] == 1:
                height = height.left
            else:
                height = height.right
            if height.left is None:
                break
        return height.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"

