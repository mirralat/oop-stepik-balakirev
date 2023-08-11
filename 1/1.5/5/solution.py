class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def closed(self):
        return 'Отображение данных закрыто'

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show is True:
            print(' '.join(map(str, self.data)))
        else:
            print(self.closed())

    def show_graph(self):
        if self.is_show is True:
            print('Графическое отображение данных:', ' '.join(map(str, self.data)))
        else:
            print(self.closed())

    def show_bar(self):
        if self.is_show is True:
            print('Столбчатая диаграмма:', ' '.join(map(str, self.data)))
        else:
            print(self.closed())

    def set_show(self, fl_show):
        if type(fl_show is bool):
            self.is_show = fl_show


data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
