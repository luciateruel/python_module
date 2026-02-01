class HistoryDict:
    def __init__(self, data):
        self.data = data
        if data:
            self.key, self.value = list(data.items())[0]
            self.d = {self.key:self.value}
        else:
            self.d = {}
        self.last_5 = []

    def get_history(self):
        return self.last_5[-5:]

    def set_value(self, key, value):
        self.d[key] = value
        print(self.d)
        self.last_5.append(key)



d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()
