class AppStore:
    def __init__(self):
        self.apps = []

    def add_application(self, name):
        self.apps.append(name)

    def remove_application(self, name):
        self.apps.remove(name)

    def total_apps(self):
        return len(self.apps)


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")

store.add_application(app_youtube)
store.remove_application(app_youtube)
print(store.apps)