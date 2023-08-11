class Graph:
    LIMIT_Y = [0, 10]
    data = None
    final = []

    def set_data(self, data):
        self.data = data

    def draw(self):
        if self.data:
            for i in self.data:
                if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
                    self.final.append(str(i))
        st = ' '.join(self.final)
        print(st)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
