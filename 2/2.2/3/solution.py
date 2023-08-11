#ll

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, value):
        if self.last:
            self.last.next = value
        self.last = value
        if self.top is None:
            self.top = value

    def pop(self):
        height = self.top
        if height is None:
            return
        while height.next != self.last:
            height = height.next
        if height:
            height.next = None
        last = self.last
        self.last = height
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        stack = []
        height = self.top
        while height is not None:
            stack.append(height.data)
            height = height.next
        return stack


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)
