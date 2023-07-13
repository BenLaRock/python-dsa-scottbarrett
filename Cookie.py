class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

c2 = Cookie('red')
print(c2)

print(c2.get_color())