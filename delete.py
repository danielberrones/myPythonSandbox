class Men:
    def __init__(self):
        self.attitude = "Large"
    def bark(self):
        return self.attitude
    

m = Men()
print(m.bark())